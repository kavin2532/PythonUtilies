import easyocr , cv2
reader =easyocr.Reader(['en'],gpu=True)
imagefilename=r'SourceImages/IMG20240616075637.jpg'
image=cv2.imread(imagefilename)
imageread=reader.readtext(image,detail=0)
print(imageread)