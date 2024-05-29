import tkinter
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector # type: ignore
import os
from time import strftime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help



def main():
    win=Tk()
    app=Login(win)
    win.mainloop()


class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x790+0+0")
        self.root.title("Login")

        # ====FOR Background Image=====
        img = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\img1.jpeg")
        img = img.resize((1275, 750), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        lbl_img = Label(image=self.photoimg, bg="black", borderwidth=0)
        lbl_img.place(x=0, y=0, width=1275, height=750)
        # =======Frame=========

        frame=Frame(self.root,bg="black")
        frame.place(x=510,y=140,width=340,height=450)

        # ====FOR Logo Image=====
        img1 = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\images (3).jfif")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl_img1 =Label(image=self.photoimg1,bg="black",borderwidth=0)
        lbl_img1.place(x=632, y=150, width=100, height=100)

        get_start=Label(frame,text="Get Started",font=("times new roman", 20, "bold"),fg="white",bg="black")
        get_start.place(x=95,y=105)

        # ======Labels=======
        # ======Username=======
        username_labl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white",bg="black")
        username_labl.place(x=70,y=155)
        self.txtuser= ttk.Entry(frame, font=("times new roman", 12, "bold"))
        self.txtuser.place(x=40,y=180,width=270)

        # ======Password=======
        passsword_labl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        passsword_labl.place(x=70, y=225)
        self.txtpassword = ttk.Entry(frame, font=("times new roman", 12, "bold"))
        self.txtpassword.place(x=40, y=250, width=270)

        # ======Icon Images=======
        # ====FOR Username icon Image=====
        img2 = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\images (3).jfif")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(image=self.photoimg2, bg="black", borderwidth=0)
        lbl_img2.place(x=550,y=295, width=25, height=25)

        # ====FOR Password icon Image=====
        img3 = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\lock.jfif")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_img3 = Label(image=self.photoimg3, bg="black", borderwidth=0)
        lbl_img3.place(x=550, y=365, width=25, height=25)

        # ====FOR Login Button=====
        login_btn = Button(frame, text="Login",command=self.login,font=("times new roman", 15, "bold"), bg="red", fg="white",bd=3,relief=RIDGE,activeforeground="white",activebackground="red")
        login_btn.place(x=110, y=300, width=120, height=35)

        # ====FOR RegisterButton=====
        register_btn = Button(frame, text="New User Register",command=self.register_window, font=("times new roman", 10, "bold"),borderwidth=0, bg="black", fg="white", activeforeground="white", activebackground="black")
        register_btn.place(x=15, y=350, width=160)

        # ====FOR Forget Password Button=====
        forgetpassword_btn = Button(frame, text="Forget Password",command=self.forget_password_window, font=("times new roman", 10, "bold"),borderwidth=0, bg="black", fg="white", activeforeground="white", activebackground="black")
        forgetpassword_btn.place(x=10, y=380, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    # ==========Login Button Function=========

    def login(self):
        if self.txtuser.get() == "" or self.txtpassword.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="khadim",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                           self.txtuser.get(),
                                                                                           self.txtpassword.get()
                                                                                        ))
                row=my_cursor.fetchall()
                if row is None:
                    messagebox.showerror("Error","Invalid Username & Password")
                else:
                    open_main=messagebox.askyesno("YesNo", "Access only admin")
                    if open_main>0:
                        self.new_window = Toplevel(self.root)
                        self.app = Face_Recognition_System(self.new_window)

                    else:
                        if not open_main:
                            return

                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)



    # ====================Forget Password========================
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="khadim",database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror("Error","Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+510+170")

                labl=Label(self.root2,text="Forget Password",font=("times new roman", 15, "bold"), fg="red", bg="white")
                labl.place(x=0,y=10,relwidth=1)

                # ------------------Row3-----------
                security_q_labl = Label(self.root2, text="Select Security Option", font=("times new roman", 15, "bold"),bg="white")
                security_q_labl.place(x=50, y=80)
                self.combo_security_q = ttk.Combobox(self.root2,font=("times new roman", 12, "bold"), state="readonly")
                self.combo_security_q["values"] = ("Select", "Your Birthday Date", "Your Pet Name", "Your favorit Color ")
                self.combo_security_q.current(0)
                self.combo_security_q.place(x=50, y=110, width=250)

                security_a_labl = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                security_a_labl.place(x=50, y=150)
                self.security_a = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.security_a.place(x=50, y=180, width=250)

                new_password_labl = Label(self.root2, text="Enter New Password", font=("times new roman", 15, "bold"),bg="white")
                new_password_labl.place(x=50, y=220)
                self.new_password = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.new_password.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman", 15, "bold"), fg="white", bg="green")
                btn.place(x=100,y=300,width=150)
    # ========reset button function============
    def reset_password(self):
        if self.combo_security_q.get() == "Select":
            messagebox.showerror("Error", "Select the security question",parent=self.root2)
        elif self.security_a.get() == "":
            messagebox.showerror("Error", "Please enter the security answer",parent=self.root2)
        elif self.new_password.get() == "":
            messagebox.showerror("Error", "Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="khadim",database="face_recognizer")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s and security_q=%s and security_a=%s")
            value = (self.txtuser.get(), self.combo_security_q.get(), self.security_a.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter the correct answer",parent=self.root2)
            else:
                query = ("update register set password=%s where email=%s")
                value = (self.new_password.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset please login new password ",parent=self.root2)
                self.root2.destroy()




    def face_recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition_System(self.new_window)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Register")

        # =========variable---------
        self.var_fname=StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security_q = StringVar()
        self.var_security_a = StringVar()
        self.var_password = StringVar()
        self.var_conform_password = StringVar()


        # ============Background Image==============
        img_bg = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\tulips-3251607_960_720.jpg")
        img_bg = img_bg.resize((1275, 750), Image.ANTIALIAS)
        self.photoimg_bg = ImageTk.PhotoImage(img_bg)
        bg_img = Label(self.root, image=self.photoimg_bg)
        bg_img.place(x=0, y=0, width=1275, height=750)

        # ============Left SideImage==============
        img_left = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\thought-good-morning-messages-LoveSove.jpg")
        img_left = img_left.resize((400, 450), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        left_img = Label(self.root, image=self.photoimg_left)
        left_img.place(x=55, y=100, width=405 ,height=450)

        # =======Main Frame=========
        frame = Frame(self.root, bg="white")
        frame.place(x=460, y=100, width=670, height=450)

        # =======Register Label=========
        register_labl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green", bg="white")
        register_labl.place(x=20,y=20)

        # =======Labels and Entry =========
        # ------------------Row1-----------
        fname_labl = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname_labl.place(x=50, y=80)
        fname = ttk.Entry(frame,textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname.place(x=50, y=110, width=250)

        lname_labl = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lname_labl.place(x=370, y=80)
        lname = ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        lname.place(x=370, y=110, width=250)

        # ------------------Row2-----------
        contact_labl = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact_labl.place(x=50, y=150)
        contact = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        contact.place(x=50, y=180, width=250)

        email_labl = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email_labl.place(x=370, y=150)
        email = ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15, "bold"))
        email.place(x=370, y=180, width=250)

        # ------------------Row3-----------
        security_q_labl = Label(frame, text="Select Security Option", font=("times new roman", 15, "bold"), bg="white")
        security_q_labl.place(x=50, y=220)
        self.combo_security_q = ttk.Combobox(frame,textvariable=self.var_security_q,font=("times new roman", 12, "bold"), state="readonly")
        self.combo_security_q["values"] = ("Select", "Your Birthday Date", "Your Pet Name","Your favorit Color ")
        self.combo_security_q.current(0)
        self.combo_security_q.place(x=50, y=250, width=250)

        security_a_labl = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_a_labl.place(x=370, y=220)
        security_a = ttk.Entry(frame,textvariable=self.var_security_a, font=("times new roman", 15, "bold"))
        security_a.place(x=370, y=250, width=250)

        # ------------------Row4-----------
        password_labl = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        password_labl.place(x=50, y=290)
        password = ttk.Entry(frame,textvariable=self.var_password, font=("times new roman", 15, "bold"))
        password.place(x=50, y=320, width=250)

        conform_password_labl = Label(frame, text="Conform Password", font=("times new roman", 15, "bold"), bg="white")
        conform_password_labl.place(x=370, y=290)
        conform_password = ttk.Entry(frame,textvariable=self.var_conform_password, font=("times new roman", 15, "bold"))
        conform_password.place(x=370, y=320, width=250)

        # ==========Check Button==========
        self.var_check=IntVar()
        check_btn=Checkbutton(frame,variable=self.var_check, text="I Agree The Terms & Condition", font=("times new roman", 12, "bold"),onvalue=1,offvalue=0)
        check_btn.place(x=50,y=360)

        # ============Buttons==============
        img = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\download.jpg")
        img= img.resize((200, 50), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        btn_img = Button(frame, image=self.photoimg,command=self.register_data,borderwidth=0,cursor="hand2")
        btn_img.place(x=40, y=400, width=200)

        img2 = Image.open(r"C:\Users\Khadim\Desktop\Face Recognaization System\img\login-icon-button-blue-glossy-260nw-45529618.jpg")
        img2= img2.resize((200, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        btn2_img = Button(frame, image=self.photoimg2,command=self.return_login, borderwidth=0, cursor="hand2")
        btn2_img.place(x=370, y=400, width=200)

    # ===========Function Declaration=============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_q.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_password.get() != self.var_conform_password.get():
            messagebox.showerror("Error","password & conform password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree all terms & conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="khadim",database="face_recognizer")
            my_cursor = conn.cursor()
            query="select * from register where email=%s"
            value =(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","User already exist please try an other email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_fname.get(),
                                                                                       self.var_lname.get(),
                                                                                       self.var_contact.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_security_q.get(),
                                                                                       self.var_security_a.get(),
                                                                                       self.var_password.get()
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Register successfully",parent=self.root)
    def return_login(self):
        self.root.destroy()


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

        # ======Time=====
        def time():
            string=strftime('%H:%M:%S %p')
            title_lbl.config(text=string)
            title_lbl.after(1000,time)

            lbl=Label(title_lbl,font=("times new roman",14,"bold"),bg="white",fg="blue")
            lbl.place(x=0,y=0,width=10,height=40)
            time()


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
    main()
