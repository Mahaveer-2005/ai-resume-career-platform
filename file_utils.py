from docx import Document
from reportlab.platypus import SimpleDocTemplate, Paragraph

def create_docx(text):
    doc = Document()
    doc.add_paragraph(text)
    doc.save("resume.docx")

def create_pdf(text):
    pdf = SimpleDocTemplate("resume.pdf")
    pdf.build([Paragraph(text)])
