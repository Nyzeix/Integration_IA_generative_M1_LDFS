# Script 13 — Charger et extraire le texte d'un fichier PDF
# Room 05 — Créer un système RAG

import fitz  # PyMuPDF — la bibliothèque s'importe sous le nom "fitz"
import os

# Chemin vers le fichier PDF à charger
# On remonte à la racine du dépôt pour accéder au dossier datasets
chemin_pdf = os.path.join(os.path.dirname(__file__), "..", "..", "..", "datasets", "rapport_fictif.pdf")

# Vérification que le fichier existe
if not os.path.exists(chemin_pdf):
    print(f"Erreur : le fichier '{chemin_pdf}' n'a pas été trouvé.")
    print("Vérifiez que le dossier datasets/ contient rapport_fictif.pdf")
    exit(1)

# Ouverture du PDF avec PyMuPDF
# fitz.open() retourne un objet document qu'on peut parcourir page par page
document = fitz.open(chemin_pdf)

print(f"=== Chargement du PDF ===")
print(f"Fichier : {chemin_pdf}")
print(f"Nombre de pages : {len(document)}")
print()

# Extraction du texte de chaque page
texte_complet = ""
for numero_page in range(len(document)):
    # get_text() extrait tout le texte de la page
    page = document[numero_page]
    texte_page = page.get_text()
    texte_complet += texte_page + "\n"

# Fermeture du document
document.close()

# Affichage du résultat
print(f"=== Texte extrait ({len(texte_complet)} caractères) ===")
print()
# On affiche les 1000 premiers caractères pour vérifier
print(texte_complet[:1000])
print()
print(f"... (tronqué, {len(texte_complet) - 1000} caractères restants)")
print()
print(f"Nombre total de mots : {len(texte_complet.split())}")
