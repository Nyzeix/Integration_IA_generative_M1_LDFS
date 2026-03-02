# Theory — Room 02 : Construire avec des prompts

## Problème concret de départ

Vous demandez à un LLM : "Explique-moi Python." Il vous répond avec 500 mots sur l'histoire du langage, ses caractéristiques, ses usages, ses frameworks... mais rien sur ce que vous vouliez vraiment apprendre.

Pourquoi ? Parce que votre prompt était trop vague. La qualité de la réponse dépend directement de la qualité de la question. Cette Room vous apprend à formuler des prompts qui produisent exactement ce dont vous avez besoin.

---

## Notion 1 — Le prompt vague

**Définition** : un prompt vague est une instruction incomplète qui ne précise ni le contexte, ni la tâche exacte, ni le format attendu. Le modèle doit alors "deviner" ce que vous voulez, et sa réponse reflète cette incertitude.

**Exemple de prompt vague** :
```
Explique-moi quelque chose sur les bases de données.
```

**Ce que le modèle ne sait pas** :
- Quel niveau de détail ? (débutant ? expert ?)
- Quel aspect ? (relationnel ? NoSQL ? performance ?)
- Quel format ? (liste ? paragraphe ? code ?)
- Pour quel usage ? (cours ? projet ? entretien ?)

**Conséquence** : la réponse sera générique, souvent inutilisable directement.

---

## Notion 2 — Le prompt structuré

**Définition** : un prompt structuré est une instruction qui précise explicitement le rôle du modèle, le contexte, la tâche et le format de sortie attendu.

**Structure recommandée** :
```
[ROLE] : qui est le modèle dans cet échange ?
[CONTEXTE] : quelle est la situation ?
[TACHE] : que doit-il produire ?
[FORMAT] : sous quelle forme ?
[CONTRAINTES] : longueur, langue, ton ?
```

**Exemple de prompt structuré** correspondant au prompt vague ci-dessus :
```
Tu es un professeur universitaire qui enseigne les bases de données à des étudiants de première année en informatique.
Explique ce qu'est une base de données relationnelle en 3 paragraphes : définition, utilité, exemple concret du quotidien.
Utilise un vocabulaire accessible, sans jargon technique avancé.
```

**Résultat** : la réponse sera ciblée, au bon niveau, dans le bon format.

---

## Notion 3 — Le rôle

**Définition** : donner un rôle au modèle (via une instruction "system" ou en début de prompt) oriente son comportement, son ton et son niveau de détail.

**Exemple** :
- Sans rôle : "Explique ce qu'est une API."
  - Réponse générique, souvent trop longue ou trop courte.
- Avec rôle : "Tu es un développeur senior qui explique les APIs à un stagiaire de première semaine. Explique ce qu'est une API en 3 phrases simples, avec une analogie du quotidien."
  - Réponse adaptée, avec analogie, dans la bonne longueur.

**En pratique** : le rôle se place dans le message "system" lors de l'appel API, ou en première ligne du prompt si on n'utilise pas de message système.

---

## Notion 4 — Les contraintes de sortie

**Définition** : une contrainte de sortie est une instruction qui limite ou formate explicitement la réponse du modèle.

**Exemples de contraintes** :
- Longueur : "Réponds en moins de 50 mots."
- Format : "Réponds uniquement sous forme de liste à puces."
- Contenu : "N'utilise aucun terme technique non expliqué."
- Structure : "Commence par une définition, puis donne un exemple."
- Langue : "Réponds en français."

**Pourquoi c'est utile** : sans contrainte, le modèle choisit lui-même la structure. Avec des contraintes, vous contrôlez exactement ce que vous obtenez.

---

## Notion 5 — La sortie JSON

**Définition** : JSON (JavaScript Object Notation) est un format structuré pour représenter des données, composé de clés et de valeurs. Un programme Python peut lire ce format directement.

**Exemple** :
```json
{
  "titre": "Introduction aux bases de données",
  "niveau": "débutant",
  "concepts_cles": ["table", "colonne", "requête SQL"],
  "résumé": "Une base de données est un système organisé pour stocker et retrouver des informations."
}
```

**Pourquoi demander une sortie JSON** :
- On peut utiliser la réponse directement dans un programme Python avec `json.loads()`
- La structure est prévisible et vérifiable
- On peut automatiser le traitement de plusieurs réponses

**Comment le demander dans un prompt** :
```
Réponds uniquement en JSON valide, sans texte avant ni après.
Utilise les clés suivantes : "titre", "résumé", "concepts_cles".
```

---

## Récapitulatif : anatomie d'un bon prompt

```
[ROLE]        Tu es un formateur en cybersécurité.
[CONTEXTE]    Un étudiant vient de découvrir les attaques par injection SQL.
[TACHE]       Explique comment se défendre contre ce type d'attaque.
[FORMAT]      Utilise 3 étapes numérotées, avec un exemple de code Python pour chaque étape.
[CONTRAINTES] Niveau débutant. Maximum 200 mots. Réponse en français.
```
