from PyPDF2 import PdfWriter, PdfReader
import getpass

pdfwritter = PdfWriter()
pdf = PdfReader("Registro.pdf")

for page_num in range(len(pdf.pages)):
    pdfwritter.add_page(pdf.pages[page_num])
passw = getpass.getpass(prompt='Ingrese la contraseña: ')
pdfwritter.encrypt(passw)

with open('newfile_lock.pdf','wb') as f:
    pdfwritter.write(f)