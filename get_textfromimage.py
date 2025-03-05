# import the following libraries 
# will convert the image to text string 
import pytesseract	 

# adds image processing capabilities 
from PIL import Image	 

# converts the text to speech 
import pyttsx3		 

#translates into the mentioned language 
from googletrans import Translator	 
import os
imagefile=r'D:\PythonPrograms\SourceImages'
for files in os.listdir(imagefile):
    # opening an image from the source path  "D:\PythonPrograms\SourceImages\IMG20240616075637.jpg"
    img = Image.open(os.path.join(imagefile,files))	 

    # describes image format in the output 
    # print(img)						 
    # path where the tesseract module is installed 
    pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # converts the image to result and saves it into result variable 
    result = pytesseract.image_to_string(img) 
    # write text in a text file and save it to source path 
    with open('abc.txt',mode ='a+') as file:	 
                    file.write("\n*********************************************\n")
                    file.write(result)
                    file.write("\n*********************************************\n") 
                    print(result) 
				
# p = Translator()					 
# translates the text into german language 
# k = p.translate(result,dest='eng')	 
# print(k) 
# engine = pyttsx3.init() 

# # an audio will be played which speaks the test if pyttsx3 recognizes it 
# engine.say(k)							 
# engine.runAndWait() 
