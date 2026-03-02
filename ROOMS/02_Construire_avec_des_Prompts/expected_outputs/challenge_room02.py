# Challenge Room 02 — Générateur de quiz interactif en JSON
# Demande un sujet, génère un quiz via LLM, parse le JSON et affiche les questions.

import json
import re
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

from utils import creer_client, MODELE

PROMPT_PATH = os.path.join(os.path.dirname(__file__), "challenge_room02_prompt.txt")

with open(PROMPT_PATH, "r", encoding="utf-8") as f:
    PROMPT_TEMPLATE = f.read()


def extraire_json(texte: str) -> str:
    """Extrait le JSON d'une réponse qui pourrait contenir du texte autour."""
    # Tente d'abord de trouver un bloc ```json ... ```
    match = re.search(r"```json\s*(.*?)\s*```", texte, re.DOTALL)
    if match:
        return match.group(1).strip()
    match = re.search(r"\{.*\}", texte, re.DOTALL)
    if match:
        return match.group(0).strip()
    return texte.strip()


def generer_quiz(client, sujet: str, max_tentatives: int = 3) -> dict | None:
    """Envoie le prompt au LLM et retourne le quiz parsé, avec retries."""
    prompt = PROMPT_TEMPLATE.replace("{sujet}", sujet)

    for tentative in range(1, max_tentatives + 1):
        print(f"⏳ Tentative {tentative}/{max_tentatives}…")

        reponse = client.chat.completions.create(
            model=MODELE,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1500,
        )

        texte_brut = reponse.choices[0].message.content
        texte_json = extraire_json(texte_brut)

        try:
            # Contrainte json.loads
            quiz = json.loads(texte_json)
            # Vérification minimale de la structure
            if "questions" not in quiz or len(quiz["questions"]) == 0:
                raise ValueError("Pas de questions dans le JSON.")
            print("JSON valide reçu !\n")
            return quiz
        # Contrainte json invalide
        except (json.JSONDecodeError, ValueError) as e:
            print(f"Erreur de parsing (tentative {tentative}) : {e}")
            if tentative < max_tentatives:
                print("   Nouvelle tentative…\n")
    # Contrainte max tentatives atteintes
    print("Impossible d'obtenir un JSON valide après 3 tentatives.")
    return None


def afficher_quiz(quiz: dict):
    """Affiche le quiz de façon lisible avec révélation des réponses."""
    sujet = quiz.get("sujet", "Inconnu")
    questions = quiz["questions"]

    print("=" * 50)
    print(f"QUIZ — {sujet}")
    print(f"{len(questions)} questions")
    print("=" * 50)

    for q in questions:
        numero = q["numero"]
        question = q["question"]
        options = q["options"]
        bonne_reponse = q["bonne_reponse"]

        print(f"Question {numero}")
        print(f"   {question}\n")

        for option in options:
            print(f"   {option}")

        # Pause — l'utilisateur appuie sur Entrée pour voir la réponse
        input("Appuyez sur Entrée pour voir la réponse…")
        print(f"Bonne réponse : {bonne_reponse}\n")
        print("-" * 40)

    print("\n🎉 Quiz terminé !")


# ── Programme principal ───────────────────────────────────────────────
def main():
    client = creer_client()

    sujet = input("Entrez un sujet pour le quiz : ").strip()
    if not sujet:
        print("Erreur : veuillez entrer un sujet.")
        sys.exit(1)

    quiz = generer_quiz(client, sujet)

    if quiz is None:
        sys.exit(1)

    afficher_quiz(quiz)


if __name__ == "__main__":
    main()
