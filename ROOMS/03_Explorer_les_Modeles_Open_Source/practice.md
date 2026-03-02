# Practice - Room 03 : Explorer les modèles open source

## Objectif

Interroger trois modèles open source avec le même prompt et comparer objectivement leurs réponses.

---

## Etape 1 - Configurer l'accès Hugging Face

Vérifiez que votre fichier `.env` contient votre token Hugging Face :

```
HF_TOKEN=hf_votre_token_ici
```

Testez l'accès :

```bash
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('Token OK' if os.getenv('HF_TOKEN') else 'Token manquant')"
```

---

## Etape 2 - Interroger Mistral-7B-Instruct

Ouvrez et lisez `code/06_tester_mistral.py`.

Exécutez-le :

```bash
python code/06_tester_mistral.py
```

Le script envoie un prompt à Mistral-7B-Instruct via l'API Hugging Face et affiche la réponse. Copiez la réponse obtenue dans `expected_outputs/tableau_comparaison_modeles.md` à la ligne Mistral.

Si le modèle prend du temps à répondre la première fois, c'est normal : le serveur charge le modèle en mémoire.

---

## Etape 3 - Interroger Llama 2

Ouvrez et lisez `code/07_tester_llama2.py`.

Exécutez-le :

```bash
python code/07_tester_llama2.py
```

Copiez la réponse dans le tableau comparatif.

---

## Etape 4 - Interroger Flan-T5

Ouvrez et lisez `code/08_tester_flan_t5.py`.

Exécutez-le :

```bash
python code/08_tester_flan_t5.py
```

Copiez la réponse dans le tableau comparatif. Notez que Flan-T5 est un modèle beaucoup plus petit : la réponse sera probablement plus courte et plus directe.

---

## Etape 5 - Remplir le tableau comparatif

Ouvrez `expected_outputs/tableau_comparaison_modeles.md`. Pour chaque modèle, évaluez :

- **Qualité** : la réponse est-elle correcte, pertinente et bien formulée ?
- **Longueur** : combien de mots/phrases la réponse contient-elle ?
- **Cohérence** : la réponse est-elle logique et bien structurée du début à la fin ?
- **Rapidité** : combien de secondes avant d'obtenir la réponse ? (estimez)

---

## Etape 6 - Analyse critique

Rédigez une analyse de 5 lignes minimum dans `expected_outputs/tableau_comparaison_modeles.md` (section "Analyse") qui répond à ces questions :

- Quel modèle a produit la meilleure réponse pour ce prompt précis ?
- La taille du modèle a-t-elle un impact visible sur la qualité ?
- Si vous deviez construire un assistant pédagogique, lequel choisiriez-vous et pourquoi ?

---

## Vérification finale

- [ ] Les 3 scripts exécutés sans erreur
- [ ] Les 3 réponses copiées dans le tableau comparatif
- [ ] Tableau rempli avec les 4 critères pour chaque modèle
- [ ] Analyse critique de 5 lignes rédigée
