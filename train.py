from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("{width}x{height}+0+0".format(width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight()))
        self.root.wm_iconbitmap("face.ico")
        self.root.title("Training Data")

        full_screen_width = self.root.winfo_screenwidth()
        desired_width = full_screen_width // 3
        lower_img_height=self.root.winfo_screenheight()-298

        title_lbl = Label(self.root, text="TRAIN DATA SET",
                          font=("times new roman", 35, "bold"), bg="white", fg="darkred")
        title_lbl.place(x=0, y=0, width=full_screen_width, height=38)

        back_btn = Button(title_lbl, text="Back", command=self.close_window,width=21,
            font=("times new roman", 10, "bold"),
            bg="Red",
            fg="white",)
        back_btn.place(x=30,y=5)
        
        img_top = Image.open("images/train_data.jpg")
        img_top = img_top.resize((desired_width, 200), Image.LANCZOS)
        self.photoimage_top = ImageTk.PhotoImage(img_top)

        top_lbl = Label(self.root, image=self.photoimage_top)
        top_lbl.place(x=0, y=40, width=desired_width, height=200)

        img2_top = Image.open("images/face_detect.jpg")
        img2_top = img2_top.resize((desired_width, 200), Image.LANCZOS)
        self.photoimage_top2 = ImageTk.PhotoImage(img2_top)

        top2_lbl = Label(self.root, image=self.photoimage_top2)
        top2_lbl.place(x=desired_width, y=40, width=desired_width, height=200)

        img_top1 = Image.open("images/analyze_left.jpg")
        img_top1 = img_top1.resize((desired_width, 200), Image.LANCZOS)
        self.photoimage_top1 = ImageTk.PhotoImage(img_top1)

        top1_lbl = Label(self.root, image=self.photoimage_top1)
        top1_lbl.place(x=2*desired_width, y=40, width=desired_width, height=200)

        but1 = Button(self.root, text="CLICK TO TRAIN DATA", command=self.training_data, cursor="hand2", font=("times new roman", 30, "bold"), bg="darkblue",
                      fg="white")
        but1.place(x=0, y=240, width=full_screen_width, height=60)

        img_bottom = Image.open("images/train_face.jpg")
        img_bottom = img_bottom.resize((full_screen_width, lower_img_height), Image.LANCZOS)
        self.photoimage_bottom = ImageTk.PhotoImage(img_bottom)

        bottom_lbl = Label(self.root, image=self.photoimage_bottom)
        bottom_lbl.place(x=0, y=300, width=full_screen_width, height=lower_img_height)

    def training_data(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        images = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')
            img_np = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            images.append(img_np)
            ids.append(id)

            cv2.imshow("Training", img_np)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # train the classifier and save
        clla_sifier = cv2.face.LBPHFaceRecognizer_create()
        clla_sifier.train(images, ids)
        clla_sifier.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Success", "Training data completed",parent=self.root)

    def close_window(self):
        self.root.destroy()
    
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()