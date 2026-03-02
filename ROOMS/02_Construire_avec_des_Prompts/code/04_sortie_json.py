# Script 04 — Obtenir une sortie JSON valide depuis un LLM
# Room 02 — Construire avec des prompts

import json                    # Pour parser et valider le JSON
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

# Prompt qui demande explicitement une sortie en JSON
# La clé est d'être très précis sur la structure souhaitée
prompt = (
    "Tu es un assistant pédagogique. "
    "Génère une fiche de révision sur le sujet 'les listes en Python'. "
    "Réponds UNIQUEMENT avec un objet JSON valide, sans texte avant ni après. "
    "Utilise exactement cette structure : "
    '{"titre": "...", "niveau": "débutant", "definition": "...", '
    '"exemples": ["...", "..."], "erreurs_courantes": ["...", "..."]}'
)

print("=== Envoi du prompt au modèle ===")
print(prompt[:200] + "...")
print()

# Appel au modèle
reponse = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=0,     # Température 0 pour des sorties plus stables et prévisibles
    max_tokens=500
)

# Récupération du texte brut de la réponse
texte_brut = reponse.choices[0].message.content

print("=== Réponse brute du modèle ===")
print(texte_brut)
print()

# Tentative de parsing JSON
# json.loads() lève une exception si le texte n'est pas du JSON valide
try:
    # On essaie de convertir la chaîne de caractères en dictionnaire Python
    fiche = json.loads(texte_brut)

    # Si on arrive ici, le JSON est valide
    print("=== JSON valide — Contenu extrait ===")

    # Accès aux valeurs clé par clé
    print(f"Titre    : {fiche['titre']}")
    print(f"Niveau   : {fiche['niveau']}")
    print(f"Définition : {fiche['definition']}")
    print()

    # Affichage de la liste des exemples
    print("Exemples :")
    for exemple in fiche['exemples']:
        print(f"  - {exemple}")
    print()

    # Affichage des erreurs courantes
    print("Erreurs courantes :")
    for erreur in fiche['erreurs_courantes']:
        print(f"  - {erreur}")

except json.JSONDecodeError as e:
    # Si le modèle n'a pas retourné du JSON valide, on affiche l'erreur
    print(f"Erreur : le modèle n'a pas retourné du JSON valide.")
    print(f"Détail de l'erreur : {e}")
    print("Conseil : améliorez la contrainte de format dans le prompt.")
