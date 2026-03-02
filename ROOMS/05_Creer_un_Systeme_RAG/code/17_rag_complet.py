# Script 17 - Pipeline RAG complet : question -> recherche -> reponse contextualisee
# Room 05 - Creer un systeme RAG

import sys
import os
import chromadb
from sentence_transformers import SentenceTransformer

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from utils import creer_client, MODELE
from rag_utils import charger_pdf, decouper_en_segments, chemin_dataset

client_llm = creer_client()


def construire_index(segments, modele_embedding):
    """Cree l'index vectoriel ChromaDB a partir des segments."""
    embeddings = modele_embedding.encode(segments)
    client_chroma = chromadb.Client()
    collection = client_chroma.get_or_create_collection(name="rapport_rag")
    collection.add(
        documents=segments,
        embeddings=[emb.tolist() for emb in embeddings],
        ids=[f"seg_{i}" for i in range(len(segments))]
    )
    return collection


def rechercher_contexte(question, collection, modele_embedding, n_resultats=3):
    """Recherche les segments les plus pertinents pour la question."""
    vecteur_q = modele_embedding.encode([question])[0]
    resultats = collection.query(
        query_embeddings=[vecteur_q.tolist()],
        n_results=n_resultats
    )
    return resultats["documents"][0]


def generer_reponse_rag(question, passages):
    """Envoie les passages et la question au LLM pour obtenir une reponse contextualisee."""
    contexte = "\n---\n".join(passages)

    prompt = (
        f"Voici des extraits d'un document :\n"
        f"---\n{contexte}\n---\n\n"
        f"En te basant UNIQUEMENT sur ces extraits, reponds a la question suivante.\n"
        f"Si l'information n'est pas dans les extraits, dis-le explicitement.\n"
        f"Cite les passages pertinents dans ta reponse.\n\n"
        f"Question : {question}"
    )

    reponse = client_llm.chat.completions.create(
        model=MODELE,
        messages=[
            {"role": "system", "content": "Tu es un assistant qui repond uniquement a partir des documents fournis."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=500
    )
    return reponse.choices[0].message.content


# --- Programme principal ---

chemin_pdf = chemin_dataset("rapport_fictif.pdf")
print("Chargement du document...")
texte = charger_pdf(chemin_pdf)
segments = decouper_en_segments(texte)

print("Creation de l'index vectoriel...")
modele_emb = SentenceTransformer("all-MiniLM-L6-v2")
collection = construire_index(segments, modele_emb)
print(f"Index pret : {collection.count()} segments indexes.")
print()

print("=== Systeme RAG pret ===")
print("Posez vos questions sur le document. Tapez 'quitter' pour arreter.")
print()

while True:
    question = input("Question : ").strip()

    if question.lower() == "quitter":
        print("Au revoir.")
        break

    if not question:
        continue

    passages = rechercher_contexte(question, collection, modele_emb)

    print("\n--- Passages trouves ---")
    for i, p in enumerate(passages):
        print(f"[{i+1}] {p[:150]}...")

    print("\n--- Reponse ---")
    reponse = generer_reponse_rag(question, passages)
    print(reponse)
    print()
