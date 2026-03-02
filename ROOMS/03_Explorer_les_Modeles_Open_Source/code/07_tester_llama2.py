# Script 07 - Interroger Llama 2 via l'API Hugging Face
# Room 03 - Explorer les modèles open source

import os
import requests
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

# URL de l'API pour Llama 2 7B Chat
# C'est un modèle instruction créé par Meta (Facebook)
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

# Le même prompt que pour Mistral - la comparaison doit être équitable
prompt = "Explique en 3 phrases simples ce qu'est une base de données relationnelle."

payload = {
    "inputs": prompt,
    "parameters": {
        "max_new_tokens": 250,
        "temperature": 0.3,
        "return_full_text": False
    }
}

print("=== Interrogation de Llama 2 7B Chat ===")
print(f"Prompt : {prompt}")
print("En attente de la réponse...")
print()

response = requests.post(API_URL, headers=headers, json=payload)

if response.status_code == 200:
    resultat = response.json()
    texte_genere = resultat[0]["generated_text"]
    print("=== Réponse de Llama 2 7B Chat ===")
    print(texte_genere)
elif response.status_code == 503:
    print("Le modèle est en cours de chargement. Réessayez dans 30 secondes.")
else:
    print(f"Erreur {response.status_code} : {response.text}")
