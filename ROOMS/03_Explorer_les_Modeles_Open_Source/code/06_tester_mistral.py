# Script 06 — Interroger Mistral-7B-Instruct via l'API Hugging Face
# Room 03 — Explorer les modèles open source

import os
import requests
from dotenv import load_dotenv

# Chargement du token Hugging Face depuis .env
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

# URL de l'API d'inférence pour Mistral-7B-Instruct
# C'est un modèle instruction créé par Mistral AI (entreprise française)
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

# En-têtes HTTP : on envoie le token pour s'authentifier
headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

# Le prompt à envoyer — utilisez le même prompt pour les 3 modèles
prompt = "Explique en 3 phrases simples ce qu'est une base de données relationnelle."

# Construction du payload (les données envoyées au serveur)
# "inputs" contient le texte du prompt
# "parameters" permet de configurer la génération
payload = {
    "inputs": prompt,
    "parameters": {
        "max_new_tokens": 250,       # Limite la longueur de la réponse
        "temperature": 0.3,          # Réponse stable et précise
        "return_full_text": False    # Ne retourne que la réponse, pas le prompt
    }
}

print("=== Interrogation de Mistral-7B-Instruct ===")
print(f"Prompt : {prompt}")
print("En attente de la réponse...")
print()

# Envoi de la requête POST à l'API Hugging Face
# requests.post envoie les données et attend la réponse du serveur
response = requests.post(API_URL, headers=headers, json=payload)

# Vérification du code de statut HTTP
if response.status_code == 200:
    # La réponse est une liste JSON contenant un objet avec le texte généré
    resultat = response.json()

    # Extraction du texte généré
    texte_genere = resultat[0]["generated_text"]

    print("=== Réponse de Mistral-7B-Instruct ===")
    print(texte_genere)
elif response.status_code == 503:
    # Le modèle est en cours de chargement sur le serveur
    print("Le modèle est en cours de chargement. Réessayez dans 30 secondes.")
else:
    # Autre erreur
    print(f"Erreur {response.status_code} : {response.text}")
