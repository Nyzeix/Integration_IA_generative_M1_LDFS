# main_starter.py - Squelette de demarrage pour le projet final
# Room 08 - Projet final
#
# Ce fichier fournit une structure de base. Adaptez-le a votre cas d'usage.
# Les sections marquees "A COMPLETER" doivent etre remplies par l'etudiant.

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

from utils import creer_client, MODELE

client = creer_client()


# --- Section 1 : Chargement des donnees ---

def charger_donnees(chemin):
    """
    Charge les donnees de votre projet (texte, PDF, CSV...).
    A COMPLETER selon votre cas d'usage.
    """
    # A COMPLETER
    pass


# --- Section 2 : Indexation (si RAG) ---

def indexer_documents(donnees):
    """
    Cree un index vectoriel a partir des donnees chargees.
    A COMPLETER si votre projet utilise du RAG.
    """
    # A COMPLETER
    pass


# --- Section 3 : Construction du prompt ---

def construire_prompt(question, contexte=None):
    """
    Construit un prompt structure avec role, contexte et contraintes.
    A COMPLETER.
    """
    # A COMPLETER
    prompt = f"Question : {question}"
    return prompt


# --- Section 4 : Appel au modele ---

def interroger_modele(prompt):
    """Envoie le prompt au LLM et retourne la reponse."""
    reponse = client.chat.completions.create(
        model=MODELE,
        messages=[
            {"role": "system", "content": "Tu es un assistant."},  # A PERSONNALISER
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=500
    )
    return reponse.choices[0].message.content


# --- Section 5 : Analyse des risques ---

def verifier_reponse(reponse):
    """
    Verifie la reponse avant de la presenter a l'utilisateur.
    A COMPLETER : ajouter des verifications (longueur, format, mots interdits...).
    """
    # A COMPLETER
    return reponse


# --- Programme principal ---

if __name__ == "__main__":
    print("=== Projet final - [Votre titre ici] ===")
    print("Tapez 'quitter' pour arreter.")
    print()

    while True:
        entree = input("Votre question : ").strip()

        if entree.lower() == "quitter":
            print("Au revoir.")
            break

        if not entree:
            continue

        prompt = construire_prompt(entree)
        reponse = interroger_modele(prompt)
        reponse = verifier_reponse(reponse)

        print(f"\nReponse : {reponse}\n")
