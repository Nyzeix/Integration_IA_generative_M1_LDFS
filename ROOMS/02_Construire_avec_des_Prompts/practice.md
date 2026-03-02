# Practice — Room 02 : Construire avec des prompts

## Objectif

Transformer des prompts vagues en prompts structurés, obtenir des sorties JSON valides et construire un assistant pédagogique simple.

---

## Etape 1 — Identifier les défauts d'un prompt vague

Ouvrez le fichier `code/prompts_exercices.txt`. Il contient 3 prompts vagues.

Pour chacun, sans exécuter de code, répondez par écrit :
- Qu'est-ce qui manque dans ce prompt ?
- Quelles informations supplémentaires le modèle aurait besoin ?
- Réécrivez ce prompt en ajoutant un rôle, un contexte, une tâche et une contrainte de format.

Enregistrez vos réécriture dans un fichier `mon_prompt_v1.txt` dans le dossier `expected_outputs/`.

---

## Etape 2 — Tester le prompt avant et après amélioration

Ouvrez `code/03_tester_prompt_structure.py`. Lisez-le entièrement.

Remplacez dans le script :
- `PROMPT_VAGUE` : collez l'un des prompts originaux de `prompts_exercices.txt`
- `PROMPT_STRUCTURE` : collez votre version améliorée depuis `mon_prompt_v1.txt`

Exécutez le script :

```bash
python code/03_tester_prompt_structure.py
```

Vous verrez les deux réponses affichées côte à côte.

Copiez les deux réponses dans `expected_outputs/comparaison_prompts.txt` et répondez à la question : laquelle est plus utile et pourquoi ?

---

## Etape 3 — Obtenir une réponse en JSON

Ouvrez `code/04_sortie_json.py` et lisez-le.

Exécutez-le :

```bash
python code/04_sortie_json.py
```

Le script envoie un prompt qui demande une fiche de révision en JSON, puis il vérifie que la réponse est bien du JSON valide en utilisant `json.loads()`.

Vous devez voir s'afficher dans le terminal :
- La réponse brute du modèle
- Le message "JSON valide" ou une erreur si le format n'est pas respecté
- Les valeurs extraites clé par clé

**Ce que vous observez** : le modèle peut ne pas toujours renvoyer du JSON parfaitement valide. Observez les cas d'échec si cela se produit.

---

## Etape 4 — Modifier le prompt JSON

Dans `code/04_sortie_json.py`, modifiez le prompt pour obtenir une fiche de révision sur un autre sujet de votre choix (par exemple : "les types de données Python", "les méthodes HTTP", "les bases du réseau").

Assurez-vous que le JSON retourné est valide. Si ce n'est pas le cas, modifiez la contrainte de format dans le prompt pour aider le modèle.

Notez dans `expected_outputs/comparaison_prompts.txt` ce qui a fonctionné et ce qui a échoué.

---

## Etape 5 — Construire un assistant pédagogique

Ouvrez `code/05_assistant_pedagogique.py`. Le squelette du script est fourni avec des commentaires indiquant ce que vous devez compléter.

L'assistant doit :
- Demander à l'utilisateur un sujet à apprendre
- Envoyer ce sujet au LLM avec un rôle de professeur bienveillant
- Afficher une explication adaptée débutant
- Proposer ensuite un exercice pratique sur ce sujet

Complétez les parties marquées `# A COMPLETER` dans le script.

Testez l'assistant avec au moins 2 sujets différents.

---

## Etape 6 — Bilan

Dans `expected_outputs/comparaison_prompts.txt`, ajoutez une section "Bilan" où vous répondez à ces 3 questions en 2-3 phrases chacune :

1. Quelle est la différence la plus importante entre votre prompt vague et votre prompt structuré ?
2. Dans quel cas demanderiez-vous une sortie JSON plutôt qu'une réponse en texte libre ?
3. Comment le rôle donné au modèle a-t-il changé la qualité des réponses ?

---

## Vérification finale

- [ ] Prompts vagues analysés et réécrits dans `mon_prompt_v1.txt`
- [ ] Script `03_tester_prompt_structure.py` exécuté avec les deux versions
- [ ] Script `04_sortie_json.py` exécuté et JSON validé
- [ ] Assistant pédagogique `05_assistant_pedagogique.py` complété et testé
- [ ] Fichier `comparaison_prompts.txt` rempli avec observations et bilan
