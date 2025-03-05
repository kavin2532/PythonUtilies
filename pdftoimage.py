from pdf2image import convert_from_path
import shutil,os
inputfilepath=r''
popplerpath=r'C:\Python\poppler-0.68.0\bin'
for pdffile in os.listdir(inputfilepath):
    if pdffile.endswith(".pdf"):
        pdftopngconvert=convert_from_path(os.path.join(inputfilepath,pdffile),popplerpath=popplerpath)
        for ii in range(len(pdftopngconvert)):
            pass