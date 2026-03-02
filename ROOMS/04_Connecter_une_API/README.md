# Room 04 - Connecter une API

## Objectif

Comprendre ce qu'est une API, envoyer des requêtes Python à un LLM distant, gérer les erreurs et les coûts, et construire votre propre mini-service avec FastAPI.

## Résultat attendu

- Un script Python qui interroge un LLM et affiche réponse et métadonnées
- Une estimation du coût en tokens avant l'envoi
- Un mini-serveur FastAPI fonctionnel interrogeable depuis un client Python local
- Un schéma du flux client-serveur-LLM documenté

## Fichiers de cette Room

| Fichier | Contenu |
|---------|---------|
| `theory.md` | API, requête HTTP, clé API, gestion d'erreurs, coût, FastAPI |
| `practice.md` | 6 étapes guidées |
| `challenge.md` | Ajouter un historique de conversation |
| `rubric.md` | Critères d'évaluation |
| `code/09_appel_api_simple.py` | Appel API avec affichage complet |
| `code/10_compter_tokens.py` | Estimation du coût avant envoi |
| `code/mini_api_fastapi.py` | Mini serveur FastAPI |
| `code/12_client_local.py` | Client qui interroge le serveur local |
| `expected_outputs/schema_flux.txt` | Gabarit de schéma du flux |
