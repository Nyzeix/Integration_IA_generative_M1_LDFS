# Datasets

Ce dossier contient les fichiers de données utilisés dans les exercices.

| Fichier | Utilisé dans | Description |
|---------|-------------|-------------|
| `texte_entreprise.txt` | Room 03, 05, 07 | Document fictif sur la stratégie de TechVision SAS |
| `rapport_fictif.pdf` | Room 05 | Version PDF du document d'entreprise |
| `articles_presse.txt` | Room 06, 07 | 3 articles de presse fictifs (banque, cybersécurité, villes intelligentes) |

## Générer le PDF

Si le fichier `rapport_fictif.pdf` est absent ou corrompu, vous pouvez le régénérer :

```bash
cd datasets
python generer_pdf.py
```
