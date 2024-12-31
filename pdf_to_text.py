import fitz  # PyMuPDF

def pdf_to_text(input_pdf, output_txt):
    """
    Extrait le texte d'un fichier PDF et le sauvegarde dans un fichier texte.
    :param input_pdf: Chemin du fichier PDF en entrée.
    :param output_txt: Chemin du fichier texte en sortie.
    """
    # Ouvrir le fichier PDF
    doc = fitz.open(input_pdf)
    
    # Ouvrir le fichier texte en mode écriture
    with open(output_txt, "w", encoding="utf-8") as file:
        # Parcourir chaque page du PDF
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            # Extraire le texte de la page
            text = page.get_text("text")
            # Écrire le texte dans le fichier de sortie
            file.write(text)
            file.write("\n\n")  # Ajouter un saut de ligne entre les pages

if __name__ == "__main__":
    # Exemple d'utilisation
    pdf_to_text("input.pdf", "output.txt")
    print("Extraction terminée. Le texte a été sauvegardé dans 'output.txt'.")