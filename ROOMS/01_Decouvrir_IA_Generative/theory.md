# Theory — Room 01 : Découvrir l'IA générative

## Problème concret de départ

Vous demandez à un logiciel : "Qui a écrit le roman *Les Fleurs du Mal* ?" et il vous répond avec assurance : "Ce roman a été écrit par Victor Hugo en 1857."

C'est faux. C'est Charles Baudelaire. Pourtant le logiciel semble convaincu.

Pourquoi un programme peut-il affirmer quelque chose de faux avec autant de confiance ?
Cette Room répond à cette question en vous expliquant comment fonctionnent les LLMs.

---

## Notion 1 — Le modèle de langage (LLM)

**Définition** : un LLM (Large Language Model, ou grand modèle de langage) est un programme informatique entraîné sur des quantités massives de textes pour apprendre à prédire quel mot (ou suite de mots) vient ensuite dans une phrase.

**Exemple** : si on lui donne "Le soleil se lève à l'", le modèle calcule que la suite la plus probable est "est". Il ne "comprend" pas le sens de la phrase : il a simplement vu des millions de fois cette construction dans ses données d'entraînement et sait qu'elle est souvent suivie d'un point cardinal.

**Ce qu'il faut retenir** : un LLM est un très puissant moteur de complétion de texte. Il ne raisonne pas comme un humain. Il prédit.

---

## Notion 2 — Le token

**Définition** : un token est la plus petite unité de texte que le modèle traite. Ce n'est pas toujours un mot entier. Cela peut être une syllabe, un mot, ou même une ponctuation.

**Exemple** :
- Le mot "chatbot" peut être découpé en : `["chat", "bot"]`
- Le mot "anticonstitutionnellement" peut donner : `["anti", "const", "itu", "tion", "nellement"]`
- La phrase "Je code." donne environ : `["Je", " code", "."]`

**Pourquoi c'est important** : les modèles ont une limite de tokens qu'ils peuvent traiter à la fois (appelée fenêtre de contexte). Si un texte est trop long, le modèle ne peut pas tout lire. Aussi, le coût d'utilisation d'un LLM via une API est souvent calculé en nombre de tokens.

**Ordre de grandeur** : 1 000 tokens représentent environ 750 mots en français.

---

## Notion 3 — La prédiction vs la compréhension

**Définition** : prédire, c'est calculer quelle suite de mots est la plus probable d'après des exemples vus précédemment. Comprendre, c'est saisir le sens réel d'une phrase, ses implications logiques, ses contradictions.

**Exemple** :
Demandez à un LLM : "Si une bougie rouge est plus grande qu'une bougie bleue, et que la bleue est plus grande que la verte, quelle est la plus grande ?"

Un humain comprend la relation logique et répond "rouge" instantanément.
Un LLM donne souvent la bonne réponse sur des cas simples, mais peut échouer sur des cas plus complexes ou inhabituels car il n'a pas de raisonnement logique : il produit la suite de texte qu'il juge la plus probable.

**Ce qu'il faut retenir** : ne confondez pas une réponse plausible avec une réponse vraie.

---

## Notion 4 — L'hallucination

**Définition** : on parle d'hallucination quand un LLM génère un texte qui semble vrai et est présenté avec confiance, mais qui est factuellement incorrect.

**Exemple** :
- Question : "Qui a écrit le roman *Le Seigneur des Ombres* publié en 1972 ?"
- Réponse du modèle : "Ce roman a été écrit par Jean-Michel Dupont, un auteur français reconnu pour ses oeuvres fantastiques."
- Réalité : ce roman n'existe pas. L'auteur non plus. Le modèle a inventé une réponse plausible.

**Pourquoi ça arrive** : le modèle ne sait pas qu'il ne sait pas. Il ne distingue pas "je connais la réponse" de "je dois produire une réponse". Il génère toujours quelque chose de plausible, même quand la bonne réponse serait "je ne sais pas".

**Conséquence pratique** : ne jamais utiliser un LLM comme source de référence sans vérification humaine.

---

## Notion 5 — La température

**Définition** : la température est un paramètre numérique (entre 0 et 1 en général) qui contrôle le degré de variabilité des réponses du modèle.

**Exemple** :
- Température 0 : le modèle choisit toujours le token le plus probable. Les réponses sont déterministes (toujours identiques pour le même prompt).
- Température 0.9 : le modèle introduit de la variabilité. Il peut choisir des tokens moins probables. Les réponses sont plus créatives mais potentiellement moins précises.

**Quand utiliser quelle température** :
- Tâches de précision (extraction de données, code, calculs) → température basse (0 à 0.3)
- Tâches créatives (écriture, brainstorming) → température haute (0.7 à 1.0)

---

## Résumé visuel

```
Texte d'entrée (prompt)
        |
        v
[Découpage en tokens]
        |
        v
[Calcul des probabilités pour le token suivant]
        |
        v
[Sélection selon la température]
        |
        v
Texte de sortie (réponse)
```

Le modèle répète cette boucle token par token jusqu'à produire une réponse complète.
Il n'a pas accès à des faits vérifiés en temps réel. Il utilise uniquement ce qu'il a appris pendant son entraînement.
