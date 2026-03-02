# Challenge Room 05 - Pipeline RAG interractif pour fichiers texte
# Ce script charge un fichier .txt passé en argument, construit un index
# vectoriel et lance une boucle de questions-reponses contextualisée.

import sys
import os

import chromadb
from sentence_transformers import SentenceTransformer

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from utils import creer_client, MODELE
from rag_utils import decouper_en_segments


def charger_fichier_texte(chemin):
    """Charge un fichier .txt et retourne son contenu complet."""
    if not os.path.exists(chemin):
        print(f"Erreur : le fichier '{chemin}' n'éxiste pas.")
        print("Veuillez fournir un chemin valide vers un fichier .txt")
        sys.exit(1)

    with open(chemin, "r", encoding="utf-8") as f:
        texte = f.read()
    return texte


def construire_index(segments, modele_embedding):
    """Crée l'index vectoriel dans ChromaDB a partir des segments."""
    print("Géneration des embeddings...")
    embeddings = modele_embedding.encode(segments)

    client_chroma = chromadb.Client()
    collection = client_chroma.get_or_create_collection(name="challenge_rag")
    collection.add(
        documents=segments,
        embeddings=[emb.tolist() for emb in embeddings],
        ids=[f"seg_{i}" for i in range(len(segments))]
    )
    return collection


def rechercher_contexte(question, collection, modele_embedding, n_resultats=3):
    """Recherche les segments les plus pertinants pour la question posée."""
    vecteur_q = modele_embedding.encode([question])[0]
    resultats = collection.query(
        query_embeddings=[vecteur_q.tolist()],
        n_results=n_resultats
    )
    return resultats["documents"][0], resultats["distances"][0]


def generer_reponse(client_llm, question, passages):
    """Envoi les passages et la question au LLM pour une reponse contextualisée."""
    contexte = "\n---\n".join(passages)

    prompt = (
        f"Voici des extraits d'un document :\n"
        f"---\n{contexte}\n---\n\n"
        f"En te basant UNIQUEMENT sur ces extraits, reponds à la question suivante.\n"
        f"Si l'information n'est pas dans les extraits, dis-le explicitment.\n"
        f"Cite les passages pertinents dans ta reponse.\n\n"
        f"Question : {question}"
    )

    reponse = client_llm.chat.completions.create(
        model=MODELE,
        messages=[
            {"role": "system", "content": "Tu es un assistant qui repond uniquement à partir des documents fournis."},
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=500
    )
    return reponse.choices[0].message.content


# --- Programme princippal ---

if __name__ == "__main__":
    # Verification de l'argument en ligne de commande
    if len(sys.argv) < 2:
        print("Usage : python challenge_room05.py <chemin_fichier.txt>")
        print("Exemple : python challenge_room05.py ../../datasets/texte_entreprise.txt")
        sys.exit(1)

    chemin_fichier = sys.argv[1]

    # Etape 1 : Chargement du fichier texte
    print("=== Chargement du fichier ===")
    texte = charger_fichier_texte(chemin_fichier)
    print(f"Fichier chargé : {chemin_fichier}")
    print(f"Caracteres : {len(texte)} | Mots : {len(texte.split())}")
    print()

    # Etape 2 : Decoupage en segments
    print("=== Decoupage en segments ===")
    segments = decouper_en_segments(texte, taille_segment=200, chevauchement=30)
    print(f"Segments crées : {len(segments)}")
    print()

    # Etape 3 : Creation de l'index vectoriel
    print("=== Construction de l'index vectoriel ===")
    modele_emb = SentenceTransformer("all-MiniLM-L6-v2")
    collection = construire_index(segments, modele_emb)
    print(f"Index prêt : {collection.count()} segments indexés.")
    print()

    # Etape 4 : Connexion au LLM
    client_llm = creer_client()

    # Etape 5 : Boucle interractive
    print("=== Systeme RAG prêt ===")
    print("Posez vos questions sur le document. Tapez 'quitter' pour arretter.")
    print()

    while True:
        question = input("Question : ").strip()

        if question.lower() == "quitter":
            print("Au revoir !")
            break

        if not question:
            continue

        # Recherche des passages pertinants
        passages, distances = rechercher_contexte(question, collection, modele_emb)

        # Affichage des sources utilisée
        print("\n--- Passages sources ---")
        for i, (passage, dist) in enumerate(zip(passages, distances)):
            print(f"\n[Source {i+1}] (distance : {dist:.4f})")
            print(passage[:300] + ("..." if len(passage) > 300 else ""))

        # Generation de la reponse
        print("\n--- Reponse ---")
        reponse = generer_reponse(client_llm, question, passages)
        print(reponse)
        print()
