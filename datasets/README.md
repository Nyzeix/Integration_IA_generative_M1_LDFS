# Datasets

Ce dossier contient les fichiers de donnees utilises dans les exercices.

| Fichier | Utilise dans | Description |
|---------|-------------|-------------|
| `texte_entreprise.txt` | Room 03, 05, 07 | Document fictif sur la strategie de TechVision SAS |
| `rapport_fictif.pdf` | Room 05 | Version PDF du document d'entreprise |
| `articles_presse.txt` | Room 06, 07 | 3 articles de presse fictifs (banque, cybersecurite, villes intelligentes) |

## Regenerer le PDF

Si le fichier `rapport_fictif.pdf` est absent ou corrompu, vous pouvez le regenerer :

```bash
python scripts/generer_pdf.py
```
