from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox



class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1270, height=40)

        # ============back button===========
        back_btn = Button(title_lbl, text="Back", command=self.root.destroy, width=15,font=("times new roman", 15, "bold"), bg="white", fg="black")
        back_btn.place(x=1050, y=0,height=35)

        # ====FOR Main Image========
        img_top = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\dev.jpg")
        img_top = img_top.resize((1270, 700), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1270, height=700)

        # ======Main Frame=======
        main_frame = Frame(f_lbl, bd=2, bg="black")
        main_frame.place(x=800, y=0, width=450, height=500)

        # ====FOR Right Image========
        img_right = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\IMG-20210310-WA0004.jpg")
        img_right = img_right.resize((200, 200), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(main_frame, image=self.photoimg_right)
        f_lbl.place(x=247, y=0, width=200, height=200)

        # ==============Developer Info Label======
        develop_label = Label(main_frame ,text="Hello! My name is", font=("times new roman", 15, "bold"),bg="black",fg="white")
        develop_label.place(x=0, y=5)

        develop_label = Label(main_frame, text="Khadim.", font=("times new roman", 17, "bold"), bg="black", fg="orange")
        develop_label.place(x=0, y=35)

        develop_label = Label(main_frame, text="I am full stack developer my", font=("times new roman", 12, "bold"), bg="black",fg="white")
        develop_label.place(x=0, y=70)

        develop_label = Label(main_frame, text="specialization front end and back ", font=("times new roman", 12, "bold"), bg="black", fg="white")
        develop_label.place(x=0, y=100)

        develop_label = Label(main_frame, text="end developer for programming ", font=("times new roman", 12, "bold"), bg="black", fg="white")
        develop_label.place(x=0, y=130)

        develop_label = Label(main_frame, text="languages python,java,C++,html,css.", font=("times new roman", 12, "bold"), bg="black", fg="white")
        develop_label.place(x=0, y=160)

        # ====FOR Right Image========
        img_bottom = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\images (1).jpg")
        img_bottom = img_bottom.resize((446, 297), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(main_frame, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=200, width=446, height=297)



if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()