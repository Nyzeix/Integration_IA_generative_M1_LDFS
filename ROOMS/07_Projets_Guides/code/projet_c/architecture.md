# Architecture - Projet C : Assistant analyse de texte

## Description

Un assistant qui analyse des articles de presse en extrayant pour chacun : le sentiment, les mots-clés et un résumé. Les résultats sont produits en JSON valide et sauvegardés.

## Composants

```
Fichier articles_presse.txt
    |
    | lecture et séparation des articles
    v
analyser_texte.py
    |
    | pour chaque article :
    |   1. Construit un prompt d'analyse structuré
    |   2. Demande au LLM une sortie JSON
    |   3. Valide le JSON avec json.loads()
    |
    v
Fichier resultats_analyse.json (sauvegarde des résultats)
```

## Format JSON attendu pour chaque article

```json
{
  "article_numero": 1,
  "sentiment": "positif",
  "mots_cles": ["innovation", "technologie", "emploi", "croissance", "investissement"],
  "resume": "L'article traite de ... en deux phrases maximum."
}
```

## Contraintes

- Le JSON doit être parseable sans erreur par `json.loads()`.
- Si le modèle retourne un JSON invalide, le script doit réessayer (maximum 3 tentatives).
- Les 3 analyses sont sauvegardées dans un seul fichier JSON (liste de 3 objets).
