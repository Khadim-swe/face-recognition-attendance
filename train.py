from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import PIL
import cv2

import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        title_lbl = Label(self.root, text="Photo Sample Training", font=("times new roman", 26, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1275, height=35)

        # ============back button===========
        back_btn = Button(title_lbl, text="Back", command=self.root.destroy, width=15,font=("times new roman", 15, "bold"), bg="white", fg="black")
        back_btn.place(x=1050, y=0,height=32)

        # ====FOR Top Image========
        img_top = Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\background.JPG")
        img_top = img_top.resize((1275, 310),  PIL.Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1275, height=310)

        # ====FOR Butto============
        b1_1 = Button(self.root, text="TRAIN DATA",command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=350, width=1275, height=60)
        # ====FOR Bottom Image=====
        img_bottom = Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\background.JPG")
        img_bottom = img_bottom.resize((1275, 315), PIL.Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=410, width=1275, height=315)

    def train_classifier(self):
        data_dir="data"
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ides=[]

        for image in path:
            img=Image.open(image).convert('L')  # =========FOR GRAY SCALE IMAGE========
            np_image=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(np_image)
            ides.append(id)
            cv2.imshow("Training",np_image)
            cv2.waitKey(1) == 13
        ides=np.array(ides)

        # ========Train The Classifire And Save==========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ides)
        clf.write('classifier.xml')
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data sets Completed!!",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()

