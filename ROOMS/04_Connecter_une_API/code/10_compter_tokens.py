# Script 10 - Compter les tokens d'un prompt avant l'envoi
# Room 04 - Connecter une API
#
# Note : tiktoken est l'encodeur d'OpenAI. Si vous utilisez Groq ou Ollama
# avec des modeles Llama, le decompte sera approximatif (les encodeurs different
# legerement). L'ordre de grandeur reste correct pour estimer les couts.

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

from utils import FOURNISSEUR, MODELE

# On tente d'utiliser tiktoken si disponible, sinon on approxime
try:
    import tiktoken
    encodeur = tiktoken.encoding_for_model("gpt-3.5-turbo")
    MODE_COMPTAGE = "tiktoken"
except Exception:
    encodeur = None
    MODE_COMPTAGE = "approximation"

# Le prompt dont on veut connaitre la taille en tokens
prompt = (
    "Tu es un professeur universitaire specialise en intelligence artificielle. "
    "Explique a un etudiant debutant ce qu'est le machine learning "
    "en utilisant uniquement des exemples du quotidien. "
    "Limite ta reponse a 100 mots."
)

print("=== Comptage de tokens ===")
print(f"Fournisseur actif : {FOURNISSEUR}")
print(f"Modele actif      : {MODELE}")
print(f"Mode de comptage  : {MODE_COMPTAGE}")
print()
print(f"Texte du prompt :")
print(f"  {prompt}")
print()
print(f"Nombre de caracteres : {len(prompt)}")

if encodeur:
    # Encodage precis avec tiktoken
    tokens = encodeur.encode(prompt)
    print(f"Nombre de tokens     : {len(tokens)} (tiktoken, encodeur OpenAI)")
    print()

    # Visualisation des tokens (les 10 premiers)
    print("=== Detail des tokens (10 premiers) ===")
    for i, token_id in enumerate(tokens[:10]):
        texte_token = encodeur.decode([token_id])
        print(f"  Token {i+1:2d} : id={token_id:6d}  texte='{texte_token}'")
    print(f"  ... ({len(tokens) - 10} tokens restants)")
    nb_tokens = len(tokens)
else:
    # Approximation : 1 token ~ 0.75 mot en francais
    nb_mots = len(prompt.split())
    nb_tokens = int(nb_mots / 0.75)
    print(f"Nombre de tokens     : ~{nb_tokens} (approximation : 1 token ~ 0.75 mot)")

print()

# Estimation du cout
if "groq" in FOURNISSEUR.lower() or "ollama" in FOURNISSEUR.lower():
    print("=== Estimation du cout ===")
    print(f"Cout du prompt : 0.000000 USD (API gratuite)")
else:
    prix_par_1k = 0.002
    cout = (nb_tokens / 1000) * prix_par_1k
    print("=== Estimation du cout ===")
    print(f"Cout du prompt seul : {cout:.6f} USD")
    print(f"(sans compter les tokens de la reponse)")

print()
print("Exercice : modifiez le prompt dans ce script et relancez pour voir l'impact.")
