# Solution Room 01 - Observations types et exemples de hallucinations
# Ce fichier est un corrige de reference executable.

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from utils import creer_client, MODELE

client = creer_client()

# Exemples de prompts qui provoquent des hallucinations
PROMPTS_HALLUCINATION = [
    "Qui est l'auteur du roman 'Le Voyage des Ombres Silencieuses' publie en 1934 ?",
    "Resume les conclusions de l'article de Zhang et al. (2023) publie dans Nature sur le teletravail.",
]

# Prompt factuel pour comparaison
PROMPT_FACTUEL = "Qui a ecrit le recueil de poemes Les Fleurs du Mal ?"


def tester_prompt(prompt, etiquette):
    """Teste un prompt et affiche la reponse."""
    print(f"\n--- {etiquette} ---")
    print(f"Q : {prompt}")

    reponse = client.chat.completions.create(
        model=MODELE,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=200
    )

    texte = reponse.choices[0].message.content
    print(f"R : {texte}")
    return texte


if __name__ == "__main__":
    print("=== Solution Room 01 - Test de hallucinations ===")

    tester_prompt(PROMPT_FACTUEL, "Question factuelle (reponse attendue : Baudelaire)")

    for i, prompt in enumerate(PROMPTS_HALLUCINATION, 1):
        tester_prompt(prompt, f"Hallucination {i} (sujet fictif)")

    print("\n=== Observations types ===")
    print("1. Le modele repond avec confiance meme sur des sujets fictifs.")
    print("2. Il invente des auteurs, des dates, des conclusions d'etudes.")
    print("3. Il ne dit pas 'je ne sais pas' spontanement.")
    print("4. Regle : toujours verifier les faits generes par un LLM.")
