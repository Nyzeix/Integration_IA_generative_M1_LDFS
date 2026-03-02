# Room 03 - Explorer les modèles open source

## Objectif

Découvrir la plateforme Hugging Face et comparer trois modèles de langage open source sur une même tâche. A la fin de cette Room, vous saurez distinguer un modèle de base d'un modèle instruction, évaluer l'impact de la taille d'un modèle et choisir un modèle adapté à un besoin.

## Résultat attendu

- Trois réponses produites par trois modèles différents à partir du même prompt
- Un tableau comparatif rempli (qualité, longueur, cohérence)
- Une analyse critique argumentée de 5 lignes

## Fichiers de cette Room

| Fichier | Contenu |
|---------|---------|
| `theory.md` | Modèle de base, modèle instruction, taille, Hugging Face, inférence |
| `practice.md` | 6 étapes guidées de comparaison |
| `challenge.md` | Comparaison sur une tâche de résumé |
| `rubric.md` | Critères d'évaluation |
| `code/06_tester_mistral.py` | Interroger Mistral-7B-Instruct via Hugging Face |
| `code/07_tester_llama2.py` | Interroger Llama 2 via Hugging Face |
| `code/08_tester_flan_t5.py` | Interroger Flan-T5 via Hugging Face |
| `expected_outputs/tableau_comparaison_modeles.md` | Gabarit de tableau |

## Avant de commencer

Créez un compte Hugging Face (https://huggingface.co) et générez un token d'accès. Ajoutez-le dans votre fichier `.env` :

```
HF_TOKEN=votre_token_huggingface
```
