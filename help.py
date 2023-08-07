from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np
from time import strftime
from datetime import datetime

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("{width}x{height}+0+0".format(width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight()))
        self.root.wm_iconbitmap("face.ico")
        self.root.title("About Developer")

        full_screen_width = self.root.winfo_screenwidth()
        desired_width=full_screen_width // 2
        desired_height=self.root.winfo_screenheight()//2

        title_lbl = Label(self.root, text="HELP DESK",
                          font=("times new roman", 35, "bold"), bg="white", fg="navyblue")
        title_lbl.place(x=0, y=0, width=full_screen_width, height=38)

        back_btn = Button(title_lbl, text="Back", command=self.close_window,width=21,
            font=("times new roman", 10, "bold"),
            bg="Red",
            fg="white",)
        back_btn.place(x=30,y=5)

        img_top = Image.open("images/contact_us.jpg")
        img_top = img_top.resize((full_screen_width, 700), Image.LANCZOS)
        self.photoimage_top = ImageTk.PhotoImage(img_top)

        top_lbl = Label(self.root, image=self.photoimage_top)
        top_lbl.place(x=0, y=40, width=full_screen_width, height=700)

        help_desk1 = Label(top_lbl, text="Contact me at ↴", font=(
            "times new roman", 15, "bold"), bg="white")
        help_desk1.place(x=desired_width-100,y=desired_height-200)


        help_desk2 = Label(top_lbl, text="E-mail: raorehan79@gmail.com", font=(
            "times new roman", 15, "bold"), bg="white")
        help_desk2.place(x=desired_width-150,y=desired_height-170)

    def close_window(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()