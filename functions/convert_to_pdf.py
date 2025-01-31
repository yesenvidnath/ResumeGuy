import pdfkit

def convert_df_to_pdf(df, output_pdf="resume.pdf"):
    """ Converts a Pandas DataFrame into a PDF file """
    html = df.to_html(index=False, border=1)
    with open("resume.html", "w") as f:
        f.write(html)
    pdfkit.from_file("resume.html", output_pdf)
