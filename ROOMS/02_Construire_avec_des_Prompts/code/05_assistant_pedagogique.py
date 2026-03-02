# Script 05 — Assistant pédagogique interactif
# Room 02 — Construire avec des prompts
# Complétez les parties marquées "# A COMPLETER"

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


def expliquer_sujet(sujet):
    """
    Envoie un sujet au LLM avec un rôle de professeur bienveillant
    et retourne une explication adaptée à un débutant.
    """
    # A COMPLETER : construisez le prompt structuré
    # Il doit contenir :
    #   - Un rôle (professeur bienveillant pour étudiants sans base IA)
    #   - Le sujet à expliquer
    #   - Une contrainte de format (3 paragraphes : définition, analogie, exemple)
    #   - Une contrainte de longueur (maximum 150 mots)
    prompt_explication = (
        # A COMPLETER
        f"Explique le sujet suivant : {sujet}"  # Version basique à améliorer
    )

    reponse = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt_explication}],
        temperature=0.3,
        max_tokens=300
    )
    return reponse.choices[0].message.content


def proposer_exercice(sujet):
    """
    Propose un exercice pratique sur le sujet donné.
    """
    # A COMPLETER : construisez un prompt qui demande au modèle de créer
    # un exercice pratique simple (1 seule question avec un exemple de code
    # si c'est un sujet de programmation) sur le sujet fourni.
    prompt_exercice = (
        # A COMPLETER
        f"Propose un exercice sur le sujet suivant : {sujet}"  # Version basique à améliorer
    )

    reponse = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt_exercice}],
        temperature=0.5,
        max_tokens=200
    )
    return reponse.choices[0].message.content


# --- Programme principal ---
print("=== Assistant pédagogique ===")
print("Entrez un sujet pour obtenir une explication et un exercice.")
print("Tapez 'quitter' pour arrêter.")
print()

while True:
    # Demande du sujet à l'utilisateur
    sujet = input("Sujet à apprendre : ").strip()

    # Condition de sortie
    if sujet.lower() == "quitter":
        print("Au revoir !")
        break

    # Vérification que le sujet n'est pas vide
    if not sujet:
        print("Veuillez entrer un sujet.")
        continue

    # Affichage de l'explication
    print("\n--- Explication ---")
    explication = expliquer_sujet(sujet)
    print(explication)

    # Affichage de l'exercice
    print("\n--- Exercice ---")
    exercice = proposer_exercice(sujet)
    print(exercice)

    print("\n" + "-"*50 + "\n")
