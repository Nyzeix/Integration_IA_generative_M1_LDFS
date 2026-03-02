# Script 10 — Compter les tokens d'un prompt avant l'envoi
# Room 04 — Connecter une API

import tiktoken

# tiktoken est la bibliothèque officielle d'OpenAI pour compter les tokens
# Chaque modèle utilise un encodeur différent
# Pour GPT-3.5-turbo et GPT-4, l'encodeur s'appelle "cl100k_base"
encodeur = tiktoken.encoding_for_model("gpt-3.5-turbo")

# Le prompt dont on veut connaître la taille en tokens
prompt = (
    "Tu es un professeur universitaire spécialisé en intelligence artificielle. "
    "Explique à un étudiant débutant ce qu'est le machine learning "
    "en utilisant uniquement des exemples du quotidien. "
    "Limite ta réponse à 100 mots."
)

# Encodage : conversion du texte en liste de tokens (nombres entiers)
tokens = encodeur.encode(prompt)

# Affichage du résultat
print("=== Comptage de tokens ===")
print(f"Texte du prompt :")
print(f"  {prompt}")
print()
print(f"Nombre de caractères : {len(prompt)}")
print(f"Nombre de tokens     : {len(tokens)}")
print()

# Visualisation des tokens (les 10 premiers)
print("=== Détail des tokens (10 premiers) ===")
for i, token_id in enumerate(tokens[:10]):
    # decode convertit un token (nombre) en texte lisible
    texte_token = encodeur.decode([token_id])
    print(f"  Token {i+1:2d} : id={token_id:6d}  texte='{texte_token}'")

print(f"  ... ({len(tokens) - 10} tokens restants)")
print()

# Estimation du coût
prix_par_1k_tokens = 0.002  # prix indicatif GPT-3.5-turbo en USD
cout_prompt = (len(tokens) / 1000) * prix_par_1k_tokens
print(f"=== Estimation du coût ===")
print(f"Coût du prompt seul : {cout_prompt:.6f} USD")
print(f"(sans compter les tokens de la réponse)")
print()

# Expérience : modifiez le prompt ci-dessus pour un texte plus long
# et observez comment le nombre de tokens évolue
print("Exercice : modifiez le prompt dans ce script et relancez pour voir l'impact sur le nombre de tokens.")
