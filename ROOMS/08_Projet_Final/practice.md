# Practice — Room 08 : Projet final

## Consignes

---

## Etape 1 — Choisir un cas d'usage

Sélectionnez l'un des cas proposés dans `README.md` ou proposez le vôtre (soumis à validation de l'enseignant). Le cas doit intégrer au minimum :
- Du prompt engineering (prompts structurés)
- Une connexion API à un LLM
- Un composant RAG (base documentaire interrogeable)
- Une analyse des risques

---

## Etape 2 — Rédiger la fiche d'architecture

Créez un fichier `code/architecture.md` qui décrit sur 1 page maximum :
- Les entrées du système (quelles données l'utilisateur fournit)
- Les composants principaux (RAG, API, prompt)
- Les sorties (ce que l'utilisateur obtient)
- Les risques identifiés (hallucination, biais, données sensibles)
- Un schéma en texte du flux de données

---

## Etape 3 — Implémenter les scripts

Créez dans `code/` les scripts nécessaires. Votre projet doit contenir au minimum :
- Un script principal exécutable (point d'entrée)
- Un script de chargement/indexation des données
- Un fichier `requirements.txt` listant les dépendances spécifiques au projet

Chaque script doit être commenté de façon à ce qu'un autre étudiant puisse comprendre le code.

---

## Etape 4 — Produire une démonstration

Exécutez votre projet et enregistrez une session complète dans `expected_outputs/demo.txt`. La session doit montrer :
- Le démarrage du système
- Au moins 3 interactions différentes
- Au moins 1 cas où le système gère correctement une question hors sujet ou un cas limite

---

## Etape 5 — Rédiger le rapport

Remplissez le modèle `templates/rapport_projet_final.md` (copiez-le dans votre dossier `code/`). Le rapport doit contenir :
- Description du cas d'usage choisi
- Architecture du système
- Choix techniques justifiés (modèle, base vectorielle, format de sortie)
- Analyse des risques du système (au moins 3 risques identifiés avec mesures de mitigation)
- Limites connues et pistes d'amélioration

---

## Etape 6 — Vérifier la checklist

Avant remise, passez en revue la checklist de `theory.md`. Assurez-vous que chaque point est satisfait.

---

## Livrable final

Remettez un dossier contenant :

```
code/
  architecture.md
  [vos scripts Python]
  requirements.txt
expected_outputs/
  demo.txt
rapport_projet_final.md
```
