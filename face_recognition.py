from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import PIL
from tkinter import messagebox
import mysql.connector 
from time import strftime
from datetime import datetime
import cv2 
import os


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white",fg="blue")
        title_lbl.place(x=0, y=0, width=1275, height=40)

        # ============back button===========
        back_btn = Button(title_lbl, text="Back", command=self.root.destroy, width=15,font=("times new roman", 15, "bold"), bg="white", fg="black")
        back_btn.place(x=1050, y=0,height=35)

        # ====For Right Image========
        img_right = Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\college1.JPEG")
        img_right = img_right.resize((650, 650), PIL.Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(self.root, image=self.photoimg_right)
        f_lbl.place(x=0, y=45, width=650, height=650)

        # ====FOR Left Image========
        img_left = Image.open(r"C:\Users\Khadim\OneDrive\Desktop\Face Recognaization System\college-images\college1.JPEG")
        img_left = img_left.resize((750, 650), PIL.Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image=self.photoimg_left)
        f_lbl.place(x=650, y=45, width=750, height=650)

        # ====FOR Butto============
        b1_1 = Button(f_lbl, text="FACE RECOGNITION", cursor="hand2", command=self.face_recog,font=("times new roman", 12, "bold"),bg="dark green", fg="white")
        b1_1.place(x=272, y=573, width=200, height=40)

    # ===============Attendance============
    def mark_attendance(self, i, r, n, d):
        with open("khadim.csv", "r+", newline="\n") as f:
            mydatalist = f.readlines()
            name_list = []
            for line in mydatalist:
                entry = line.split(",")
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},present")

    # ===============face recogition========
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text,clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="root",database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                if n:
                  n = "+".join(n)
                else:
                  n = "Khadim"

                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                if r:
                  r = "+".join(r)
                else:
                  r = "6"

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d= my_cursor.fetchone()
                if d:
                  d = "+".join(d)
                else:
                  d = "Computer"

                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                if i:
                  i = "+".join(i)
                else:
                  i = "7"

                if confidence > 77:
                    cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll NO:{r}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img,f"Name:{n}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img,f"Department:{d}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, h]
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read('classifier.xml')

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img =recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                messagebox.showinfo("Info", "Detection has been completed", parent=self.root)
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
