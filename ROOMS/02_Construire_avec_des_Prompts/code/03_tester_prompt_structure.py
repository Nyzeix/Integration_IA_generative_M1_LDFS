# Script 03 — Comparer un prompt vague et un prompt structuré
# Room 02 — Construire avec des prompts

from openai import OpenAI
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

# Création du client
client = OpenAI()

# --- A MODIFIER ---
# Remplacez ces deux chaînes par vos propres prompts
PROMPT_VAGUE = "Parle-moi des réseaux de neurones."

PROMPT_STRUCTURE = (
    "Tu es un professeur de Master 1 en informatique. "
    "Un étudiant n'ayant aucune connaissance en IA te demande une explication. "
    "Explique ce qu'est un réseau de neurones artificiel en 3 paragraphes : "
    "1) une analogie avec le cerveau humain, "
    "2) comment il apprend, "
    "3) un exemple d'application concrète. "
    "Utilise un langage simple, sans formule mathématique."
)
# --- FIN A MODIFIER ---


def interroger(prompt_texte, etiquette):
    """Envoie un prompt et affiche la réponse avec une étiquette."""
    # Affichage de l'étiquette pour identifier quelle réponse on lit
    print(f"\n{'='*60}")
    print(f"  {etiquette}")
    print(f"{'='*60}")
    print(f"Prompt : {prompt_texte[:100]}...")  # On n'affiche que les 100 premiers caractères
    print()

    # Appel au modèle
    reponse = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt_texte}],
        temperature=0,
        max_tokens=400
    )

    # Extraction et affichage du texte de la réponse
    texte = reponse.choices[0].message.content
    print(texte)
    return texte


# Test du prompt vague
reponse_vague = interroger(PROMPT_VAGUE, "REPONSE AU PROMPT VAGUE")

# Test du prompt structuré
reponse_structuree = interroger(PROMPT_STRUCTURE, "REPONSE AU PROMPT STRUCTURE")

# Instructions pour l'étudiant
print("\n" + "="*60)
print("A faire maintenant :")
print("1. Copiez les deux réponses dans expected_outputs/comparaison_prompts.txt")
print("2. Indiquez laquelle est plus utile et expliquez pourquoi en 2-3 phrases.")
print("="*60)
