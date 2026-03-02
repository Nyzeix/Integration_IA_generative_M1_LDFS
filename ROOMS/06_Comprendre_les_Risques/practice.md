# Practice - Room 06 : Comprendre les risques

## Objectif

Détecter concrètement les hallucinations et les biais d'un LLM, analyser une étude de cas et rédiger des bonnes pratiques.

---

## Etape 1 - Détecter des hallucinations

Ouvrez et lisez `code/18_detecter_hallucination.py`. Ce script pose 5 questions factuelles au modèle, dont 2 portent sur des sujets fictifs.

```bash
python code/18_detecter_hallucination.py
```

Pour chaque réponse, remplissez `expected_outputs/grille_verification_faits.txt` :
- La réponse est-elle correcte ?
- Comment l'avez-vous vérifié (source citée) ?

---

## Etape 2 - Vérifier les faits

Pour les 5 réponses obtenues, effectuez une vérification externe :
- Utilisez Wikipédia, un moteur de recherche ou une source officielle
- Notez la source utilisée pour chaque vérification
- Indiquez si la réponse est : vraie, fausse, partiellement vraie ou non vérifiable

Remplissez toutes les lignes de `expected_outputs/grille_verification_faits.txt`.

---

## Etape 3 - Tester les biais

Ouvrez et lisez `code/19_tester_biais.py`. Ce script envoie des prompts avec des contextes neutres et des contextes stéréotypés, puis compare les réponses.

```bash
python code/19_tester_biais.py
```

Notez les différences de réponse dans `expected_outputs/analyse_biais.txt` :
- Le modèle utilise-t-il des pronoms différents selon le contexte ?
- Les descriptions sont-elles influencées par des stéréotypes ?

---

## Etape 4 - Identifier des biais dans un texte

Ouvrez `datasets/articles_presse.txt`. Lisez les articles et identifiez 2 passages où un LLM pourrait produire un biais s'il utilisait ce texte comme source.

Consignez vos observations dans `expected_outputs/analyse_biais.txt` :
- Le passage original
- Le biais potentiel
- Une reformulation neutre

---

## Etape 5 - Analyser l'étude de cas

Relisez la section "Etude de cas" dans `theory.md` et répondez aux 3 questions posées. Rédigez vos réponses en phrases complètes (pas en mots-clés) dans un fichier `expected_outputs/etude_de_cas_reponses.txt`.

---

## Etape 6 - Bonnes pratiques

Rédigez une liste de 5 règles de bonne pratique pour utiliser un LLM en contexte professionnel. Chaque règle doit tenir en une phrase et être suivie d'une justification d'une ligne.

Enregistrez dans `expected_outputs/bonnes_pratiques.txt`.

---

## Vérification finale

- [ ] Script 18 exécuté, 5 réponses obtenues
- [ ] Grille de vérification remplie avec sources
- [ ] Script 19 exécuté, biais identifiés
- [ ] 2 passages biaisés identifiés dans les articles
- [ ] Étude de cas analysée, 3 questions répondues
- [ ] 5 bonnes pratiques rédigées avec justification
