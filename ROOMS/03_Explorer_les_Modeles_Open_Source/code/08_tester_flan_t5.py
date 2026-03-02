# Script 08 — Interroger Flan-T5-large via l'API Hugging Face
# Room 03 — Explorer les modèles open source

import os
import requests
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

# URL de l'API pour Flan-T5-large
# C'est un modèle instruction créé par Google, beaucoup plus petit que Mistral ou Llama 2
# 780 millions de paramètres contre 7 milliards pour les deux autres
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

# Le même prompt que pour les autres modèles
prompt = "Explique en 3 phrases simples ce qu'est une base de données relationnelle."

payload = {
    "inputs": prompt,
    "parameters": {
        "max_new_tokens": 250,
        "temperature": 0.3
    }
}

print("=== Interrogation de Flan-T5-large ===")
print(f"Prompt : {prompt}")
print("En attente de la réponse...")
print()

response = requests.post(API_URL, headers=headers, json=payload)

if response.status_code == 200:
    resultat = response.json()

    # Flan-T5 retourne le résultat dans un format légèrement différent
    # Parfois c'est une liste, parfois un objet avec "generated_text"
    if isinstance(resultat, list):
        texte_genere = resultat[0].get("generated_text", str(resultat[0]))
    else:
        texte_genere = str(resultat)

    print("=== Réponse de Flan-T5-large ===")
    print(texte_genere)
    print()
    print("Note : Flan-T5 est 10 fois plus petit que Mistral et Llama 2.")
    print("Observez la différence de longueur et de détail dans la réponse.")
elif response.status_code == 503:
    print("Le modèle est en cours de chargement. Réessayez dans 30 secondes.")
else:
    print(f"Erreur {response.status_code} : {response.text}")
