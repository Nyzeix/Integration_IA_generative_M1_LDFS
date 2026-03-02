# Room 05 — Créer un système RAG

## Objectif

Construire un système RAG (Retrieval-Augmented Generation) complet qui permet de poser des questions sur vos propres documents. A la fin de cette Room, vous saurez charger un PDF, l'indexer dans une base vectorielle et obtenir des réponses contextualisées avec citation de la source.

## Résultat attendu

- Un texte extrait d'un PDF affiché dans le terminal
- Un index vectoriel créé et interrogeable
- Une réponse générée à partir du contenu de votre document (et non des connaissances générales du modèle)
- Une comparaison entre réponse RAG et réponse directe

## Fichiers de cette Room

| Fichier | Contenu |
|---------|---------|
| `theory.md` | Limites du LLM, embeddings, similarité, base vectorielle, architecture RAG |
| `practice.md` | 6 étapes guidées pour construire un pipeline RAG complet |
| `challenge.md` | Adapter le RAG pour un fichier texte personnel |
| `rubric.md` | Critères d'évaluation |
| `code/13_charger_pdf.py` | Extraire le texte d'un PDF |
| `code/14_decouper_texte.py` | Découper le texte en segments |
| `code/15_creer_embeddings.py` | Vectoriser et stocker dans ChromaDB |
| `code/16_recherche_vectorielle.py` | Rechercher les segments les plus pertinents |
| `code/17_rag_complet.py` | Pipeline RAG complet : question → recherche → réponse |
| `expected_outputs/comparaison_rag_vs_direct.txt` | Gabarit de comparaison |
