from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ==============Variables===========
        self.var_attend_id = StringVar()
        self.var_attend_department = StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_roll = StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_attendance = StringVar()



        # ======first image=========
        img = Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\college1.JPEG")
        img = img.resize((635, 150), PIL.Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=635, height=150)

        # ======second image=========
        img1 = Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\college1.JPEG")
        img1 = img1.resize((635, 150), PIL.Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=635, y=0, width=635, height=150)

        # ============BackgroundImage==============
        img2 = Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\college1.JPEG")
        img2 = img2.resize((1275, 600), PIL.Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=150, width=1275, height=600)

        # =======Title=======
        title_lbl = Label(bg_img, text="STUDENT ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1275, height=30)

        # ============back button===========
        back_btn = Button(title_lbl, text="Back", command=self.root.destroy, width=15,font=("times new roman", 15, "bold"), bg="white", fg="red")
        back_btn.place(x=1100, y=0,height=25)
        # ======Main Frame=======
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=45, width=1260, height=525)

        # ==============Left Label Frame======
        left_frame = LabelFrame(main_frame, bd=2, bg="white",fg="red", relief=RIDGE, text="Student Information", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=3, width=610, height=515)

        # =====Left Image======
        img_left = Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\college1.JPEG")
        img_left = img_left.resize((610, 125), PIL.Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=610, height=125)

        # =============Left Inside Frame======
        left_inside_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE)
        left_inside_frame.place(x=0, y=130, width=605, height=350)

        # =============Labels and Entry=======
        # ======Attendance ID=======
        attendanceid_labl = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 12, "bold"),bg="white")
        attendanceid_labl.grid(row=0, column=0, padx=10, sticky="w")

        attendanceid_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attend_id, width=15,font=("times new roman", 12, "bold"))
        attendanceid_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # ======Student Department=======
        attendance_dep_labl = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"),bg="white")
        attendance_dep_labl.grid(row=0, column=2, padx=10, sticky="w")

        attendance_dep_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attend_department, width=15, font=("times new roman", 12, "bold"))
        attendance_dep_entry.grid(row=0, column=3, padx=10, pady=5, sticky="w")

        # ======Student Name=======
        studentname_labl = Label(left_inside_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white")
        studentname_labl.grid(row=1, column=0, padx=10, sticky="w")

        studentname_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attend_name, width=15,font=("times new roman", 12, "bold"))
        studentname_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # ======Roll Number=======
        roll_labl = Label(left_inside_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
        roll_labl.grid(row=1, column=2, padx=10, sticky="w")

        roll_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attend_roll, width=15, font=("times new roman", 12, "bold"))
        roll_entry.grid(row=1, column=3, padx=10, pady=5, sticky="w")

        # ======Date=======
        attendance_date_labl = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        attendance_date_labl.grid(row=2, column=0, padx=10, sticky="w")

        attendance_date_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attend_date, width=15, font=("times new roman", 12, "bold"))
        attendance_date_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # ======Time=======
        attendance_time_labl = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        attendance_time_labl.grid(row=2, column=2, padx=10, sticky="w")

        attendance_time_entry = ttk.Entry(left_inside_frame,textvariable=self.var_attend_time, width=15, font=("times new roman", 12, "bold"))
        attendance_time_entry.grid(row=2, column=3, padx=10, pady=5, sticky="w")

        # ======Attendance=======
        attendance_labl = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white")
        attendance_labl.grid(row=3, column=0, padx=10, sticky="w")

        self.attend_status = ttk.Combobox(left_inside_frame,textvariable=self.var_attend_attendance,font=("times new roman", 12, "bold"), width=13, state="readonly")
        self.attend_status["values"] = ("Status", "Present", "Absent")
        self.attend_status.current(0)
        self.attend_status.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # =============Button Frame======
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=250, width=585, height=38)

        import_btn = Button(btn_frame, text="Import csv",command=self.importcsv, width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export csv",command=self.exportcsv, width=15,font=("times new roman", 12, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", width=15, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset" ,command=self.reset_data,  width=15,font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # ==============Right Label Frame======
        right_frame = LabelFrame(main_frame, bd=2, bg="white",fg="red", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=640, y=3, width=610, height=515)

        # =============Right Table Frame======
        table_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=595, height=480)

        # =============Scrollbar Table======
        scroll_x =ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_report_table=ttk.Treeview(table_frame,column=("id","department","name","roll","date","time","attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.attendance_report_table.xview)
        scroll_y.config(command=self.attendance_report_table.yview)

        self.attendance_report_table.heading("id",text="Attendance ID")
        self.attendance_report_table.heading("department", text="Department")
        self.attendance_report_table.heading("name", text="Name")
        self.attendance_report_table.heading("roll", text="Roll No")
        self.attendance_report_table.heading("date", text="Date")
        self.attendance_report_table.heading("time", text="Time")
        self.attendance_report_table.heading("attendance", text="Attendance")
        self.attendance_report_table["show"] = "headings"

        self.attendance_report_table.column("id", width=100)
        self.attendance_report_table.column("department", width=100)
        self.attendance_report_table.column("name", width=100)
        self.attendance_report_table.column("roll", width=100)
        self.attendance_report_table.column("date", width=100)
        self.attendance_report_table.column("time", width=100)
        self.attendance_report_table.column("attendance", width=100)

        self.attendance_report_table.pack(fill=BOTH, expand=1)
        self.attendance_report_table.bind("<ButtonRelease>",self.get_cursor)

    # ========Fetch Data==================
    def fetch_data(self,rows):
        self.attendance_report_table.delete(*self.attendance_report_table.get_children())
        for i in rows:
            self.attendance_report_table.insert("",END,values=i)
    # ========Import CSV File Data=========
    def importcsv(self):
        global mydata
        mydata.clear()
        filn=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
        with open(filn) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    # =========Export CSV File Data=============
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found To Export",parent=self.root)
                return False
            filn = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            with open(filn,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Has Been Exported To " +os.path.basename(filn) +  " Successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # ==============Get Cursor==============
    def get_cursor(self, event=""):
        cursor_row = self.attendance_report_table.focus()
        content = self.attendance_report_table.item(cursor_row)
        rows = content["values"]
        self.var_attend_id.set(rows[0])
        self.var_attend_department.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_roll.set(rows[3])
        self.var_attend_date.set(rows[4])
        self.var_attend_time.set(rows[5])
        self.var_attend_attendance.set(rows[6])

    # =============Reset Data==========
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_department.set("")
        self.var_attend_name.set("")
        self.var_attend_roll.set("")
        self.var_attend_date.set("")
        self.var_attend_time.set("")
        self.var_attend_attendance.set("")



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
