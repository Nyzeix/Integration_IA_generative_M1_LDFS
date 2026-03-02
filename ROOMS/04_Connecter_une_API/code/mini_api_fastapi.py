# Script 11 — Mini serveur FastAPI qui interroge un LLM (avec historique)
# Room 04 — Connecter une API
# Lancer avec : uvicorn ROOMS.04_Connecter_une_API.code.11_mini_api_fastapi:app --reload --port 8000

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from utils import creer_client, MODELE

client = creer_client()

# Création de l'application FastAPI
app = FastAPI(title="Mini Assistant LLM", version="2.0")

# --- Historique de conversation (en mémoire) ---
# Chaque élément est un dict {"role": "user"|"assistant", "content": "..."}
MAX_HISTORIQUE = 10  # Limite aux 10 derniers échanges
historique: list[dict] = []


class QuestionRequest(BaseModel):
    question: str


class MessageSchema(BaseModel):
    role: str
    content: str


class ReponseResult(BaseModel):
    question: str
    reponse: str
    tokens_utilises: int
    historique: List[MessageSchema]


@app.post("/question", response_model=ReponseResult)
def poser_question(req: QuestionRequest):
    """Reçoit une question, l'envoie au LLM avec l'historique et retourne la réponse."""

    # Ajouter la question de l'utilisateur à l'historique
    historique.append({"role": "user", "content": req.question})

    completion = client.chat.completions.create(
        model=MODELE,
        messages = [
            {"role": "system", "content": "Tu es un assistant concis et pédagogique."}
        ] + historique
        temperature=0.3,
        max_tokens=300
    )

    reponse_texte = completion.choices[0].message.content
    tokens = completion.usage.total_tokens if completion.usage else 0

    # Ajouter la réponse de l'assistant à l'historique
    historique.append({"role": "assistant", "content": reponse_texte})

    # Limiter l'historique aux MAX_HISTORIQUE derniers échanges (paires user+assistant)
    while len(historique) > MAX_HISTORIQUE * 2:
        historique.pop(0)

    return ReponseResult(
        question=req.question,
        reponse=reponse_texte,
        tokens_utilises=tokens,
        historique=[MessageSchema(**m) for m in historique]
    )


@app.get("/historique")
def obtenir_historique():
    """Retourne la liste des messages échangés."""
    return {"historique": historique, "nombre_messages": len(historique)}


@app.post("/reset")
def reinitialiser_historique():
    """Vide l'historique de conversation."""
    historique.clear()
    return {"statut": "ok", "message": "Historique réinitialisé."}


@app.get("/sante")
def verifier_sante():
    """Retourne un message simple pour verifier que le serveur est operationnel."""
    return {"statut": "ok", "message": "Le serveur fonctionne correctement."}
