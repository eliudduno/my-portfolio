from PyPDF4 import PdfFileMerger
import os 
var = os.getcwd() #For extracting from enother folder
merger = PdfFileMerger()

for items in os.listdir(var):
    if items.endswith('.pdf'):
        merger.append(items)
merger.write("Archivo_final.pdf")
merger.close()

# Deleteing original files
for items in os.listdir(var):
    if items != ( 'Archivo_final.pdf') and items.endswith('.pdf'):
        os.remove(items)