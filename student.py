from tkinter import*
from tkinter import ttk
import PIL
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
             def __init__(self, root):
              self.root = root
              self.root.geometry("1530x790+0+0")
              self.root.title("Face Recognition System")

              # ==============Variables===========
              self.var_dep = StringVar()
              self.var_course = StringVar()
              self.var_year = StringVar()
              self.var_semester = StringVar()
              self.var_std_id = StringVar()
              self.var_std_name = StringVar()
              self.var_div = StringVar()
              self.var_roll = StringVar()
              self.var_gender = StringVar()
              self.var_dob = StringVar()
              self.var_email = StringVar()
              self.var_phone = StringVar()
              self.var_address = StringVar()
              self.var_teacher = StringVar()

              img = Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\college1.JPEG")
              img = img.resize((425, 115), PIL.Image.Resampling.LANCZOS)
              self.photoimg = ImageTk.PhotoImage(img)
              f_lbl = Label(self.root, image=self.photoimg)
              f_lbl.place(x=0, y=0, width=425, height=115)

              img1 = Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\college2.JPEG")
              img1 = img1.resize((425, 115), PIL.Image.Resampling.LANCZOS)
              self.photoimg1 = ImageTk.PhotoImage(img1)
              f_lbl = Label(self.root, image=self.photoimg1)
              f_lbl.place(x=425, y=0, width=425, height=115)

              img2 = Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\college3.JPEG")
              img2 = img2.resize((425, 115), PIL.Image.Resampling.LANCZOS)
              self.photoimg2 = ImageTk.PhotoImage(img2)
              f_lbl = Label(self.root, image=self.photoimg2)
              f_lbl.place(x=850, y=0, width=425, height=115)

              # ============BackgroundImage==============
              img3 = Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\college1.JPEG")
              img3 = img3.resize((1275, 710), PIL.Image.Resampling.LANCZOS)
              self.photoimg3 = ImageTk.PhotoImage(img3)

              bg_img = Label(self.root, image=self.photoimg3)
              bg_img.place(x=0, y=115, width=1275, height=710)

              title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 28, "bold"), bg="white", fg="blue")
              title_lbl.place(x=0, y=0, width=1275, height=35)

              # ============back button===========
              back_btn = Button(title_lbl, text="Back",command=self.root.destroy, width=15,font=("times new roman", 15, "bold"), bg="white", fg="black")
              back_btn.place(x=1050,y=0,height=32)



              # =========Main Frame=================
              main_frame = Frame(bg_img, bd=2, bg="white")
              main_frame.place(x=10, y=40, width=1250, height=565)

              # ==============LableFrame======

              left_Frame = LabelFrame(main_frame, bd=2, bg="white",fg="red", relief=RIDGE, text="Student Information", font=("times new roman", 12, "bold"))
              left_Frame.place(x=15, y=0, width=600, height=580)

              img_left = Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\college1.JPEG")
              img_left = img_left.resize((600, 115), PIL.Image.Resampling.LANCZOS)
              self.photoimg_left = ImageTk.PhotoImage(img_left)
              f_lbl = Label(left_Frame, image=self.photoimg_left)
              f_lbl.place(x=0, y=0, width=600, height=115)

              # =============Current Course======

              current_course_Frame = LabelFrame(left_Frame, bd=2, bg="white",fg="darkgreen", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
              current_course_Frame.place(x=5, y=120, width=590, height=95)

              # ======Department=======
              dep_labl = Label(current_course_Frame, text="Department", font=("times new roman", 11, "bold"), bg="white")
              dep_labl.grid(row=0, column=0, padx=10, sticky="w")

              dep_combo = ttk.Combobox(current_course_Frame, textvariable=self.var_dep, font=("times new roman", 11, "bold"), width=17, state="readonly")
              dep_combo["values"] = ("Select Department", "Computer", "Physic", "Math", "Chemistry")
              dep_combo.current(0)
              dep_combo.grid(row=0, column=1, padx=2, pady=5, sticky="w")

              # ======Course=======
              course_labl = Label(current_course_Frame, text="Course", font=("times new roman", 11, "bold"), bg="white")
              course_labl.grid(row=0, column=2, padx=10, sticky="w")

              course_combo = ttk.Combobox(current_course_Frame, textvariable=self.var_course, font=("times new roman", 11,  "bold"), width=17, state="readonly")
              course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
              course_combo.current(0)
              course_combo.grid(row=0, column=3, padx=2, pady=5, sticky="w")

              # ======Year=======
              year_labl = Label(current_course_Frame, text="Year", font=("times new roman", 11, "bold"), bg="white")
              year_labl.grid(row=1, column=0, padx=10, sticky="w")

              year_combo = ttk.Combobox(current_course_Frame, textvariable=self.var_year, font=("times new roman", 11, "bold"), width=17, state="readonly")
              year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
              year_combo.current(0)
              year_combo.grid(row=1, column=1, padx=2, pady=5, sticky="w")

              # ======Semester=======
              semester_labl = Label(current_course_Frame, text="Semester", font=("times new roman", 11, "bold"), bg="white")
              semester_labl.grid(row=1, column=2, padx=10, sticky="w")

              semester_combo = ttk.Combobox(current_course_Frame, textvariable=self.var_semester, font=("times new roman", 11, "bold"), width=17, state="readonly")
              semester_combo["values"] = ("Select Year", "Semester-1", "Semester-2")
              semester_combo.current(0)
              semester_combo.grid(row=1, column=3, padx=2, pady=5, sticky="w")

              # =============Class Student Information======
              Class_Student_Frame = LabelFrame(left_Frame, bd=2, bg="white",fg="darkgreen", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
              Class_Student_Frame.place(x=5, y=215, width=590, height=325)

              # ======Student ID=======
              studentId_labl = Label(Class_Student_Frame, text="Student ID:", font=("times new roman", 11, "bold"), bg="white")
              studentId_labl.grid(row=0, column=0, padx=10, sticky="w")

              studentId_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_std_id, width=15, font=("times new roman", 11, "bold"))
              studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

              # ======Student Name=======
              studentname_labl = Label(Class_Student_Frame, text="Student Name:", font=("times new roman", 11, "bold"), bg="white")
              studentname_labl.grid(row=0, column=2, padx=10, sticky="w")

              studentname_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_std_name, width=15, font=("times new roman", 11, "bold"))
              studentname_entry.grid(row=0, column=3, padx=10, pady=5, sticky="w")

              # ======Class Division=======
              class_division_labl = Label(Class_Student_Frame, text="Class Division:", font=("times new roman", 11, "bold"), bg="white")
              class_division_labl.grid(row=1, column=0, padx=10, sticky="w")

              class_division_combo = ttk.Combobox(Class_Student_Frame, textvariable=self.var_div, font=("times new roman",  11, "bold"), width=13, state="readonly")
              class_division_combo["values"] = ("A", "B", "C")
              class_division_combo.current(0)
              class_division_combo.grid(row=1, column=1, padx=10, pady=5, sticky="w")

              # ======Roll Number=======
              Roll_labl = Label(Class_Student_Frame, text="Roll No:", font=("times new roman", 11, "bold"), bg="white")
              Roll_labl.grid(row=1, column=2, padx=10, sticky="w")

              Roll_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_roll, width=15, font=("times new roman", 11, "bold"))
              Roll_entry.grid(row=1, column=3, padx=10, pady=5, sticky="w")

              # ======Gender=======
              gender_labl = Label(Class_Student_Frame, text="Gender:", font=("times new roman", 11, "bold"), bg="white")
              gender_labl.grid(row=2, column=0, padx=10, sticky="w")

              gender_combo = ttk.Combobox(Class_Student_Frame, textvariable=self.var_gender, font=("times new roman", 11, "bold"), width=13, state="readonly")
              gender_combo["values"] = ("Male", "Female", "Other")
              gender_combo.current(0)
              gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky="w")

              # ======Date OF Birth=======
              dob_labl = Label(Class_Student_Frame, text="D.O.B:", font=("times new roman", 11, "bold"), bg="white")
              dob_labl.grid(row=2, column=2, padx=10, sticky="w")

              dob_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_dob, width=15, font=("times new roman", 11, "bold"))
              dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky="w")

              # ======Email=======
              email_labl = Label(Class_Student_Frame, text="Email:", font=("times new roman", 11, "bold"), bg="white")
              email_labl.grid(row=3, column=0, padx=10, sticky="w")

              email_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_email, width=15, font=("times new roman", 11, "bold"))
              email_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

              # ======Phone=======
              phone_labl = Label(Class_Student_Frame, text="Phone No:", font=("times new roman", 11, "bold"), bg="white")
              phone_labl.grid(row=3, column=2, padx=10, sticky="w")

              phone_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_phone, width=15, font=("times new roman", 11, "bold"))
              phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky="w")

              # ======Address=======
              address_labl = Label(Class_Student_Frame, text="Address:", font=("times new roman", 11, "bold"), bg="white")
              address_labl.grid(row=4, column=0, padx=10, sticky="w")

              address_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_address, width=15, font=("times new roman", 11, "bold"))
              address_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

              # ======Teacher Name=======
              teachername_labl = Label(Class_Student_Frame, text="Teacher Name:", font=("times new roman", 11, "bold"), bg="white")
              teachername_labl.grid(row=4, column=2, padx=10, sticky="w")

              teachername_entry = ttk.Entry(Class_Student_Frame, textvariable=self.var_teacher, width=15, font=("times new roman", 11, "bold"))
              teachername_entry.grid(row=4, column=3, padx=10, pady=5, sticky="w")

              # ======Radio Button=======
              self.var_radio1 = StringVar()
              radiobtn1 = ttk.Radiobutton(Class_Student_Frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
              radiobtn1.grid(row=6, column=0,padx=10,pady=20)

              radiobtn2 = ttk.Radiobutton(Class_Student_Frame, variable=self.var_radio1, text="No Photo Sample", value="No")
              radiobtn2.grid(row=6, column=1)

              # =============Button Frame======
              btn_frame = Frame(Class_Student_Frame, bd=2, relief=RIDGE)
              btn_frame.place(x=0, y=230, width=585, height=38)

              save_btn = Button(btn_frame, text="Save", command=self.add_data, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
              save_btn.grid(row=0, column=0)

              update_btn = Button(btn_frame, text="update", command=self.update_data, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
              update_btn.grid(row=0, column=1)

              delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
              delete_btn.grid(row=0, column=2)

              reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
              reset_btn.grid(row=0, column=3)

              # =============Button Frame======
              btn_Fram1 = LabelFrame(Class_Student_Frame, bd=2, bg="white", relief=RIDGE)
              btn_Fram1.place(x=0, y=265, width=585, height=38)

              take_photo_sample_btn = Button(btn_Fram1 ,command=self.generate_dataset, text="Take photo Sample", width=31, font=("times new roman", 12, "bold"), bg="blue", fg="white")
              take_photo_sample_btn.grid(row=0, column=0)

              update_photo_btn = Button(btn_Fram1, text="Update Photo Sample", width=32, font=("times new roman", 12, "bold"), bg="blue", fg="white")
              update_photo_btn.grid(row=0, column=1)

              # ========Small Image=======
              img_small = Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\college1.JPEG")
              img_small = img_small.resize((300, 65), PIL.Image.Resampling.LANCZOS)
              self.photoimg_small = ImageTk.PhotoImage(img_small)
              f_lbl = Label(Class_Student_Frame, image=self.photoimg_small)
              f_lbl.place(x=285, y=165, width=300, height=65)

              # ==============Right LableFrame======
              Right_Frame = LabelFrame(main_frame, bd=2, bg="white",fg="red", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
              Right_Frame.place(x=630, y=0, width=600, height=580)

              img_right = Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\college1.JPEG")
              img_right = img_right.resize((600, 200), PIL.Image.Resampling.LANCZOS)
              self.photoimg_right = ImageTk.PhotoImage(img_right)
              f_lbl = Label(Right_Frame, image=self.photoimg_right)
              f_lbl.place(x=0, y=0, width=600, height=200)

              # =============Search System======

              search_Frame = LabelFrame(Right_Frame, bd=2, bg="white", relief=RIDGE, text="View Student Details & Search System", font=("times new roman", 11, "bold"))
              search_Frame.place(x=5, y=200, width=590, height=70)

              search_labl = Label(search_Frame, text="Search By", width=10, font=("times new roman", 15, "bold"), bg="red", fg="white")
              search_labl.grid(row=0, column=0, padx=5, sticky="w")

              search_combo = ttk.Combobox(search_Frame, font=("times new roman", 10, "bold"), width=10, state="readonly")
              search_combo["values"] = ("Select Option", "Roll", "Name", "Phon_No")
              search_combo.current(0)
              search_combo.grid(row=0, column=1, padx=2, pady=10, sticky="w")

              search_entry = ttk.Entry(search_Frame, width=12, font=("times new roman", 11, "bold"))
              search_entry.grid(row=0, column=2, padx=10, pady=5, sticky="w")

              search_btn = Button(search_Frame, text="Search", width=10, font=("times new roman", 11, "bold"), bg="blue",  fg="white")
              search_btn.grid(row=0, column=3, padx=4)

              showall_btn = Button(search_Frame, text="Show All", width=10, font=("times new roman", 11, "bold"), bg="blue", fg="white")
              showall_btn.grid(row=0, column=4, padx=4)

              # =============Table Frame======

              table_Frame =Frame(Right_Frame, bd=2, bg="white", relief=RIDGE)
              table_Frame.place(x=5, y=275, width=590, height=260)

              scroll_x = Scrollbar(table_Frame, orient=HORIZONTAL)
              scroll_y = Scrollbar(table_Frame, orient=VERTICAL)

              self.Student_table = ttk.Treeview(table_Frame, columns=("dep", "course", "year", "semester", "student_id", "student_name", "class_division", "Roll", "gender", "dob", "email", "phone", "address", "teacher_name", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
              scroll_x.pack(side=BOTTOM, fill=X)
              scroll_y.pack(side=RIGHT, fill=Y)

              scroll_x.config(command=self.Student_table.xview)
              scroll_y.config(command=self.Student_table.yview)

              self.Student_table.heading("dep", text="Department")
              self.Student_table.heading("course", text="Course")
              self.Student_table.heading("year", text="Year")
              self.Student_table.heading("semester", text="Semester")
              self.Student_table.heading("student_id", text="Student ID")
              self.Student_table.heading("student_name", text="Student Name")
              self.Student_table.heading("class_division", text="Division")
              self.Student_table.heading("Roll", text="Roll No")
              self.Student_table.heading("gender", text="Gender")
              self.Student_table.heading("dob", text="D.O.B")
              self.Student_table.heading("email", text="Email")
              self.Student_table.heading("phone", text="Phone")
              self.Student_table.heading("address", text="Address")
              self.Student_table.heading("teacher_name", text="Teacher Name")
              self.Student_table.heading("photo", text="Photo Sample Status")
              self.Student_table["show"] = "headings"

              self.Student_table.column("dep", width=100)
              self.Student_table.column("course", width=100)
              self.Student_table.column("year", width=100)
              self.Student_table.column("semester", width=100)
              self.Student_table.column("student_id", width=100)
              self.Student_table.column("student_name", width=100)
              self.Student_table.column("class_division", width=100)
              self.Student_table.column("Roll", width=100)
              self.Student_table.column("gender", width=100)
              self.Student_table.column("dob", width=100)
              self.Student_table.column("email", width=100)
              self.Student_table.column("phone", width=100)
              self.Student_table.column("address", width=100)
              self.Student_table.column("teacher_name", width=100)
              self.Student_table.column("photo", width=150)

              self.Student_table.pack(fill=BOTH, expand=1)
              self.Student_table.bind("<ButtonRelease>", self.get_cursor)
              self.fetch_data()

              # ==================Function Declearation==================
             def add_data(self):
                 if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                    messagebox.showerror("Error", "All Fields are required", parent=self.root)
                 else:
                     try:
                         conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                         my_cursor = conn.cursor()
                         my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                                         self.var_dep.get(),
                                                                                                                         self.var_course.get(),
                                                                                                                         self.var_year.get(),
                                                                                                                         self.var_semester.get(),
                                                                                                                         self.var_std_id.get(),
                                                                                                                         self.var_std_name.get(),
                                                                                                                         self.var_div.get(),
                                                                                                                         self.var_roll.get(),
                                                                                                                         self.var_gender.get(),
                                                                                                                         self.var_dob.get(),
                                                                                                                         self.var_email.get(),
                                                                                                                         self.var_phone.get(),
                                                                                                                         self.var_address.get(),
                                                                                                                         self.var_teacher.get(),
                                                                                                                         self.var_radio1.get()
                                                                                                                    ))
                         conn.commit()
                         self.fetch_data()
                         conn.close()
                         messagebox.showinfo("Success", "Student details has been added successfully", parent=self.root)
                     except Exception as es:
                         messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

             # ==============Fetch Data===================
             def fetch_data(self):
                 conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                 my_cursor = conn.cursor()
                 my_cursor.execute("select * from student")
                 data = my_cursor.fetchall()

                 if len(data) != 0:
                     self.Student_table.delete(*self.Student_table.get_children())
                     for i in data:
                        self.Student_table.insert("", END, values=i)
                     conn.commit()
                 conn.close()
             # ==============Get Cursor==============
             def get_cursor(self, event=""):
                 cursor_focus = self.Student_table.focus()
                 content = self.Student_table.item(cursor_focus)
                 data = content["values"]

                 self.var_dep.set(data[0]),
                 self.var_course.set(data[1]),
                 self.var_year.set(data[2]),
                 self.var_semester.set(data[3]),
                 self.var_std_id.set(data[4]),
                 self.var_std_name.set(data[5]),
                 self.var_div.set(data[6]),
                 self.var_roll.set(data[7]),
                 self.var_gender.set(data[8]),
                 self.var_dob.set(data[9]),
                 self.var_email.set(data[10]),
                 self.var_phone.set(data[11]),
                 self.var_address.set(data[12]),
                 self.var_teacher.set(data[13]),
                 self.var_radio1.set(data[14])

             # ==============Update Function===========
             def update_data(self):
                 if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                     messagebox.showerror("Error", "All Fields are required", parent=self.root)
                 else:
                     try:
                         Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                         if Update>0:
                             conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                             my_cursor = conn.cursor()
                             my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s  where Student_id=%s",(

                                                                                                                                                                                             self.var_dep.get(),
                                                                                                                                                                                             self.var_course.get(),
                                                                                                                                                                                             self.var_year.get(),
                                                                                                                                                                                             self.var_semester.get(),
                                                                                                                                                                                             self.var_std_name.get(),
                                                                                                                                                                                             self.var_div.get(),
                                                                                                                                                                                             self.var_roll.get(),
                                                                                                                                                                                             self.var_gender.get(),
                                                                                                                                                                                             self.var_dob.get(),
                                                                                                                                                                                             self.var_email.get(),
                                                                                                                                                                                             self.var_phone.get(),
                                                                                                                                                                                             self.var_address.get(),
                                                                                                                                                                                             self.var_teacher.get(),
                                                                                                                                                                                             self.var_radio1.get(),
                                                                                                                                                                                             self.var_std_id.get()
                                                                                                                                                                                         ))
                         else:
                             if not Update:
                                 return
                         messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
                         conn.commit()
                         self.fetch_data()
                         conn.close()
                     except Exception as es:
                         messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

             # ==============Delete Function===============
             def delete_data(self):
                 if self.var_std_id.get() == "":
                     messagebox.showerror("Error", "Student id must be required", parent=self.root)
                 else:
                     try:
                         delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student", parent=self.root)
                         if delete > 0:
                             conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                             my_cursor = conn.cursor()
                             query="delete from student where Student_id=%s"
                             value=(self.var_std_id.get(),)
                             my_cursor.execute(query,value)
                         else:
                             if not delete:
                                 return
                         conn.commit()
                         self.fetch_data()
                         conn.close()
                         messagebox.showinfo("Delete","Student details has been deleted successfully", parent=self.root)
                     except Exception as es:
                         messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

             # =============Reset Data==========
             def reset_data(self):
                 self.var_dep.set("Select Department")
                 self.var_course.set("Select Course")
                 self.var_year.set("Select Year")
                 self.var_semester.set("Select Semester")
                 self.var_std_id.set("")
                 self.var_std_name.set("")
                 self.var_div.set("Select Division")
                 self.var_roll.set("")
                 self.var_gender.set("Male")
                 self.var_dob.set("")
                 self.var_email.set("")
                 self.var_phone.set("")
                 self.var_address.set("")
                 self.var_teacher.set("")
                 self.var_radio1.set("")

             # ===============Generate Data Set and Take Photo Sample===========
             def generate_dataset(self):
                 if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                     messagebox.showerror("Error", "All Fields are required", parent=self.root)
                 else:
                     try:
                         conn = mysql.connector.connect(host="localhost", username="root", password="root",database="face_recognizer")
                         my_cursor = conn.cursor()
                         my_cursor.execute("select * from student")
                         myresult=my_cursor.fetchall()
                         id=0
                         for x in myresult:
                             id+=1
                         my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s  where Student_id=%s",(

                                                                                                                                                                                     self.var_dep.get(),
                                                                                                                                                                                     self.var_course.get(),
                                                                                                                                                                                     self.var_year.get(),
                                                                                                                                                                                     self.var_semester.get(),
                                                                                                                                                                                     self.var_std_name.get(),
                                                                                                                                                                                     self.var_div.get(),
                                                                                                                                                                                     self.var_roll.get(),
                                                                                                                                                                                     self.var_gender.get(),
                                                                                                                                                                                     self.var_dob.get(),
                                                                                                                                                                                     self.var_email.get(),
                                                                                                                                                                                     self.var_phone.get(),
                                                                                                                                                                                     self.var_address.get(),
                                                                                                                                                                                     self.var_teacher.get(),
                                                                                                                                                                                     self.var_radio1.get(),
                                                                                                                                                                                     self.var_std_id.get()==id+1
                                                                                                                                                                                 ))
                         conn.commit()
                         self.fetch_data()
                         self.reset_data()
                         conn.close()

                         # ========Load Predefined Data on Face Frontals From Opencv========
                         face_classifire=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                         def face_cropped(img):
                             gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                             faces=face_classifire.detectMultiScale(gray,1.3,5)
                             #===Scaling Factor= 1.3====
                             #====Minimum Neighbour=5====
                             for (x,y,w,h) in faces:
                                 face_cropped=img[y:y+h,x:x+w]
                                 return face_cropped

                         cap=cv2.VideoCapture(0)
                         img_id=0
                         while True:
                             ret,my_frame=cap.read()
                             if face_cropped(my_frame) is not None:
                                 img_id+=1
                                 face=cv2.resize(face_cropped(my_frame),(450,450))
                                 face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                 filename_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                                 cv2.imwrite(filename_path,face)
                                 cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                 cv2.imshow("Cropped Face",face)

                             if cv2.waitKey(1)==13 or int(img_id)==50:
                                break
                         cap.release()
                         cv2.destroyAllWindows()
                         messagebox.showinfo("Result","Generating Data Set Completed!!",parent=self.root)
                     except Exception as es:
                         messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)




if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
