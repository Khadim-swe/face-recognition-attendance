from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import PIL


class Face_Recognition_System:
  def __init__(self,root):
    self.root=root
    self.root.geometry("1530x790+0+0")
    self.root.title(" Face Recognition System")

    # first-image

    img=Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\college1.JPEG")
    img=img.resize((500,130),PIL.Image.Resampling.LANCZOS) 
    self.photoimg=ImageTk.PhotoImage(img)

    f_lbl=Label(self.root,image=self.photoimg)
    f_lbl.place(x=0,y=0,width=500,height=130)   

    # second-image

    img1=Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\college2.JPEG")
    img1=img1.resize((500,130),PIL.Image.Resampling.LANCZOS) 
    self.photoimg1=ImageTk.PhotoImage(img1)

    f_lbl=Label(self.root,image=self.photoimg1)
    f_lbl.place(x=500,y=0,width=500,height=130) 

    # third-image

    img2=Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\college3.JPEG")
    img2=img2.resize((500,130),PIL.Image.Resampling.LANCZOS) 
    self.photoimg2=ImageTk.PhotoImage(img2)

    f_lbl=Label(self.root,image=self.photoimg2)
    f_lbl.place(x=1000,y=0,width=500,height=130) 


    # background-image
    img3=Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\background.JPG")
    img3=img3.resize((1530,710),PIL.Image.Resampling.LANCZOS) 
    self.photoimg3=ImageTk.PhotoImage(img3)

    bg_img=Label(self.root,image=self.photoimg3)
    bg_img.place(x=0,y=130,width=1530,height=710) 

    title_lbl=Label(bg_img,text="Face Recognition Attendance System",font=("times new roman",35,"bold"),bg="white",fg="red")
    title_lbl.place(x=0,y=0,width=1530,height=45)

    # student Button
    img4=Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\background.JPG")
    img4=img4.resize((200,200),PIL.Image.Resampling.LANCZOS) 
    self.photoimg4=ImageTk.PhotoImage(img4)

    b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
    b1.place(x=150,y=70,width=200,height=200)

    b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red")
    b1_1.place(x=150,y=250,width=200,height=40)

       # Face Dectection Button
    img5=Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\background.JPG")
    img5=img5.resize((200,200),PIL.Image.Resampling.LANCZOS) 
    self.photoimg5=ImageTk.PhotoImage(img5)
    b2=Button(bg_img,image=self.photoimg5,cursor="hand2")
    b2.place(x=400,y=70,width=200,height=200)

    b2_2=Button(bg_img,text="Face Detection",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red")
    b2_2.place(x=400,y=250,width=200,height=40)

         # Attendance Button
    img6=Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\background.JPG")
    img6=img6.resize((200,200),PIL.Image.Resampling.LANCZOS) 
    self.photoimg6=ImageTk.PhotoImage(img6)
    b3=Button(bg_img,image=self.photoimg6,cursor="hand2")
    b3.place(x=650,y=70,width=200,height=200)

    b3_3=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red")
    b3_3.place(x=650,y=250,width=200,height=40)

    # Help Button

    img7=Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\background.JPG")
    img7=img7.resize((200,200),PIL.Image.Resampling.LANCZOS) 
    self.photoimg7=ImageTk.PhotoImage(img7)
    b4=Button(bg_img,image=self.photoimg7,cursor="hand2")
    b4.place(x=900,y=70,width=200,height=200)

    b4_4=Button(bg_img,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red")
    b4_4.place(x=900,y=250,width=200,height=40)


        # Train DataButton

    img8=Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\background.JPG")
    img8=img8.resize((200,200),PIL.Image.Resampling.LANCZOS) 
    self.photoimg8=ImageTk.PhotoImage(img8)
    b5=Button(bg_img,image=self.photoimg8,cursor="hand2")
    b5.place(x=150,y=300,width=200,height=200)

    b5_5=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red")
    b5_5.place(x=150,y=500,width=200,height=40)

     #  Photo Button

    img9=Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\background.JPG")
    img9=img9.resize((200,200),PIL.Image.Resampling.LANCZOS) 
    self.photoimg9=ImageTk.PhotoImage(img9)
    b6=Button(bg_img,image=self.photoimg9,cursor="hand2")
    b6.place(x=400,y=300,width=200,height=200)

    b6_6=Button(bg_img,text="Photo",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red")
    b6_6.place(x=400,y=500,width=200,height=40)

     # Developer Button

    img10=Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\background.JPG")
    img10=img10.resize((200,200),PIL.Image.Resampling.LANCZOS) 
    self.photoimg10=ImageTk.PhotoImage(img10)
    b5=Button(bg_img,image=self.photoimg10,cursor="hand2")
    b5.place(x=650,y=300,width=200,height=200)

    b7_7=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red")
    b7_7.place(x=650,y=500,width=200,height=40)

    # Exit Button

    img11=Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\background.JPG")
    img11=img11.resize((200,200),PIL.Image.Resampling.LANCZOS) 
    self.photoimg11=ImageTk.PhotoImage(img11)
    b8=Button(bg_img,image=self.photoimg11,cursor="hand2")
    b8.place(x=900,y=300,width=200,height=200)

    b8_8=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red")
    b8_8.place(x=900,y=500,width=200,height=40)












if __name__=="__main__":
  root=Tk()
  obj=Face_Recognition_System(root)
  root.mainloop()

