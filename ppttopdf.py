import subprocess

def ppt_to_pdf(ppt_file, pdf_file):
    subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', ppt_file, '--outdir', pdf_file])

ppt_file = 'example.pptx'
pdf_file = 'example.pdf'
ppt_to_pdf(ppt_file, pdf_file)