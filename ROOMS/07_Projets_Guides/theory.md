# Theory — Room 07 : Projets guidés

Cette Room ne présente pas de nouvelles notions. Elle mobilise les compétences acquises dans les Rooms 1 à 6. Voici un récapitulatif des notions clés nécessaires pour les 3 projets.

---

## Récapitulatif pour le Projet A — Assistant mémoire

**Notions mobilisées** :
- **Historique de conversation** : le LLM n'a pas de mémoire entre les appels. Pour simuler une conversation continue, on renvoie les messages précédents à chaque nouvelle requête.
- **Gestion du contexte** : la liste des messages envoyés ne doit pas dépasser la fenêtre de contexte du modèle. Il faut donc limiter l'historique (par exemple aux 10 derniers échanges).
- **Rôle système** : le message "system" définit le comportement global de l'assistant pendant toute la conversation.

**Rappel pratique** :
```python
messages = [
    {"role": "system", "content": "Tu es un assistant pédagogique."},
    {"role": "user", "content": "Bonjour, explique-moi les variables."},
    {"role": "assistant", "content": "Une variable est..."},
    {"role": "user", "content": "Donne-moi un exemple."}
]
```

---

## Récapitulatif pour le Projet B — Assistant entreprise

**Notions mobilisées** :
- **Architecture RAG** : charger un document, le découper, le vectoriser, chercher les passages pertinents et générer une réponse contextualisée.
- **Citation des sources** : le prompt RAG demande au modèle d'indiquer quel passage du document il utilise.
- **Gestion des questions hors sujet** : quand la question ne concerne pas le document, le modèle doit répondre qu'il ne dispose pas de l'information.

---

## Récapitulatif pour le Projet C — Assistant analyse de texte

**Notions mobilisées** :
- **Prompt structuré avec sortie JSON** : demander au modèle de produire un JSON avec des clés prédéfinies (sentiment, mots-clés, résumé).
- **Traitement par lots** : appliquer le même traitement à plusieurs textes successivement.
- **Validation de la sortie** : vérifier que le JSON retourné est valide et contient les clés attendues.
