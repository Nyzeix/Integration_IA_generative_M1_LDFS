# Script 12 — Client Python qui interroge le serveur FastAPI local (avec historique)
# Room 04 — Connecter une API
# Prérequis : le serveur 11_mini_api_fastapi.py doit tourner sur le port 8000

import requests

URL_SERVEUR = "http://127.0.0.1:8000"

# Vérification que le serveur est opérationnel
print("=== Vérification du serveur ===")
try:
    r = requests.get(f"{URL_SERVEUR}/sante", timeout=10)
    if r.status_code == 200:
        print(f"Serveur OK : {r.json()['message']}")
    else:
        print(f"Le serveur a répondu avec le code {r.status_code}")
except requests.ConnectionError:
    print("Impossible de se connecter au serveur.")
    print("Assurez-vous que le serveur est lancé avec :")
    print("  python -m uvicorn code.mini_api_fastapi:app --reload --port 8000")
    exit(1)
except requests.Timeout:
    print("Le serveur met trop de temps a repondre (timeout).")
    print("Verifiez que FastAPI est bien demarre et disponible sur le port 8000.")
    exit(1)

print()


def afficher_historique(historique: list[dict]):
    """Affiche l'historique de conversation de manière lisible."""
    if not historique:
        print("  (aucun message)")
        return
    for i, msg in enumerate(historique, 1):
        role = "Vous" if msg["role"] == "user" else "Assistant"
        contenu = msg["content"][:100] + "..." if len(msg["content"]) > 100 else msg["content"]
        print(f"  {i}. [{role}] {contenu}")


# Boucle interactive : l'utilisateur pose des questions
print("=== Client interactif (avec historique) ===")
print("Commandes spéciales :")
print("  'historique' — Afficher l'historique complet")
print("  'reset'      — Réinitialiser la conversation")
print("  'quitter'    — Quitter le client")
print()

while True:
    question = input("Votre question : ").strip()

    if question.lower() == "quitter":
        print("Au revoir.")
        break

    if not question:
        print("Veuillez entrer une question.")
        continue

    # Commande : afficher l'historique
    if question.lower() == "historique":
        try:
            r = requests.get(f"{URL_SERVEUR}/historique")
            if r.status_code == 200:
                data = r.json()
                print(f"\n=== Historique ({data['nombre_messages']} messages) ===")
                afficher_historique(data["historique"])
            else:
                print(f"Erreur : {r.status_code}")
        except requests.ConnectionError:
            print("Connexion perdue avec le serveur.")
        print()
        continue

    # Commande : réinitialiser l'historique
    if question.lower() == "reset":
        try:
            r = requests.post(f"{URL_SERVEUR}/reset")
            if r.status_code == 200:
                print(f"\n{r.json()['message']}")
            else:
                print(f"Erreur : {r.status_code}")
        except requests.ConnectionError:
            print("Connexion perdue avec le serveur.")
        print()
        continue

    # Envoi requete
    try:
        r = requests.post(
            f"{URL_SERVEUR}/question",
            json={"question": question},
            timeout=30
        )

        if r.status_code == 200:
            data = r.json()
            print(f"\nRéponse : {data['reponse']}")
            print(f"Tokens utilisés : {data['tokens_utilises']}")

            # Afficher l'historique complet après chaque réponse
            print(f"\n--- Historique ({len(data['historique'])} messages) ---")
            afficher_historique(data["historique"])
        else:
            print(f"Erreur du serveur : {r.status_code}")

    except requests.ConnectionError:
        print("Connexion perdue avec le serveur.")
    except requests.Timeout:
        print("Le serveur ne repond pas a temps. Reessayez dans quelques secondes.")

    print()
