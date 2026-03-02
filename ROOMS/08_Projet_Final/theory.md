# Theory - Room 08 : Projet final

Cette Room ne présente pas de nouvelles notions. Elle rassemble les compétences de toutes les Rooms précédentes dans un projet intégrateur.

---

## Rappel des compétences à mobiliser

| Room | Compétence | Application dans le projet final |
|------|-----------|----------------------------------|
| 01 | Comprendre les LLMs | Savoir ce que le modèle peut et ne peut pas faire |
| 02 | Prompt engineering | Concevoir des prompts structurés pour chaque composant |
| 03 | Modèles open source | Justifier le choix du modèle utilisé |
| 04 | API | Connecter le modèle via API dans une application |
| 05 | RAG | Intégrer une base de connaissances documentaire |
| 06 | Risques | Identifier et documenter les risques du système |

---

## Conseils d'architecture

Un bon projet final suit cette structure :

```
1. Entrée : l'utilisateur fournit une question ou un document
2. Traitement : le système applique un pipeline
   a. Recherche de contexte pertinent (RAG)
   b. Construction du prompt (prompt engineering)
   c. Appel au modèle (API)
   d. Validation de la sortie
3. Sortie : réponse structurée, avec source et avertissements
```

**Erreur courante** : tout mettre dans un seul script monolithique. Séparez les composants en fonctions ou fichiers distincts (chargement, indexation, recherche, génération, affichage).

---

## Checklist avant remise

Avant de remettre votre projet, vérifiez :

- [ ] Le projet s'installe avec `pip install -r requirements.txt`
- [ ] Le projet s'exécute sans erreur sur une machine propre
- [ ] Le fichier `architecture.md` décrit clairement les composants
- [ ] Le rapport `rapport_projet_final.md` est complet
- [ ] La démonstration dans `expected_outputs/demo.txt` est réaliste
- [ ] Les risques du système sont identifiés et documentés
