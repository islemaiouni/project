from fpdf import FPDF

def text_to_pdf(input_txt, output_pdf):
    """
    Convertit un fichier texte en fichier PDF.
    :param input_txt: Chemin du fichier texte en entrée.
    :param output_pdf: Chemin du fichier PDF en sortie.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(input_txt, "r", encoding="utf-8") as file:
        for line in file:
            pdf.cell(200, 10, txt=line.strip(), ln=True)

    pdf.output(output_pdf)

if __name__ == "__main__":
    # Exemple d'utilisation
    text_to_pdf("input.txt", "output.pdf")
    print("Conversion terminée. Le fichier PDF a été sauvegardé sous 'output.pdf'.")