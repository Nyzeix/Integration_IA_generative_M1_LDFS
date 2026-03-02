# Solution Room 01 — Observations types et exemples de hallucinations
# Ce fichier est un corrigé de référence.

# Exemples de prompts qui provoquent des hallucinations :

PROMPTS_HALLUCINATION = [
    "Qui est l'auteur du roman 'Le Voyage des Ombres Silencieuses' publié en 1934 ?",
    "Résume les conclusions de l'article de Zhang et al. (2023) publié dans Nature sur le télétravail.",
]

# Observations types pour le tableau :
#
# Etape 1 : Le modèle répond correctement à une question factuelle simple.
#           La réponse est vérifiable sur Wikipédia.
#
# Etape 2 : Le modèle invente un auteur et un résumé pour un livre fictif.
#           C'est une hallucination : le modèle ne dit pas "je ne sais pas".
#
# Etape 3 : La formulation change légèrement la réponse. Un prompt avec
#           une contrainte ("en une seule phrase") produit une réponse plus courte.
#
# Etape 4 : A température 0, la réponse est identique à chaque exécution.
#           A température 0.9, la réponse change. Parfois légèrement, parfois beaucoup.
#
# Analyse réflexive (exemple de réponse attendue) :
# 1. Le modèle affirme des choses fausses parce qu'il ne distingue pas "savoir" et
#    "prédire". Il génère toujours la suite de texte la plus probable, même quand
#    la bonne réponse serait "je ne sais pas".
# 2. Dans un contexte médical, une hallucination pourrait conduire à un mauvais
#    diagnostic ou à un traitement inapproprié.
# 3. Toujours vérifier les informations factuelles produites par un LLM auprès
#    d'une source fiable avant de les utiliser.
