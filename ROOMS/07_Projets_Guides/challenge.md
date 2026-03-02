# Challenge — Room 07

## Objectif

Enrichir l'un des 3 projets avec une fonctionnalité avancée.

## Options (choisissez-en une)

### Option A — Assistant mémoire avec résumé automatique

Au lieu de supprimer les anciens messages quand l'historique dépasse 10 échanges, demandez au LLM de résumer les 5 premiers échanges en un seul message. Injectez ce résumé au début de l'historique pour conserver la mémoire longue.

### Option B — Assistant entreprise multi-documents

Modifiez l'assistant entreprise pour qu'il indexe plusieurs fichiers (texte_entreprise.txt et un fichier de votre choix). L'assistant doit être capable de citer non seulement le passage mais aussi le document source.

### Option C — Analyse de texte avec scoring de confiance

Ajoutez au JSON de sortie un champ "confiance" (entre 0 et 1) pour chaque extraction. Demandez au modèle d'estimer sa propre confiance. Analysez : l'auto-évaluation du modèle est-elle corrélée à la qualité réelle de l'extraction ?

## Livrable

Le code modifié et un fichier `challenge_room07.txt` dans `expected_outputs/` documentant votre extension et les résultats obtenus.
