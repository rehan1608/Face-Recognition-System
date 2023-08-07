from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import csv


class Recognizer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("{width}x{height}+0+0".format(width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight()))
        self.root.wm_iconbitmap("face.ico")
        self.root.title("Face Detector")

        full_screen_width = self.root.winfo_screenwidth()
        desired_width=full_screen_width // 2
        desired_height=self.root.winfo_screenheight()-48

        title_lbl = Label(self.root, text="FACE RECOGNITION",
                          font=("times new roman", 45, "bold"), bg="white", fg="navyblue")
        title_lbl.place(x=0, y=0, width=full_screen_width, height=48)

        back_btn = Button(title_lbl, text="Back", command=self.close_window,width=21,
            font=("times new roman", 10, "bold"),
            bg="Red",
            fg="white",)
        back_btn.place(x=30,y=5)

        img_left = Image.open("images/analyze_left.jpg")
        img_left = img_left.resize((desired_width, desired_height), Image.LANCZOS)
        self.photoimage_left = ImageTk.PhotoImage(img_left)

        left_lbl = Label(self.root, image=self.photoimage_left)
        left_lbl.place(x=0, y=50, width=desired_width, height=desired_height)

        img_right = Image.open("images/face_detect.jpg")
        img_right = img_right.resize((desired_width, desired_height), Image.LANCZOS)
        self.photoimage_right = ImageTk.PhotoImage(img_right)

        right_lbl = Label(self.root, image=self.photoimage_right)
        right_lbl.place(x=desired_width, y=50, width=desired_width, height=desired_height)

        titl_lbl = Label(self.root, text="1 0 "*455,
                         font=("times new roman", 15, "bold"), bg="green", fg="navyblue")
        titl_lbl.place(x=0, y=725, width=full_screen_width, height=20)

        but_face = Button(right_lbl,command=self.recog_face ,text="Analyze", cursor="hand2", font=("times new roman", 20, "bold"), bg="red",
                          fg="white")
        but_face.place(x=300, y=630, width=150, height=35)

    # mark attendence
    def mark_attendance(self, var1, var2, var3, var4):
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y")
        t1 = now.strftime("%H:%M:%S")
        attendance_data = f"{var4},{var2},{var1},{var3},{t1},{d1},Present"

        with open("sheet/Attendence_Sheet.csv", "r", newline="\n") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    if row[0] == str(var4):
                        return  

        # Append the new attendance data to the CSV file
        with open("sheet/Attendence_Sheet.csv", "a", newline="\n") as f:
            f.write("\n" + attendance_data)


    # rcognition function
    def recog_face(self):
        def draw_bound(img, classifier, scaleFactor, minNeighbour,color, text, clla_sifier):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbour)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img,(x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clla_sifier.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", user="root", password="@INDIA12tnb", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select Name from student where Student_iD="+str(id))
                var1 = my_cursor.fetchone()
                name = var1[0] if var1 else ""
                
                my_cursor.execute(
                    "select RollNum from student where Student_iD="+str(id))
                var2 = my_cursor.fetchone()
                rollnum = var2[0] if var2 else ""
                
                my_cursor.execute(
                    "select Dep from student where Student_iD="+str(id))
                var3=my_cursor.fetchone()
                dep = var3[0] if var3 else ""
                
                my_cursor.execute(
                    "select Student_iD from student where Student_iD="+str(id))
                var4 = my_cursor.fetchone()
                std_id = var4[0] if var4 else ""
    
                if confidence > 77:
                    cv2.putText(
                        img, f"Name : {name}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Student ID. : {std_id}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Roll No. : {rollnum}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Department : {dep}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    if not self.is_attendance_marked:
                        self.mark_attendance(name,rollnum,dep,std_id)
                        self.is_attendance_marked = True
                else:
                    cv2.rectangle(img,(x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, f"Uknown Face", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            return coord

        def recog_nition(img, clla_sifier, faceCascade):
            ret_img = draw_bound(img, faceCascade, 1.1, 10,(255, 255, 255), "Face", clla_sifier)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clla_sifier = cv2.face.LBPHFaceRecognizer_create()
        clla_sifier.read("Classifier.xml")

        vide_cap = cv2.VideoCapture(0)
        self.is_attendance_marked = False

        while True:
            ret,img = vide_cap.read()
            img = recog_nition(img, clla_sifier, faceCascade)
            cv2.imshow("Welcome To face Recognition", img)
            if cv2.waitKey(33)==27:
                break
        vide_cap.release()
        cv2.destroyAllWindows()

    def close_window(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Recognizer(root)
    root.mainloop()