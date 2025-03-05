import fitz
pdffilename=r'D:\PythonPrograms\Input\Invoice_425561.pdf'
doc=fitz.open(pdffilename)
page=doc[0]
print(page.get_text("dict",sort=False))
for ii in range(len(doc)):
    # print(ii)
    page=doc[ii]
    all_info1=page.get_text("dict",sort=False)
    if len(all_info1['blocks'])>0:
        print("Search PDF")
    else:
        print("image PDF")