# Script 16 — Recherche vectorielle : trouver les segments les plus pertinents
# Room 05 — Créer un système RAG

import fitz
import os
import chromadb
from sentence_transformers import SentenceTransformer


def charger_pdf(chemin):
    document = fitz.open(chemin)
    texte = ""
    for page in document:
        texte += page.get_text() + "\n"
    document.close()
    return texte


def decouper_en_segments(texte, taille_segment=300, chevauchement=50):
    mots = texte.split()
    segments = []
    debut = 0
    while debut < len(mots):
        fin = debut + taille_segment
        segment = " ".join(mots[debut:fin])
        segments.append(segment)
        debut += taille_segment - chevauchement
    return segments


# Reconstruction de l'index (en mémoire, il faut le recréer à chaque exécution)
chemin_pdf = os.path.join(os.path.dirname(__file__), "..", "..", "..", "datasets", "rapport_fictif.pdf")
texte = charger_pdf(chemin_pdf)
segments = decouper_en_segments(texte)

modele_embedding = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = modele_embedding.encode(segments)

client_chroma = chromadb.Client()
collection = client_chroma.get_or_create_collection(name="rapport")
collection.add(
    documents=segments,
    embeddings=[emb.tolist() for emb in embeddings],
    ids=[f"segment_{i}" for i in range(len(segments))]
)

# La question à poser
question = "Quels sont les objectifs principaux décrits dans le rapport ?"

print(f"=== Recherche vectorielle ===")
print(f"Question : {question}")
print()

# Conversion de la question en vecteur
vecteur_question = modele_embedding.encode([question])[0]

# Recherche des 3 segments les plus proches
# query() retourne les documents les plus similaires au vecteur fourni
resultats = collection.query(
    query_embeddings=[vecteur_question.tolist()],
    n_results=3  # On veut les 3 segments les plus pertinents
)

# Affichage des résultats
print(f"=== Segments trouvés (top 3) ===")
for i, (doc, distance) in enumerate(zip(resultats["documents"][0], resultats["distances"][0])):
    # La distance est inversement proportionnelle à la similarité
    # Plus la distance est faible, plus le segment est pertinent
    print(f"\n--- Segment {i+1} (distance : {distance:.4f}) ---")
    print(doc[:300] + "..." if len(doc) > 300 else doc)
