# Script 11 — Mini serveur FastAPI qui interroge un LLM
# Room 04 — Connecter une API
# Lancer avec : uvicorn code.11_mini_api_fastapi:app --reload --port 8000

from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

# Création du client OpenAI
client = OpenAI()

# Création de l'application FastAPI
app = FastAPI(title="Mini Assistant LLM", version="1.0")


# Modèle de données pour la requête entrante
# pydantic.BaseModel valide automatiquement les données reçues
class QuestionRequest(BaseModel):
    question: str


# Modèle de données pour la réponse
class ReponseResult(BaseModel):
    question: str
    reponse: str
    tokens_utilises: int


# Point d'accès principal : recevoir une question et retourner la réponse du LLM
@app.post("/question", response_model=ReponseResult)
def poser_question(req: QuestionRequest):
    """
    Reçoit une question, l'envoie au LLM et retourne la réponse.
    """
    # Appel au modèle OpenAI
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Tu es un assistant concis et pédagogique."},
            {"role": "user", "content": req.question}
        ],
        temperature=0.3,
        max_tokens=300
    )

    # Construction de la réponse
    return ReponseResult(
        question=req.question,
        reponse=completion.choices[0].message.content,
        tokens_utilises=completion.usage.total_tokens
    )


# Point d'accès de test : vérifier que le serveur fonctionne
@app.get("/sante")
def verifier_sante():
    """Retourne un message simple pour vérifier que le serveur est opérationnel."""
    return {"statut": "ok", "message": "Le serveur fonctionne correctement."}
