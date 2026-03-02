# Projet C — Assistant analyse de texte avec sortie JSON
# Room 07 — Projets guidés

import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

# Nombre maximum de tentatives si le JSON est invalide
MAX_TENTATIVES = 3


def charger_articles(chemin):
    """
    Charge le fichier d'articles et les sépare.
    Les articles sont séparés par une ligne '---'.
    Retourne une liste de chaînes de caractères.
    """
    with open(chemin, "r", encoding="utf-8") as f:
        contenu = f.read()

    articles = [a.strip() for a in contenu.split("---") if a.strip()]
    return articles


def analyser_article(texte_article, numero):
    """
    Analyse un article en demandant au LLM d'extraire sentiment, mots-clés et résumé en JSON.

    A COMPLETER :
    - Construire un prompt qui demande au modèle d'analyser le texte
    - Exiger une sortie JSON avec les clés : article_numero, sentiment, mots_cles, resume
    - Tenter jusqu'à MAX_TENTATIVES fois si le JSON est invalide
    - Retourner le dictionnaire Python résultant, ou None si toutes les tentatives échouent
    """
    # A COMPLETER
    pass


# --- Programme principal ---

chemin_articles = os.path.join(os.path.dirname(__file__), "..", "..", "..", "datasets", "articles_presse.txt")

print("Chargement des articles...")
articles = charger_articles(chemin_articles)
print(f"{len(articles)} articles chargés.")
print()

resultats = []

for i, article in enumerate(articles, 1):
    print(f"=== Analyse de l'article {i} ===")
    print(f"Début : {article[:100]}...")

    resultat = analyser_article(article, i)

    if resultat:
        resultats.append(resultat)
        print(f"Sentiment  : {resultat.get('sentiment', 'N/A')}")
        print(f"Mots-clés  : {resultat.get('mots_cles', [])}")
        print(f"Résumé     : {resultat.get('resume', 'N/A')}")
    else:
        print("Echec de l'analyse pour cet article.")

    print()

# Sauvegarde des résultats
chemin_sortie = os.path.join(os.path.dirname(__file__), "..", "expected_outputs", "resultats_analyse.json")
with open(chemin_sortie, "w", encoding="utf-8") as f:
    json.dump(resultats, f, ensure_ascii=False, indent=2)

print(f"Résultats sauvegardés dans {chemin_sortie}")
