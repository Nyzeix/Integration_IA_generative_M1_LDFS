# Theory — Room 04 : Connecter une API

## Problème concret de départ

Vous savez envoyer un prompt depuis un script Python. Mais que se passe-t-il entre votre script et le modèle ? Comment votre question voyage-t-elle sur internet ? Et si le serveur refuse votre requête, ou si vous dépassez le budget ? Cette Room explique ce mécanisme invisible.

---

## Notion 1 — L'API

**Définition** : une API (Application Programming Interface) est un ensemble de règles qui permet à deux programmes de communiquer entre eux. Quand votre script Python envoie un prompt à un LLM hébergé chez OpenAI, il utilise l'API d'OpenAI.

**Analogie** : imaginez un restaurant. Vous (le client) ne parlez pas directement au cuisinier (le modèle). Vous passez par le serveur (l'API) qui prend votre commande (le prompt), la transmet au cuisinier, et vous ramène le plat (la réponse).

**Exemple concret** :
```
Votre script Python  →  requête HTTP  →  serveur OpenAI  →  modèle GPT  →  réponse  →  votre script
```

---

## Notion 2 — La requête HTTP

**Définition** : une requête HTTP est un message standardisé envoyé par votre programme à un serveur distant. Elle contient une adresse (URL), une méthode (GET pour demander, POST pour envoyer), des en-têtes (comme votre clé d'authentification) et un corps (les données, ici le prompt).

**Exemple en Python avec la bibliothèque `requests`** :
```python
import requests

response = requests.post(
    "https://api.openai.com/v1/chat/completions",   # adresse du serveur
    headers={"Authorization": "Bearer sk-..."},       # authentification
    json={"model": "gpt-3.5-turbo", "messages": [...]}  # données envoyées
)
```

**Ce qu'il faut retenir** : chaque appel à un LLM via API est en réalité une requête HTTP POST.

---

## Notion 3 — La clé d'API

**Définition** : une clé d'API est une chaîne de caractères secrète qui identifie votre compte auprès du serveur. Sans cette clé, le serveur refuse votre requête.

**Exemple** : `sk-abc123xyz456...` pour OpenAI, `hf_abc123...` pour Hugging Face.

**Règle de sécurité fondamentale** : ne jamais écrire votre clé directement dans le code source. Utilisez un fichier `.env` (non versionné dans Git) et la bibliothèque `python-dotenv` pour la charger.

```python
from dotenv import load_dotenv
import os

load_dotenv()
cle = os.getenv("OPENAI_API_KEY")
```

---

## Notion 4 — La gestion des erreurs

**Définition** : quand vous envoyez une requête à une API, le serveur répond avec un code de statut qui indique si tout s'est bien passé ou s'il y a eu un problème.

**Codes les plus fréquents** :

| Code | Signification | Action à prendre |
|------|---------------|-----------------|
| 200 | Succès | Traiter la réponse normalement |
| 401 | Clé API invalide ou manquante | Vérifier le fichier `.env` |
| 429 | Trop de requêtes en peu de temps | Attendre puis réessayer |
| 500 | Erreur interne du serveur | Réessayer plus tard |
| 503 | Service indisponible (modèle en chargement) | Attendre 30 secondes |

**Exemple de gestion en Python** :
```python
if response.status_code == 200:
    print(response.json())
elif response.status_code == 429:
    print("Trop de requêtes. Attendez quelques secondes.")
elif response.status_code == 401:
    print("Clé API invalide. Vérifiez votre fichier .env.")
else:
    print(f"Erreur inattendue : {response.status_code}")
```

---

## Notion 5 — Le coût d'utilisation

**Définition** : les API de LLM facturent à l'usage, proportionnellement au nombre de tokens traités (prompt + réponse).

**Ordre de grandeur** (indicatif, les prix varient) :
- 1 000 tokens environ 750 mots
- GPT-3.5-turbo : environ 0.002 USD / 1 000 tokens
- GPT-4 : environ 0.06 USD / 1 000 tokens (30 fois plus cher)

**Pourquoi c'est important** : un script mal conçu qui envoie des requêtes en boucle peut générer des coûts importants. Toujours estimer le coût avant d'exécuter un traitement en masse.

**Bonne pratique** : utiliser la bibliothèque `tiktoken` pour compter les tokens avant l'envoi.

---

## Notion 6 — FastAPI

**Définition** : FastAPI est un framework Python qui permet de créer un serveur web (une API) en quelques lignes de code. Vous pouvez l'utiliser pour exposer votre propre service qui, en interne, interroge un LLM.

**Exemple minimal** :
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/bonjour")
def dire_bonjour():
    return {"message": "Bonjour depuis FastAPI"}
```

On lance le serveur avec :
```bash
uvicorn nom_du_fichier:app --reload
```

Le serveur écoute sur `http://127.0.0.1:8000` et répond aux requêtes.

**Pourquoi c'est utile** : vous pouvez construire un assistant local que d'autres programmes ou utilisateurs interrogent via HTTP, tout en gardant la clé API protégée côté serveur.
