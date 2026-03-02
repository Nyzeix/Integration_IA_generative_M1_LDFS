# Script 15 — Créer les embeddings et les stocker dans ChromaDB
# Room 05 — Créer un système RAG

import fitz
import os
import chromadb
from sentence_transformers import SentenceTransformer


def charger_pdf(chemin):
    """Charge un PDF et retourne le texte complet."""
    document = fitz.open(chemin)
    texte = ""
    for page in document:
        texte += page.get_text() + "\n"
    document.close()
    return texte


def decouper_en_segments(texte, taille_segment=300, chevauchement=50):
    """Découpe un texte en segments avec chevauchement."""
    mots = texte.split()
    segments = []
    debut = 0
    while debut < len(mots):
        fin = debut + taille_segment
        segment = " ".join(mots[debut:fin])
        segments.append(segment)
        debut += taille_segment - chevauchement
    return segments


# Chargement du PDF et découpage
chemin_pdf = os.path.join(os.path.dirname(__file__), "..", "..", "..", "datasets", "rapport_fictif.pdf")
texte = charger_pdf(chemin_pdf)
segments = decouper_en_segments(texte)

print(f"=== Création des embeddings ===")
print(f"Segments à vectoriser : {len(segments)}")
print()

# Chargement du modèle d'embedding
# all-MiniLM-L6-v2 est un modèle léger et rapide
# Il transforme du texte en vecteurs de 384 dimensions
print("Chargement du modèle d'embedding (all-MiniLM-L6-v2)...")
modele_embedding = SentenceTransformer("all-MiniLM-L6-v2")
print("Modèle chargé.")
print()

# Création des embeddings pour tous les segments
# encode() prend une liste de textes et retourne une liste de vecteurs
embeddings = modele_embedding.encode(segments)
print(f"Embeddings créés : {len(embeddings)} vecteurs de {len(embeddings[0])} dimensions")
print()

# Visualisation : les 10 premiers nombres du premier vecteur
print("=== Exemple de vecteur (10 premières dimensions) ===")
print([round(float(x), 4) for x in embeddings[0][:10]])
print()

# Stockage dans ChromaDB
# ChromaDB crée une base de données locale dans un dossier
client_chroma = chromadb.Client()

# On crée (ou récupère) une collection nommée "rapport"
# get_or_create_collection évite les erreurs si la collection existe déjà
collection = client_chroma.get_or_create_collection(name="rapport")

# Ajout des segments et de leurs embeddings dans la collection
# Chaque document reçoit un identifiant unique (id)
collection.add(
    documents=segments,
    embeddings=[emb.tolist() for emb in embeddings],
    ids=[f"segment_{i}" for i in range(len(segments))]
)

print(f"=== Indexation terminée ===")
print(f"{collection.count()} segments stockés dans ChromaDB.")
