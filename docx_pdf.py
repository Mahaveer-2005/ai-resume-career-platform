from docx import Document
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_docx(text):
    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)
    doc.save("resume.docx")

def create_pdf(text):
    styles = getSampleStyleSheet()
    pdf = SimpleDocTemplate("resume.pdf")
    story = []
    for line in text.split("\n"):
        story.append(Paragraph(line, styles["Normal"]))
    pdf.build(story)
