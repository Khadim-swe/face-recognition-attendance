from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox



class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1270, height=40)

        # ============back button===========
        back_btn = Button(title_lbl, text="Back", command=self.root.destroy, width=15,font=("times new roman", 15, "bold"), bg="white", fg="black")
        back_btn.place(x=1050, y=0,height=35)

        # ====FOR Main Image========
        img_top = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top = img_top.resize((1270, 700), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1270, height=700)

        # ==============Left Label Frame======
        help_label = Label(f_lbl, bd=2, text="Email:k.hussain1051@gmail.com", font=("times new roman", 20, "bold"),bg="white",fg="blue")
        help_label.place(x=416, y=200)




if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()