# Challenge - Room 05

## Objectif

Adapter le pipeline RAG pour traiter un fichier texte fourni par l'utilisateur via la ligne de commande.

## Défi

Créez un script `challenge_room05.py` qui :

1. Accepte en argument le chemin vers un fichier `.txt` : `python challenge_room05.py mon_fichier.txt`
2. Charge et découpe le fichier en segments
3. Crée les embeddings et les stocke dans ChromaDB
4. Lance une boucle interactive : l'utilisateur pose des questions et reçoit des réponses contextualisées
5. A chaque réponse, le script affiche aussi les passages sources utilisés

## Contraintes

- Le script doit fonctionner avec n'importe quel fichier `.txt` (pas seulement le PDF fourni).
- Si le fichier n'existe pas, un message d'erreur clair est affiché.
- L'utilisateur peut taper "quitter" pour arrêter la boucle.

## Livrable

- Le script `challenge_room05.py` dans `code/`
- Un fichier `challenge_room05_session.txt` dans `expected_outputs/` montrant une session de 3 questions-réponses avec un fichier de votre choix
