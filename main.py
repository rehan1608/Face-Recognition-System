from cProfile import label
from email.mime import image
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from student_Details import StudentDetails
from train import Train
from face_detection import Recognizer
from attendence import Attendence
from developer import Developer
from help import Help
import os

class Main:
    def __init__(self, root):
        self.root = root
        self.root.geometry("{width}x{height}+0+0".format(width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight()))
        self.root.wm_iconbitmap("face.ico")
        self.root.title("Face Recognition Attendence System Software")

        main_image1 = Image.open(r"images\2_img.jpg")
        main_image1 = main_image1.resize((515, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(main_image1)
        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=0, y=0, width=515, height=130)

        main_image = Image.open(r"images\1_img.jpg")
        main_image = main_image.resize((515, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(main_image)
        second_label = Label(self.root, image=self.photoimg)
        second_label.place(x=515, y=0, width=515, height=130)

        main_image2 = Image.open(r"images\3_img.jpg")
        main_image2 = main_image2.resize((515, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(main_image2)
        third_label = Label(self.root, image=self.photoimg2)
        third_label.place(x=1030, y=0, width=515, height=130)

        # background image
        bg_img = Image.open(r"images\bgimage.jpg")
        bg_img = bg_img.resize((1550, 720), Image.LANCZOS)
        self.photoimgbg = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.root, image=self.photoimgbg)
        bg_label.place(x=0, y=130, width=1550, height=720)

        # title label
        titl_lbl = Label(
            bg_label,
            text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="green",
        )
        titl_lbl.place(x=0, y=0, width=1530, height=45)

        # Buttons for different purpose
        # 1-student details button
        std_dtl = Image.open(r"images\student_details.jpg")
        std_dtl = std_dtl.resize((220, 220), Image.LANCZOS)
        self.photoimgstdDtl = ImageTk.PhotoImage(std_dtl)
        std_dtl_btn = Button(
            bg_label, image=self.photoimgstdDtl,command=self.stDetails,cursor="hand2"
        )
        std_dtl_btn.place(x=100, y=100, width=220, height=220)
        std_dtl_btn_text = Button(
            bg_label,
            text="Student Details",
            command=self.stDetails,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        std_dtl_btn_text.place(x=100, y=319, width=220, height=50)

        # 2-Face detection button
        std2 = Image.open(r"images\face_detect.jpg")
        std2 = std2.resize((220, 220), Image.LANCZOS)
        self.photoimgstdDtl2 = ImageTk.PhotoImage(std2)
        std_dtl_btn2 = Button(bg_label, image=self.photoimgstdDtl2, cursor="hand2",command=self.face_recognize)
        std_dtl_btn2.place(x=465, y=100, width=220, height=220)
        std_dtl_btn2_text = Button(
            bg_label,
            text="Face Detector",
            command=self.face_recognize,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        std_dtl_btn2_text.place(x=465, y=319, width=220, height=50)

        # 3-Attendence button
        std3 = Image.open(r"images\attendance.jpg")
        std3 = std3.resize((220, 220), Image.LANCZOS)
        self.photoimgstdDtl3 = ImageTk.PhotoImage(std3)
        std_dtl_btn3 = Button(bg_label, image=self.photoimgstdDtl3, cursor="hand2",command=self.attendence_sheet)
        std_dtl_btn3.place(x=830, y=100, width=220, height=220)
        std_dtl_btn3_text = Button(
            bg_label,
            text="Attendance",
            command=self.attendence_sheet,
            cursor="hand2",
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        std_dtl_btn3_text.place(x=830, y=319, width=220, height=50)

        # 7-help button
        std_help = Image.open(r"images\help_desk.jpg")
        std_help = std_help.resize((220, 220), Image.LANCZOS)
        self.photoimgstdDtl_help = ImageTk.PhotoImage(std_help)
        std_dtl_btn_help = Button(
            bg_label, image=self.photoimgstdDtl_help, cursor="hand2", command=self.helo_sec
        )
        std_dtl_btn_help.place(x=1195, y=100, width=220, height=220)
        std_dtl_btn_help_text = Button(
            bg_label,
            text="Help Desk",
            cursor="hand2",
            command=self.helo_sec,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        std_dtl_btn_help_text.place(x=1195, y=319, width=220, height=50)

        # 4-Train Data button
        std_dtl4 = Image.open(r"images\train_data.jpg")
        std_dtl4 = std_dtl4.resize((220, 220), Image.LANCZOS)
        self.photoimgstdDtl4 = ImageTk.PhotoImage(std_dtl4)
        std_dtl_btn4 = Button(bg_label, image=self.photoimgstdDtl4, cursor="hand2",command=self.data_training)
        std_dtl_btn4.place(x=100, y=400, width=220, height=220)
        std_dtl_btn4_text = Button(
            bg_label,
            text="Train Face",
            cursor="hand2",
            command=self.data_training,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        std_dtl_btn4_text.place(x=100, y=620, width=220, height=50)

        # 5-Photos Data button
        std5 = Image.open(r"images\photos_collection.png")
        std5 = std5.resize((220, 220), Image.LANCZOS)
        self.photoimgstdDtl5 = ImageTk.PhotoImage(std5)
        std_dtl_btn5 = Button(bg_label, image=self.photoimgstdDtl5, cursor="hand2",command=self.open_img)
        std_dtl_btn5.place(x=465, y=400, width=220, height=220)
        std_dtl_btn5_text = Button(
            bg_label,
            text="Photos",
            cursor="hand2",
            command=self.open_img,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        std_dtl_btn5_text.place(x=465, y=620, width=220, height=50)

        # 6-Developer Section button
        std6 = Image.open(r"images\developer_section.png")
        std6 = std6.resize((220, 220), Image.LANCZOS)
        self.photoimgstdDtl6 = ImageTk.PhotoImage(std6)
        std_dtl_btn6 = Button(bg_label, image=self.photoimgstdDtl6, cursor="hand2",command=self.developer_sec)
        std_dtl_btn6.place(x=830, y=400, width=220, height=220)
        std_dtl_btn6_text = Button(
            bg_label,
            text="Developer",
            cursor="hand2",
            command=self.developer_sec,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        std_dtl_btn6_text.place(x=830, y=620, width=220, height=50)

        # 8-Exit button
        std8 = Image.open(r"images\exit.png")
        std8 = std8.resize((220, 220), Image.LANCZOS)
        self.photoimgstdDtl8 = ImageTk.PhotoImage(std8)
        std_dtl_btn8 = Button(bg_label, image=self.photoimgstdDtl8, cursor="hand2",command=self.exit_window)
        std_dtl_btn8.place(x=1195, y=400, width=220, height=220)
        std_dtl_btn8_text = Button(
            bg_label,
            text="Exit",
            cursor="hand2",
            command=self.exit_window,
            font=("times new roman", 15, "bold"),
            bg="darkblue",
            fg="white",
        )
        std_dtl_btn8_text.place(x=1195, y=620, width=220, height=50)

    def open_img(self):
        os.startfile("data")

    # ------------Declaring button function to open different windows ------------
    def stDetails(self):
        self.new_window = Toplevel(self.root)
        self.open_window = StudentDetails(self.new_window)

    def data_training(self):
        self.new_window = Toplevel(self.root)
        self.open_window = Train(self.new_window)

    def face_recognize(self):
        self.new_window=Toplevel(self.root)
        self.open_window=Recognizer(self.new_window)

    def attendence_sheet(self):
        self.new_window=Toplevel(self.root)
        self.open_window=Attendence(self.new_window)

    def developer_sec(self):
        self.new_window=Toplevel(self.root)
        self.open_window=Developer(self.new_window)

    def helo_sec(self):
        self.new_window=Toplevel(self.root)
        self.open_window=Help(self.new_window)
    
    def exit_window(self):
        self.exit_window=messagebox.askyesno("Exit","Do you want to exit?",parent=self.root)
        if self.exit_window>0:
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root = Tk()
    obj = Main(root)
    root.mainloop()
