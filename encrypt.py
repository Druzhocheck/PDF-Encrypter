from PyPDF2 import PdfWriter, PdfReader 
from getpass import getpass
from pathlib import Path

pdfwriter = PdfWriter()
dir = input("Input fill directory to PDF file: ")
pdf = PdfReader(dir)
name = Path(dir).stem

for page in range(len(pdf.pages)):
    pdfwriter.add_page(pdf.pages[page])

password = getpass(prompt='Input password: ')
pdfwriter.encrypt(password)

with open('protected ' + name + '.pdf', 'wb') as file:
    pdfwriter.write(file)