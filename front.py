from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
import time
from time import strftime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\BestFacialRecognition.jpg")
        img=img.resize((425,115),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=425,height=115)



        img1 = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\facialrecognition.png")
        img1 = img1.resize((425, 115), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=425, y=0, width=425, height=115)

        img2 = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\images - Copy.jpg")
        img2 = img2.resize((425, 115), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=850, y=0, width=425, height=115)

        #============BackgroundImage==============
        img3 = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\bg.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=115, width=1275, height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",28,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1275,height=35)


        #========Image Student Button========
        img4 = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\student.jpg")
        img4 = img4.resize((200,200), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_file,cursor="hand2")
        b1.place(x=135,y=50,width=200,height=200)

        b1_1 = Button(bg_img,text="Students Details",command=self.student_file,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=135, y=250, width=200, height=40)

        # ========Detect Button========
        img5 = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\face_detector1.jpg")
        img5= img5.resize((200, 200), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=395, y=50, width=200, height=200)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=395, y=250, width=200, height=40)

        # ========Attendance Button========
        img6 = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\face.jpg")
        img6 = img6.resize((200, 200), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b1.place(x=655, y=50, width=200, height=200)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=655, y=250, width=200, height=40)

        # ========Help Button========
        img7 = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\help.jpg")
        img7 = img7.resize((200, 200), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.help_data)
        b1.place(x=920, y=50, width=200, height=200)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_data, font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=920, y=250, width=200, height=40)

        # ========Train Button========
        img8 = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\di.jpg")
        img8 = img8.resize((200, 200), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=135, y=325, width=200, height=200)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=135, y=525, width=200, height=40)

        # ========Photos Button========
        img9 = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\smart-attendance.jpg")
        img9 = img9.resize((200, 200), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=395, y=325, width=200, height=200)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=395, y=525, width=200, height=40)

        # ========Developer Button========
        img10 = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\dev.jpg")
        img10= img10.resize((200, 200), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.developer_data)
        b1.place(x=655, y=325, width=200, height=200)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2",command=self.developer_data, font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=655, y=525, width=200, height=40)


        # ========Exit  Button========
        img11 = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\exit.jpg")
        img11= img11.resize((200, 200), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.iExit)
        b1.place(x=920, y=325, width=200, height=200)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit, font=("times new roman", 15, "bold"),bg="darkblue", fg="white")
        b1_1.place(x=920, y=525, width=200, height=40)

        bottom_lbl = Label(bg_img, text="Leadership is the ability to facilitate movement in the needed direction and have people feel good about it",font=("times new roman", 18, "bold"), bg="white", fg="red")
        bottom_lbl.place(x=0, y=575, width=1275, height=35)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are You Sure Want To Exit This Project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return


    #=========Function Button========

    def student_file(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window )

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
