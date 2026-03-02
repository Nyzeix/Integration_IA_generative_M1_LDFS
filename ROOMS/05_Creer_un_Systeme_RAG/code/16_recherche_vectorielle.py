# Script 16 - Recherche vectorielle : trouver les segments les plus pertinents
# Room 05 - Creer un systeme RAG

import chromadb
from sentence_transformers import SentenceTransformer
from rag_utils import charger_pdf, decouper_en_segments, chemin_dataset

# Reconstruction de l'index (en memoire, il faut le recreer a chaque execution)
chemin_pdf = chemin_dataset("rapport_fictif.pdf")
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

# La question a poser
question = "Quels sont les objectifs principaux decrits dans le rapport ?"

print("=== Recherche vectorielle ===")
print(f"Question : {question}")
print()

# Conversion de la question en vecteur
vecteur_question = modele_embedding.encode([question])[0]

# Recherche des 3 segments les plus proches
resultats = collection.query(
    query_embeddings=[vecteur_question.tolist()],
    n_results=3
)

# Affichage des resultats
print("=== Segments trouves (top 3) ===")
for i, (doc, distance) in enumerate(zip(resultats["documents"][0], resultats["distances"][0])):
    print(f"\n--- Segment {i+1} (distance : {distance:.4f}) ---")
    print(doc[:300] + "..." if len(doc) > 300 else doc)
