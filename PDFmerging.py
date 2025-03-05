from pypdf import PdfWriter
pdfs=[r'',r'']
merger=PdfWriter()
for pdf in pdfs:
    merger.append(pdf)
merger.write(r'')
merger.close()