# Projet B — Assistant entreprise avec RAG et citation des sources
# Room 07 — Projets guidés

import os
import chromadb
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client_openai = OpenAI()


def charger_texte(chemin):
    """Charge un fichier texte et retourne son contenu."""
    with open(chemin, "r", encoding="utf-8") as f:
        return f.read()


def decouper_en_segments(texte, taille=300, chevauchement=50):
    """Découpe un texte en segments avec chevauchement."""
    mots = texte.split()
    segments = []
    debut = 0
    while debut < len(mots):
        fin = debut + taille
        segment = " ".join(mots[debut:fin])
        segments.append(segment)
        debut += taille - chevauchement
    return segments


def construire_index(segments, modele_emb):
    """Crée un index ChromaDB à partir des segments."""
    embeddings = modele_emb.encode(segments)
    client_chroma = chromadb.Client()
    collection = client_chroma.get_or_create_collection(name="entreprise")
    collection.add(
        documents=segments,
        embeddings=[e.tolist() for e in embeddings],
        ids=[f"seg_{i}" for i in range(len(segments))]
    )
    return collection


def rechercher_passages(question, collection, modele_emb, n=3):
    """
    Recherche les passages les plus pertinents pour la question.

    A COMPLETER :
    - Convertir la question en vecteur
    - Interroger la collection ChromaDB
    - Retourner les documents trouvés
    """
    # A COMPLETER
    pass


def generer_reponse(question, passages):
    """
    Génère une réponse à partir des passages trouvés.

    A COMPLETER :
    - Construire un prompt RAG qui inclut les passages comme contexte
    - Instruire le modèle à répondre uniquement à partir du contexte
    - Instruire le modèle à citer les passages sources
    - Si l'information n'est pas dans les passages, le dire explicitement
    - Retourner la réponse du modèle
    """
    # A COMPLETER
    pass


# --- Programme principal ---

# Chargement et indexation du document
chemin = os.path.join(os.path.dirname(__file__), "..", "..", "..", "datasets", "texte_entreprise.txt")
print("Chargement du document d'entreprise...")
texte = charger_texte(chemin)
segments = decouper_en_segments(texte)

print("Création de l'index...")
modele = SentenceTransformer("all-MiniLM-L6-v2")
collection = construire_index(segments, modele)
print(f"Index prêt : {collection.count()} segments.")
print()

print("=== Assistant entreprise ===")
print("Posez vos questions sur le document. Tapez 'quitter' pour arrêter.")
print()

while True:
    question = input("Question : ").strip()

    if question.lower() == "quitter":
        print("Au revoir.")
        break

    if not question:
        continue

    passages = rechercher_passages(question, collection, modele)
    if passages:
        print("\n--- Sources ---")
        for i, p in enumerate(passages):
            print(f"  [{i+1}] \"{p[:120]}...\"")

        reponse = generer_reponse(question, passages)
        print(f"\n--- Réponse ---\n{reponse}\n")
    else:
        print("Aucun passage pertinent trouvé.\n")
