# Practice - Room 05 : Créer un système RAG

## Objectif

Construire un pipeline RAG complet : charger un document, le découper, le vectoriser, l'indexer et poser des questions dont les réponses sont extraites du document.

---

## Etape 1 - Charger un PDF

Ouvrez et lisez `code/13_charger_pdf.py`. Ce script utilise PyMuPDF pour extraire le texte d'un fichier PDF.

```bash
python code/13_charger_pdf.py
```

Vous devez voir le texte brut du document `datasets/rapport_fictif.pdf` affiché dans le terminal. Vérifiez que le texte est lisible et qu'il correspond au contenu du PDF.

---

## Etape 2 - Découper le texte en segments

Ouvrez et lisez `code/14_decouper_texte.py`. Ce script découpe le texte extrait en segments de 300 mots avec un chevauchement de 50 mots entre les segments.

```bash
python code/14_decouper_texte.py
```

Vous devez voir s'afficher : le nombre total de segments créés et les 3 premiers segments. Le chevauchement permet d'éviter qu'une information soit coupée en plein milieu.

---

## Etape 3 - Créer les embeddings et les stocker

Ouvrez et lisez `code/15_creer_embeddings.py`. Ce script vectorise chaque segment avec le modèle `all-MiniLM-L6-v2` de sentence-transformers et les stocke dans une collection ChromaDB.

```bash
python code/15_creer_embeddings.py
```

Vous devez voir : le nombre de segments indexés et un exemple de vecteur (les 10 premiers nombres) pour visualiser ce à quoi ressemble un embedding.

---

## Etape 4 - Rechercher les segments pertinents

Ouvrez et lisez `code/16_recherche_vectorielle.py`. Ce script pose une question, la convertit en vecteur et cherche les 3 segments les plus proches dans la base.

```bash
python code/16_recherche_vectorielle.py
```

Vous devez voir : la question posée, les 3 segments trouvés et leur score de similarité. Vérifiez que les segments affichés sont bien en rapport avec la question.

---

## Etape 5 - Pipeline RAG complet

Ouvrez et lisez `code/17_rag_complet.py`. Ce script combine toutes les étapes précédentes : il prend une question, cherche les passages pertinents et les envoie au LLM comme contexte pour générer une réponse.

```bash
python code/17_rag_complet.py
```

Vous devez voir : la question, les passages trouvés, et la réponse du LLM qui s'appuie sur ces passages. Le LLM doit citer la source de l'information.

---

## Etape 6 - Comparer RAG vs réponse directe

Posez la même question de deux façons :
1. Via le pipeline RAG (script 17)
2. Directement au LLM sans contexte (utilisez le script 01 de la Room 01 avec la même question)

Copiez les deux réponses dans `expected_outputs/comparaison_rag_vs_direct.txt` et répondez :
- La réponse RAG est-elle plus précise ?
- La réponse directe contient-elle des informations inventées ?
- Dans quel cas utiliseriez-vous le RAG plutôt qu'un appel direct ?

---

## Vérification finale

- [ ] PDF chargé et texte affiché
- [ ] Texte découpé en segments
- [ ] Embeddings créés et stockés dans ChromaDB
- [ ] Recherche vectorielle fonctionnelle, segments pertinents trouvés
- [ ] Pipeline RAG complet : question → recherche → réponse contextualisée
- [ ] Comparaison RAG vs direct remplie
