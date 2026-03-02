# Challenge — Room 01

## Objectif

Aller plus loin en construisant un protocole personnel pour détecter les hallucinations d'un LLM.

## Défi

Trouvez 2 prompts différents qui font systématiquement halluciner le modèle (c'est-à-dire qu'à chaque exécution, le modèle produit une réponse fausse ou inventée).

Pour chaque prompt :
1. Notez le prompt exact utilisé.
2. Copiez la réponse obtenue.
3. Vérifiez la réponse par une source externe fiable (Wikipédia, base de données officielle).
4. Expliquez en 2-3 phrases pourquoi ce type de question piège particulièrement le modèle.

## Livrable

Un fichier texte `challenge_room01.txt` dans `expected_outputs/` contenant vos 2 prompts, les réponses obtenues, la vérification et l'explication.

## Piste de réflexion

Les catégories de questions qui hallucinent le plus souvent sont :
- Les questions sur des événements très récents (après la date de coupure du modèle)
- Les questions sur des personnes peu connues
- Les questions qui demandent des statistiques précises ou des dates exactes
- Les questions sur des oeuvres fictives
