# Script 14 — Découper un texte en segments avec chevauchement
# Room 05 — Créer un système RAG

import fitz
import os


def charger_pdf(chemin):
    """Charge un PDF et retourne le texte complet."""
    document = fitz.open(chemin)
    texte = ""
    for page in document:
        texte += page.get_text() + "\n"
    document.close()
    return texte


def decouper_en_segments(texte, taille_segment=300, chevauchement=50):
    """
    Découpe un texte en segments de taille_segment mots,
    avec un chevauchement de 'chevauchement' mots entre segments consécutifs.

    Le chevauchement évite qu'une information importante soit coupée
    à la frontière entre deux segments.
    """
    # Découpage du texte en mots
    mots = texte.split()

    segments = []
    debut = 0

    while debut < len(mots):
        # On prend 'taille_segment' mots à partir de la position 'debut'
        fin = debut + taille_segment
        segment = " ".join(mots[debut:fin])
        segments.append(segment)

        # On avance de (taille_segment - chevauchement) mots
        # Le chevauchement fait que les derniers mots du segment actuel
        # sont aussi les premiers mots du segment suivant
        debut += taille_segment - chevauchement

    return segments


# Chargement du PDF
chemin_pdf = os.path.join(os.path.dirname(__file__), "..", "..", "..", "datasets", "rapport_fictif.pdf")
texte = charger_pdf(chemin_pdf)

# Découpage en segments
segments = decouper_en_segments(texte, taille_segment=300, chevauchement=50)

# Affichage du résultat
print(f"=== Découpage du texte ===")
print(f"Texte original : {len(texte.split())} mots")
print(f"Segments créés  : {len(segments)}")
print()

# Affichage des 3 premiers segments
for i, seg in enumerate(segments[:3]):
    print(f"--- Segment {i+1} ({len(seg.split())} mots) ---")
    print(seg[:200] + "...")  # On affiche les 200 premiers caractères
    print()
