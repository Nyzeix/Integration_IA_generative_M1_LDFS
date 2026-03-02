# Script 09 — Appel API simple avec affichage de la réponse et des métadonnées
# Room 04 — Connecter une API

from openai import OpenAI
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

# Création du client OpenAI
client = OpenAI()

# Le prompt à envoyer
prompt = "Donne trois conseils pratiques pour bien organiser un projet Python."

print("=== Envoi du prompt à l'API ===")
print(f"Prompt : {prompt}")
print()

# Envoi de la requête à l'API
# On utilise chat.completions.create pour les modèles de type chat
reponse = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Tu es un développeur Python expérimenté."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.3,
    max_tokens=300
)

# Affichage de la réponse
print("=== Réponse du modèle ===")
print(reponse.choices[0].message.content)
print()

# Affichage des métadonnées
print("=== Métadonnées ===")
print(f"Modèle utilisé          : {reponse.model}")
print(f"Tokens (prompt)         : {reponse.usage.prompt_tokens}")
print(f"Tokens (réponse)        : {reponse.usage.completion_tokens}")
print(f"Tokens (total)          : {reponse.usage.total_tokens}")

# Estimation du coût (indicatif, prix GPT-3.5-turbo)
cout_estime = reponse.usage.total_tokens * 0.000002
print(f"Coût estimé             : {cout_estime:.6f} USD")
