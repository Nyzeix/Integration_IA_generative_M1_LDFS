# Script 14 - Decouper un texte en segments avec chevauchement
# Room 05 - Creer un systeme RAG

from rag_utils import charger_pdf, decouper_en_segments, chemin_dataset

# Chargement du PDF
chemin_pdf = chemin_dataset("rapport_fictif.pdf")
texte = charger_pdf(chemin_pdf)

# Decoupage en segments de 300 mots avec chevauchement de 50 mots
segments = decouper_en_segments(texte, taille_segment=300, chevauchement=50)

# Affichage du resultat
print("=== Decoupage du texte ===")
print(f"Texte original : {len(texte.split())} mots")
print(f"Segments crees  : {len(segments)}")
print()

# Affichage des 3 premiers segments
for i, seg in enumerate(segments[:3]):
    print(f"--- Segment {i+1} ({len(seg.split())} mots) ---")
    print(seg[:200] + "...")
    print()
