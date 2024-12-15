from pptx import Presentation
from PyPDF2 import PdfFileWriter, PdfFileReader

def ppt_to_pdf(ppt_file, pdf_file):
    prs = Presentation(ppt_file)
    pdf_writer = PdfFileWriter()
    for slide in prs.slides:
        pdf_writer.addPage(slide.pdf_page)
    with open(pdf_file, 'wb') as f:
        pdf_writer.write(f)
        
ppt_file = 'example.pptx'
pdf_file = 'example.pdf'
ppt_to_pdf(ppt_file, pdf_file)