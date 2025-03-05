import cv2 ,csv, re ,os, shutil
from tkinter import *
from future.moves import tkinter as tk
#config_file = os.path.join (path_configfile,
#if not os.path.isfile (config file):
# AnnotationConfig.cfg')
# raise Exception('Invoice AutoEngine Path config file not found') configparser.ConfigParser()
from tkinter import filedialog
from pytesseract import pytesseract
import numpy as np
from PIL import Image, ImageTk
from numpy.linalg import norm
from tkdocviewer import *
import pandas as pd
#path = os.path.dirname ( file
#path configfile=os.path.join(path, 'cfg')
#print (path, "aaaa")
# tesseract_path
# filepath =
# Python file
#config.read(config_file)
#Output folder
#tesseract_path
# config.get('PATH', 'Output folder').replace('\n','') config.get('PATH', 'tesseract_path').replace('\n','')
Output_folder=r"D:\AnnotationToolProcess\OutputFolder"
# =
tesseract_path=r"C:\Program Files\Tesseract-OCR tesseract.exe"
pytesseract.tesseract_cmd = tesseract_path
filepath22=[]
def open_image():
    global image,orig_image , img, label1
    filepath=filedialog.askopenfilename(title="Select Image")
    img=Image.open(filepath)
    resize_image=img.resize((600,700))
    img=ImageTk.PhotoImage(resize_image)
    label1=Label(image=img)
    label1.image=img
    label1.pack()
    label1.place(x=0,y=0)
    var = StringVar()
    # annotatedlabels.clear()
    # annotatedlabelstring=str(annotatedlabels).replace(",",",\n")
    if len(filepath22)>0:
        filepath22.clear()
    try:
        label.after(1000,label.destroy)
    except:
        pass

    filepath22.append(filepath)
    image=cv2.imread(filepath)
    orig_image=image.copy()
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    text=pytesseract.image_to_string(image)
    text_box.delete(1.0,END)
    text_box.insertr(END,text)
def save_annotations_text():
    savingfile=filepath22[0].replace('.png','.csv')
    with open(savingfile,"a+",newline='') as file:
        csvfile=csv.reader(file)
        headeridenfied=NO
        for lines in csvfile:
            if lines[0]=='label':
                headeridenfied=YES
                break
        writer=csv.writer(file)
        if headeridenfied==NO:
            writer.writerow(["Label","ID", "Token", "Token _X","Token Y", "Token Width","Token Height",
                "Text", "x", "Y", "Width", "Height", "Filename", "Image Size"])
        img = Image.open(filepath22[0])
        # get width and height
        width = img.width
        height = img-height
        sizeofimage=str(width) +" & "+str (height)
        for ii in range(len(label_items)):
            print(ii)
            try:
                writer.writerow([label_items[ii], Selected_items[ii], x_coordinates[ii], y_coordinate[ii] ,
                                 width_coordinates[ii], height_coordinates[ii] ,filepath22[0] ,sizeofimage])
            except:
                writer.writerow([label_items[ii], Selected_items[ii], x_coordinates1[ii], y_coordinate1[ii] ,
                                 width_coordinates1[ii], height_coordinates1[ii] ,filepath22[0] ,sizeofimage])
        img.close()
        labelledfilename=filepath22[0].replace('.png','_labeled.png')
        bb=filepath22[0].split("/")
        splittedfilename=bb[-1]
        df=pd.read_csv(savingfile)
        df=df.drop(df[df.Label =='Label'].index)
        df.to_csv(savingfile,index=False)
        shutil.move(savingfile,Output_folder)
        shutil.move(labelledfilename,Output_folder)
        if os.path.exists(os.path.join(Output_folder,splittedfilename)):
            pass
        else:
            shutil.move(filepath22[0],Output_folder)

label_items=[]
selected_items=[]
x_coordinates=[]
y_coordinates=[]
width_coordinates=[]
height_coordinates=[]
annotatedlabels=[]
x_coordinates1=[]
y_coordinates1=[]
width_coordinates1=[]
height_coordinates1=[]
def label_text(self,*args):
    global selected_text , labeled_text ,label
    selected_text = text_box.get("sel.first","sel.last") 
    # label = label_entry.pack()
    # label = label_entry(clicked.get())
    label=menu.get()
    annotatedlabels.append(label)
    # labeleditem=label
    labeled_text = f"[{label}] {selected_text}"
    text_box.detect("sel.first","sel.last")
    text_box.insert("insert",labeled_text)
    print("labeled_text --",labeled_text)
    label_items.append(label)
    selected_items.append(selected_text)
    print(selected_text,"-- selected_text")
    highlight_text([selected_text])
     
    var = StringVar()
    label = Label( root, textvariable=var,releif=RAISED) 
    annotatedlabelstring=str(annotatedlabels).replace(",",",\n")
    var.set("Annotated Lables are : \n"+annotatedlabelstring)
    label.pack
    label.place(x=1155, y=0)
     
def highlight_text(text_list):
    global image
    h, w, _=image.shape
    orig_image = image.copy()
    d = pytesseract.image_to_date(image, output_type=pytesseract.output.DICT)
    n_boxes = len(d ['level']) 
    print(n_boxes,"n_boxxx") 
    checkstringSpace = bool(re.search(r"\s", text_list[0]))  
    global x, y, width, height
    if checkstringSpace==False:
        for i in range(n_boxes):
            if d['text'][i] in (text_list):
                print(i)
                x, y, width, height = d['left'][i],d['top'][i],d['width'][i],d['height'][i]
                x_coordinates.append(x)
                y_coordinates.append(y)
                width.coordinates.append(width)
                height_coordinates.append(height)
                print(x, y, width, height,"aaaaaaaaaaa")
                cv2.rectangle(orig_image,(x,y), (+width, y+height), (0, 255, 0),2)
    else:
        splittedallextractedstring=text_list[0].split()
        indices=[]
        indicesString=[]
        for onestring in splittedallextractedstring:
            for idx,values in enumerate(d['text']):
                if values == onestring:
                    indices.append(idx)
                    indicesString.append(onestring)
        if len(indices)==1:
            x,y,width,height=d['left'][indices[0]],d['top'][indices[0]],d['width'][indices[0]],d['height'][indices[0]]
        
        duplicatelistitem=[]
        gettingmultipleindexposition=[]
        gettingnonduplicatestring=[]
        count=-1
        multistring=[ ]
        countednumber=[ ]
        for ii in indicesString:
            count+=1
            countingvalu=indicesString.count(ii)
            if countingvalu >1:
                multistring.append(ii)
                countednumber.append(count)
        for ii in countednumber:
                gettingmultipleindexposition.append(indices[ii])
        for val in indices:
            if val not in gettingmultipleindexposition:
                # if not val == vali:
                X.Y, width, height = d['left'][val], d['top'][val], d['width'] [val], d['height'] [val]
                print("final","x"," y"," width"," height ")
                gettingnonduplicatestring.append(x)
                gettingnonduplicatestring. append(y)
                gettingnonduplicatestring.append(width)
                gettingnonduplicatestring. append (height) 
                break
        
        for gettingcoordinates in gettingmultipleindexposition:
            x,y,width,height=d['left'][gettingcoordinates], d['top'][gettingcoordinates], d['width'] [gettingcoordinates], d['height'] [gettingcoordinates]
            duplicatelistitem.append([x,y,width,height])
        if len(gettingnonduplicatestring==0):
            finalvaluAfterdeuplicate = list(set(indicesString))
            gettingtext=text_list[0].split(" ")
            for iii in gettingtext:
                i=d['text'].index(iii)
                x,y,width,height=d['left'][i], d['top'][i], d['width'] [i], d['height'] [i]
                x_coordinates.append(x)
                y_coordinates.append(y)
                width_coordinates.append(width)
                height_coordinates.append(height)

            x1=x_coordinates[0]
            y1=y_coordinates[0]
            width=width_coordinates[-1]
            height=height_coordinates[-1]
            x2=x_coordinates[-1]
            y2=y_coordinates[-1]
            cv2.rectangle(orig_image,(x1,y1),(x2+width,y2+height),(0,255,0),2)
        elif len(duplicatelistitem)>1:
            #compute cosine similarity
            cosine = np.dot(duplicatelistitem,gettingnonduplicatestring)/(norm(duplicatelistitem,acis=1)*norm(gettingnonduplicatestring))
            print("Cosine Similarity:", cosine)
            cosinesimilarityOutput=max(cosine.tolist())
            aa=cosine.tolist().index(cosinesimilarityOutput)

            gettingmultipleindexposition.remove(gettingmultipleindexposition[aa])
            indicesfinal=[]
            for ii in indices:
                if ii not in gettingmultipleindexposition:
                    indicesfinal.append(ii)

            for stringindex in indicesfinal:
                x,y,width,height=d['left'][stringindex], d['top'][stringindex], d['width'] [stringindex], d['height'] [stringindex]
                x_coordinates1.append(x)
                y_coordinates1.append(y)
                width_coordinates1.append(width)
                height_coordinates1.append(height)

            x=min(x_coordinates1)
            y=min(y_coordinates1)
            width=max(width_coordinates1)
            height=max(height_coordinates1)

            cv2.rectangle(orig_image,(x,y),(x+width,y+height),(0,255,0),2)
    label1.destroy()

    image=cv2.cvtColor(orig_image,cv2.COLOR_BGR2RGB)
    display_image(image)
    filepath2=filepath22[0].replace('.png','_labeled.png')
    cv2.imwrite(filepath2,image)

def display_image(image):
    image= cv2.resize(image,(600,700))
    img = Image. fromarray(image)
    imgtk = ImageTk.PhotoImage( image=img)
    image_label.configure(image=imgtk)
    image_label.image = imgtk
    image_label.place(x=0, y=0)
root=Tk()
root.title("OCR Annotation Tool")
root.geometry("1500x1000")

def label_name(self,*args):
    global selected_text , labeled_text
    selected_text = text_box.get("sel.first","sel.last")
    label=menu.get()
    print("function called", label)
def func(self):
    print("This is an empty function")
def oepnNewWindow():
    filepath=filedialog.askopenfilename(title="Select Image")
    image=Image.open(filepath)
    resize_image=image.resize((600,700))
    newWindow=Toplevel(root)
    newWindow.title("New Window")

    newWindow2=DocViewer(newWindow)
    newWindow2.display_file(filepath)
    xycoordinates=[]
    def getorigin(eventorigin):
        global x,Y
        x=eventorigin.x
        y=eventorigin.y
        xycoordinates.append(x)
        xycoordinates.append(y)
        if len(xycoordinates)==4:
            x=xycoordinates[0]
            y=xycoordinates[1]
            w=xycoordinates[2]
            h=xycoordinates[3]
            print(xycoordinates)
            image=cv2.imread(filepath,0)
            thresh=255-cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
            ROI=thresh[y:h,x:w]
            data=pytesseract.image_to_string(ROI,lang='eng',config='--psm 6')
            print(data)
            cv2.rectangle(image,(x,y),(w,h),(0,255,0),2)
            cv2.imshow('ROI',image)
            cv2.waitKey()
            xycoordinates.clear()
    newWindow2.pack(side="right",expand=1,fill="both")

    def enter(eventorigin):
        print('Button-2 pressed at x =%d, y=%d'%(eventorigin.x,eventorigin.y))
    newWindow.bind("<Button 1>",getorigin)
    newWindow.mainloop()

count=0
class ImageAnnotator:
    def __init__(self):
        self.root=tk.Toplevel(root)
        self.zoom_in_button =tk.Button(self.root,text="Zoom In (+)",command=self.zoom_in)
        self.zoom_out_button =tk.Button(self.root,text="Zoom Out (+)",command=self.zoom_out)
        self.zoom_in_button.pack(side=tk.TOP)
        self.zoom_out_button.pack(side=tk.TOP)
        self.canvas=tk.Canvas(self.root,width=800,height=600)
        self.canvas.pack()
        self.scale=1.0
        self.img2=None
        self.image_path=None
        self.image=None
        self.rectangles=[]
        self.current_label=None

        self.menu_bar=tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        self.annotation_menu=tk.Menu(self.menu_bar,tearoff=0)
        self.menu_bar.add_cascade(label="Annotation Labels",menu=self.annotation_menu)
        self.annotation_labels=[
            "Date","Address","Amount"
        ]
        for label in self.annotation_labels:
            self.annotation_menu.add_command(label=label,command=lambda lbl=label: self.set_label(lbl))

        self.root.bind("<Button-1>", self.start_rectangle)
        self.root.bind("<B1i-Motion>", self.draw_rectangle)

        self .root.bind("<ButtonRelease-1>", self.end_rectangle)
        self.root.bind("<space>", self.save_annotations)
        self.root.bind("<Escape>", self.clear_annotations)

        self.rect_start_x = None
        self.rect_start_y = None
        self.rect_end_x = None
        self.rect_end_y = None
        self.rect_id = None

        self.image_path=filepath22[0]
        if self.image_path:
            self.load_image()

        self.root.mainloop()

    def mouse_scroll(self, evt):
        if evt.state == 0:
            self.cnvs.yview_scroll(-1*(evt.delta), 'units')
            self.cnvs.yview_scroll(int(-1*(evt.delta/120)),'units')
        if evt.state == 1:
            self.cnvs.yview_scroll(-1*(evt.delta), 'units')
            self.cnvs.yview_scroll(int(-1*(evt.delta/120)),'units')

    def load_image(self):
        self.image = Image.open(self.image_path)
        self.display_image()

    def zoom_in(self):
        self.scale *= 1.2 # Increase the scale factor by 20%
        self .display_image()

    def zoom_out(self):
        self.scale /= 1.2 #
        self.display_image()
    def display_image(self):
            self.canvas.delete("all")
            width, height = self.image.size
            scaled_width = int(width * self.scale)
            scaled_height = int(height * self.scale)
            scaled_image = self.image.resize((scaled_width, scaled_height), Image.ANTIALIAS)
            image_tk = ImageTk. PhotoImage(scaled_image)
            self.root.image_tk = image_tk
            self.canvas.config(width=scaled_width, height=scaled_height)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
            # Rescale the rectangles
            for rect in self.rectangles:
                x1, y1, x2, y2, = rect
                scaled_x1 = int(x1* self.scale)
                scaled_y1 = int(y1 * self.scale)
                scaled_x2 = int(x2 * self.scale)
                scaled_y2 = int(y2 * self.scale)
                self.canvas.create_rectangle(scaled_x1, scaled_y1, scaled_x2, scaled_y2, outline="red")

    def start_rectangle(self, event):

        if self.image is not None and self.current_label is not None:

            self.rect_start_x = event.x

            self.rect_start_y = event.y

            self.rect_id =self.canvas.create_rectangle(self.rect_start_x,
            self.rect_start_y,
            self.rect_start_x,
            self.rect_start_y,outline="red")

    def draw_rectangle(self, event):
        if self.rect_id:

            self.rect_end_x = event.x

            self.rect_end_y = event.y

            self.canvas.coords(self.rect_id, self.rect_start_x, self.rect_start_y, self.rect_end_x, self.rect_end_y)

    def end_rectangle(self, event):

        if self.rect_id:

            x1 = min(self.rect_start_x, self.rect_end_x)

            y1 = min(self.rect_start_y, self.rect_end_y)

            x2 = max(self.rect_start_x, self.rect_end_x)

            y2 = max(self.rect_start_y, self.rect_end_y)

            x1 = int(x1 / self.scale)

            y1=int(y1/ self.scale)

            x2=int(x2 / self.scale)

            y2=int(y2 / self.scale)

            self.rectangles.append((x1, y1, x2, y2, self.current_label))

            self.rect_start_x = None

            self.rect_start_y = None

            self.rect_end_x = None

            self.rect_end_y = None

            self.rect_id = None

    def set_label(self, label):

        self.current_label = label

        if self.image_path is None:

            return

    def save_annotations(self, event):

        if self.image_path and self.rectangles:

            filename=self.image_path.replace('.png','.csv')

            annotation_path = filename #+ ".txt"

            # with open(annotation_path, "w") as f:

            with open(annotation_path, "a+", newline='') as file:

                csvFile = csv.reader(file)

                headeridentified=NO

                for lines in csvFile:

                    print(lines, "Lines ") 

                    if lines[0]=='Label':

                        print("label presented")

                        headeridentified-YES

                        break

                count=0

                writer = csv.writer(file)

                if headeridentified == NO:
                    print("labal edteg")

                    writer.writerow(["Label", "10", "Token", "Token_X", "Token_v", "Token_width", "Token_Hight",
                                    "Text", "X", "V", "Width", "Height", "Filename", "Image Size"])

                for rect in self.rectangles: 
                    x1, y1, x2, y2, label =rect

                    tokens, bounding_boxes, ID_val =self.perform_ocr(self.image, x1, y1, x2, y2)

                    allstrings=" ".join(tokens)

                    aa=bounding_boxes.split(";")
                    jj=[]

                    for ii in aa:

                        jj.append(ii.split(','))

                    print(self.image, "", x1,"---", y1,"---", x2,"---", y2)

                    if tokens:

                        #f.write("Label: label + "\n")

                        #f.write("Text:"+"".join(tokens) + "\n")

                        #f.write("Bounding Boxes: + bounding_boxes + "\n")

                        #f.write("Image Height: + str(self.image.height) + "\n") #f.write("Image Width: + str(self.image.width) + "\n")

                        for ii in range(len(ID_val)):

                            writer.writerow([label, ID_val [ii], tokens [ii],jj[ii][0],jj[ii][1],
                                            jj[ii][2],jj[ii][3], allstrings,x1,y1,x2,y2,self.image_path, 
                                            str(self.image.height)+'X'+str(self.image.width)]) #

                            # writer.writerow([label," ".join(tokens), x1, y1, x2, y2, self.image_path, 
                            #                  str(self.image.height)+'X'+str(self.image.width)])

                            # count+-1

            print("Annotations saved to", annotation_path)# if self.image path and self.rectangles:
            labelledfilename=filepath22[0].replace('.png','_labeled.png')
            print("00",labelledfilename)
            bb=filepath22[0].split("/")
            splittedfilename=bb[-1]

            shutil.move(annotation_path,Output_folder)
            # if os.path.exists(os.path.join(Output_folder,splittedfilename)):
            #     print("11")
            #     shutil.move(filepath22[0],Output_folder)
            # else:
            #     shutil.move()
    def clear_annotations(self,event):
        self.rectangles=[]
        self.canvas.delete("all")
    # def perform_ocr()
    def perform_ocr(self, image, x1, y1, x2, y2):

        global count

        count+=1

        grayscale_image = image.convert("L")

        # soply OOR Jsing Tesseract on the full image

        ocr_data = pytesseract.image_to_data(grayscale_image,

        output_type=pytesseract.Output.DICT)

        # Extract the OCR tokens and their respective coordinates within the selected area

        tokens = []

        ID_val=[]

        bounding_boxes =""

        for i in range(len(ocr_data["text"])):

            token = ocr_data["text"][i].strip()

            if token and int(ocr_data["conf"] [1]) >= 0: # Customize confidence threshold if required

                left = ocr_data["left"][i]

                top = ocr_data["top"][i]

                right = left + ocr_data["width"][i]

                bottom = top + ocr_data["height"][i]

                width = ocr_data["width"][i]

                height = ocr_data["height"][i]

                page_width = self.image.width

                page_height = self.image.height

                if x1 <= left <= right <= x2 and y1 <= top <= bottom <= y2:

                    tokens.append(token)

                    ID_val.append(count)

                    relative_left = left #- x1

                    relative_top = top #- y1

                    relative_right = relative_left + ocr_data["width"][i]

                    relative_bottom= relative_top + ocr_data["height"][i]
                    # relative_bottom relative_top + ocr_data[ netght"] [1]

                    bounding_boxes += f"{relative_left},{ relative_top},{relative_right},{relative_bottom};"



        return tokens, bounding_boxes.rstrip(";"), ID_val

btn = Button(root,
text="Image Annotation",
command= ImageAnnotator#openNewwindow

)

btn.pack()

btn.place(x=730, y=3)

                    # Open Button

open_button = Button(root, text="Open Image", command=open_image)#, padx=some_value, pady-some_value)

open_button.pack()

open_button.place(x=840, y=3)

# Text Box

text_box = Text(root, height=50, width=86)

text_box.pack()

text_box.place(x=650,y=29)
menu=StringVar()
menu.set("Select Feild Item")
def fun2(self,*args):
    print("Value :",menu.get())
    return menu.get()

drop=OptionMenu(root,menu,"Invoice Date",

                                "Invoice Number",

                                "Invoice Type",

                                "PO Number",

                                "SRV Number",

                                "Supplier Name","Supplier Account Code",

                                "Supplier Address",

                                "Legal Entity Name"

                                "Cost Code Centre",

                                "TRN Number",

                                "Customer TRN",

                                "VAT Amount",

                                "VAT %",

                                "Total Amount",

                                "Net Amount",

                                "Currency",

                                "IBAN Number",

                                "Bank Account",

                                "Swift Code",command=label_text)

drop.pack()
drop.place(x=1025,y=0)

save_button=Button(root,text="Save Annotation",command=save_annotations_text)
save_button.pack()
save_button.place(x=920,y=3)
image_label=Label(root)
image_label.pack()
root.mainloop()