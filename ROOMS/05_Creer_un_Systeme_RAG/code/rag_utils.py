# rag_utils.py - Fonctions partagees pour le pipeline RAG
# Room 05 - Creer un systeme RAG
# Ce module est importe par les scripts 13 a 17 pour eviter la duplication de code.

import fitz
import os


def charger_pdf(chemin):
    """Charge un PDF et retourne le texte complet extrait de toutes les pages."""
    if not os.path.exists(chemin):
        print(f"Erreur : le fichier '{chemin}' n'a pas ete trouve.")
        print("Verifiez que le dossier datasets/ contient rapport_fictif.pdf")
        exit(1)

    document = fitz.open(chemin)
    texte = ""
    for page in document:
        texte += page.get_text() + "\n"
    document.close()
    return texte


def decouper_en_segments(texte, taille_segment=300, chevauchement=50):
    """
    Decoupe un texte en segments de taille_segment mots,
    avec un chevauchement de 'chevauchement' mots entre segments consecutifs.

    Le chevauchement evite qu'une information importante soit coupee
    a la frontiere entre deux segments.
    """
    mots = texte.split()
    segments = []
    debut = 0

    while debut < len(mots):
        fin = debut + taille_segment
        segment = " ".join(mots[debut:fin])
        segments.append(segment)
        debut += taille_segment - chevauchement

    return segments


def chemin_dataset(nom_fichier):
    """Retourne le chemin absolu vers un fichier du dossier datasets/."""
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "datasets", nom_fichier)
