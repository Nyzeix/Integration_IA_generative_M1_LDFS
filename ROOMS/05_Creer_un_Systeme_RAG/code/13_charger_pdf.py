# Script 13 - Charger et extraire le texte d'un fichier PDF
# Room 05 - Creer un systeme RAG

from rag_utils import charger_pdf, chemin_dataset

# Chemin vers le fichier PDF a charger
chemin_pdf = chemin_dataset("rapport_fictif.pdf")

# Chargement du PDF avec PyMuPDF (via rag_utils)
texte_complet = charger_pdf(chemin_pdf)

# Affichage du resultat
print("=== Chargement du PDF ===")
print(f"Fichier : {chemin_pdf}")
print(f"Caracteres extraits : {len(texte_complet)}")
print(f"Mots extraits       : {len(texte_complet.split())}")
print()

# On affiche les 1000 premiers caracteres pour verifier
print("=== Texte extrait (1000 premiers caracteres) ===")
print()
print(texte_complet[:1000])
print()
print(f"... (tronque, {len(texte_complet) - 1000} caracteres restants)")
