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

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("{width}x{height}+0+0".format(width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight()))
        self.root.wm_iconbitmap("face.ico")
        self.root.title("About Developer")

        full_screen_width = self.root.winfo_screenwidth()
        desired_width=full_screen_width // 2
        desired_height=self.root.winfo_screenheight()-48

        title_lbl = Label(self.root, text="DVELOPER'S SECTION",
                          font=("times new roman", 35, "bold"), bg="white", fg="navyblue")
        title_lbl.place(x=0, y=0, width=full_screen_width, height=38)

        back_btn = Button(title_lbl, text="Back", command=self.close_window,width=21,
            font=("times new roman", 10, "bold"),
            bg="Red",
            fg="white",)
        back_btn.place(x=30,y=5)

        img_top = Image.open("images/right_frame_img.jpg")
        img_top = img_top.resize((full_screen_width, 700), Image.LANCZOS)
        self.photoimage_top = ImageTk.PhotoImage(img_top)

        top_lbl = Label(self.root, image=self.photoimage_top)
        top_lbl.place(x=0, y=40, width=full_screen_width, height=700)

         # frame
        frame_dev = Frame(top_lbl, bd=2, bg="white")
        frame_dev.place(x=850, y=150, width=550, height=300)

        img_my = Image.open("images\dev.jpg")
        img_my = img_my.resize((230, 250), Image.LANCZOS)
        self.photoimage_my = ImageTk.PhotoImage(img_my)

        my_lbl = Label(frame_dev, image=self.photoimage_my)
        my_lbl.place(x=280, y=20, width=230, height=250)
        
        # Developer INFO
        dev_label1 = Label(frame_dev, text="Hello users, I am Rehan.", font=(
            "times new roman", 15, "bold"), bg="white")
        dev_label1.place(x=0,y=5)

        dev_label2 = Label(frame_dev, text="I am a B.Tech student.", font=(
            "times new roman", 15, "bold"), bg="white")
        dev_label2.place(x=0,y=30)

        dev_label3 = Label(frame_dev, text="This is my first ever software", font=(
            "times new roman", 15, "bold"), bg="white")
        dev_label3.place(x=0,y=60)

        dev_label4 = Label(frame_dev, text="I'm persuing my degree from ", font=(
            "times new roman", 15, "bold"), bg="white")
        dev_label4.place(x=0,y=95)

        dev_label5 = Label(frame_dev, text="DCRUSTM.", font=(
            "times new roman", 15, "bold"), bg="white")
        dev_label5.place(x=0,y=135)

        dev_label6 = Label(frame_dev, text="  Nice to see you", font=(
            "times new roman", 15, "bold"), bg="white")
        dev_label6.place(x=0,y=180)

    def close_window(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()