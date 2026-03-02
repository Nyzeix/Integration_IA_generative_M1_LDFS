"""Script utilitaire pour générer rapport_fictif.pdf à partir de texte_entreprise.txt"""
import os

try:
    import fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF requis. Installez avec : pip install PyMuPDF")
    exit(1)

chemin_dir = os.path.dirname(os.path.abspath(__file__))
chemin_txt = os.path.join(chemin_dir, "texte_entreprise.txt")
chemin_pdf = os.path.join(chemin_dir, "rapport_fictif.pdf")

with open(chemin_txt, "r", encoding="utf-8") as f:
    texte = f.read()

doc = fitz.open()
paragraphes = texte.split("\n\n")
y = 72
page = doc.new_page()

for para in paragraphes:
    para = para.strip()
    if not para:
        continue
    if para.startswith("Section") or para.startswith("Document"):
        fontsize = 14
        fontname = "helv"
        y += 10
    else:
        fontsize = 11
        fontname = "helv"

    rect = fitz.Rect(72, y, 523, y + 400)
    rc = page.insert_textbox(rect, para, fontsize=fontsize, fontname=fontname)
    lines_used = para.count('\n') + len(para) // 60 + 2
    y += lines_used * (fontsize + 4)

    if y > 750:
        page = doc.new_page()
        y = 72

doc.save(chemin_pdf)
doc.close()
print(f"PDF généré : {chemin_pdf}")
