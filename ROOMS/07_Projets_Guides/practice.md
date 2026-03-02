# Practice - Room 07 : Projets guidés

Réalisez les 3 projets dans l'ordre. Chaque projet suit la même démarche : lire l'architecture, compléter le code, tester et documenter.

---

## Projet A - Assistant mémoire

### Consignes

1. Lisez l'architecture dans `code/projet_a/architecture.md`.
2. Ouvrez `code/projet_a/assistant_memoire.py`. Les fonctions à compléter sont marquées `# A COMPLETER`.
3. Complétez la fonction `ajouter_au_contexte()` : elle doit ajouter un nouveau message à l'historique et limiter l'historique aux 10 derniers échanges.
4. Complétez la fonction `envoyer_message()` : elle doit envoyer l'historique complet au LLM et retourner la réponse.
5. Testez l'assistant sur 5 échanges consécutifs. Vérifiez que l'assistant se souvient du contexte (par exemple, posez une question, puis une question de suivi qui nécessite le contexte précédent).
6. Documentez dans `expected_outputs/projet_a_observations.txt` :
   - Les 5 échanges (questions et réponses)
   - Les limites observées (le modèle perd-il le contexte ? à quel moment ?)
   - Le coût approximatif en tokens de la session complète

---

## Projet B - Assistant entreprise

### Consignes

1. Lisez l'architecture dans `code/projet_b/architecture.md`.
2. Indexez `datasets/texte_entreprise.txt` en utilisant le pipeline RAG de la Room 05.
3. Ouvrez `code/projet_b/assistant_entreprise.py`. Complétez les fonctions marquées `# A COMPLETER`.
4. L'assistant doit :
   - Recevoir une question
   - Chercher les passages pertinents dans l'index
   - Générer une réponse contextualisée
   - Afficher le passage source utilisé
5. Testez avec 5 questions pertinentes (dont la réponse est dans le document) et 2 questions hors sujet (dont la réponse n'est pas dans le document).
6. Documentez dans `expected_outputs/projet_b_observations.txt` :
   - Les 7 échanges (questions, réponses, sources citées)
   - Le comportement sur les questions hors sujet
   - Votre analyse : le système est-il fiable ?

---

## Projet C - Assistant analyse de texte

### Consignes

1. Lisez l'architecture dans `code/projet_c/architecture.md`.
2. Ouvrez `code/projet_c/analyser_texte.py`. Complétez les fonctions marquées `# A COMPLETER`.
3. L'assistant doit, pour chaque texte fourni :
   - Extraire le sentiment (positif, négatif, neutre)
   - Extraire les 5 mots-clés principaux
   - Produire un résumé en 2 phrases
   - Retourner le tout en JSON valide
4. Traitez les 3 articles de `datasets/articles_presse.txt` et sauvegardez les résultats JSON dans `expected_outputs/resultats_analyse.json`.
5. Vérifiez que tous les JSON sont valides avec `json.loads()`.
6. Rédigez une analyse critique dans `expected_outputs/projet_c_analyse.txt` :
   - Cas où la sortie JSON était incorrecte (si cela s'est produit)
   - Causes possibles
   - Comment vous avez corrigé le prompt ou le code

---

## Vérification finale

- [ ] Projet A : assistant mémoire fonctionnel, 5 échanges documentés
- [ ] Projet B : assistant entreprise fonctionnel, 7 échanges documentés
- [ ] Projet C : 3 articles analysés, résultats JSON valides, analyse critique
