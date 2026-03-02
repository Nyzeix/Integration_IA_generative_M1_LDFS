# Challenge — Room 04

## Objectif

Ajouter un historique de conversation à votre assistant local pour qu'il se souvienne des échanges précédents.

## Défi

Modifiez `code/11_mini_api_fastapi.py` et `code/12_client_local.py` pour que :

1. Le serveur maintienne une liste de messages (historique de la conversation).
2. A chaque nouvelle question, les messages précédents sont envoyés au LLM avec la nouvelle question.
3. Le client affiche l'historique complet après chaque réponse.
4. L'historique est limité aux 10 derniers échanges pour ne pas dépasser la fenêtre de contexte.

## Consignes techniques

- L'historique est stocké en mémoire côté serveur (pas besoin de base de données).
- Chaque message dans l'historique doit avoir un rôle ("user" ou "assistant") et un contenu.
- Ajoutez un point d'accès `/historique` qui retourne la liste des messages échangés.
- Ajoutez un point d'accès `/reset` qui vide l'historique.

## Livrable

- Les fichiers `11_mini_api_fastapi.py` et `12_client_local.py` modifiés.
- Un fichier `challenge_room04.txt` dans `expected_outputs/` montrant une session de 3 échanges consécutifs où le modèle se souvient du contexte.
