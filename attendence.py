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

mydata = []


class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("{width}x{height}+0+0".format(width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight()))
        self.root.wm_iconbitmap("face.ico")
        self.root.title("Attendence")
        # variables
        self.var_attend_id=StringVar()
        self.var_roll_no=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_date=StringVar()
        self.var_time=StringVar()
        self.var_attend_stat=StringVar()

        full_screen_width = self.root.winfo_screenwidth()
        desired_width = full_screen_width // 2
        lower_img_height=self.root.winfo_screenheight()-298

        # first image
        img_attend = Image.open("images/attendence_1.jpg")
        img_attend = img_attend.resize((desired_width, 150), Image.LANCZOS)
        self.photoimage_attend = ImageTk.PhotoImage(img_attend)

        f_lbl_attend = Label(self.root, image=self.photoimage_attend)
        f_lbl_attend.place(x=0, y=0, width=desired_width, height=150)

        # second image
        img_attend1 = Image.open("images/attendence_3.jpg")
        img_attend1 = img_attend1.resize((desired_width, 150), Image.LANCZOS)
        self.photoimage_attend1 = ImageTk.PhotoImage(img_attend1)

        f_lbl1_attend = Label(self.root, image=self.photoimage_attend1)
        f_lbl1_attend.place(x=desired_width, y=0, width=desired_width, height=150)

        # bg image
        img3_attend = Image.open("images/left_label.jpg")
        img3_attend = img3_attend.resize((full_screen_width, 618), Image.LANCZOS)
        self.photoimage3_attend = ImageTk.PhotoImage(img3_attend)

        bg_img_attend = Label(self.root, image=self.photoimage3_attend)
        bg_img_attend.place(x=0, y=150, width=full_screen_width, height=618)

        title_lbl_attend = Label(bg_img_attend, text="ATTENDENCE MANAGEMENT SYSTEM",
                                 font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl_attend.place(x=0, y=0, width=full_screen_width, height=38)

        back_btn = Button(title_lbl_attend, text="Back", command=self.close_window,width=21,
            font=("times new roman", 10, "bold"),
            bg="Red",
            fg="white",)
        back_btn.place(x=30,y=5)

        # frame
        main_frame_attend = Frame(bg_img_attend, bd=2, bg="white")
        main_frame_attend.place(x=7, y=42, width=full_screen_width, height=550)

        # left lable frame
        left_frame_attend = LabelFrame(main_frame_attend, bd=2, bg="white", relief=RIDGE, text="Student's Attendence Details",
                                       font=("times new roman", 10, "bold"))
        left_frame_attend.place(x=10, y=10, width=desired_width, height=530)

        img_left_attend = Image.open("images/attendence_2.jpg")
        img_left_attend = img_left_attend.resize((desired_width, 115), Image.LANCZOS)
        self.photoimage_left_attend = ImageTk.PhotoImage(img_left_attend)

        left_lbl_attend = Label(
            left_frame_attend, image=self.photoimage_left_attend)
        left_lbl_attend.place(x=5, y=0, width=desired_width, height=130)

        left_in_frame_attend = Frame(
            left_frame_attend, bd=2, relief=RIDGE, bg="white")
        left_in_frame_attend.place(x=5, y=135, width=desired_width, height=340)

        # Attendence ID
        attendenceID_label = Label(left_in_frame_attend, text="Attendence ID:", font=(
            "times new roman", 10, "bold"), bg="white")
        attendenceID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendenceID_entry_label = ttk.Entry(
            left_in_frame_attend, width=20,textvariable=self.var_attend_id, font=("times new roman", 10, "bold"))
        attendenceID_entry_label.grid(
            row=0, column=1, padx=10, pady=5, sticky=W)

        # roll no
        roll_label = Label(left_in_frame_attend, text="Roll No:", font=(
            "times new roman", 10, "bold"), bg="white")
        roll_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        roll_entry_label = ttk.Entry(
            left_in_frame_attend, width=20,textvariable=self.var_roll_no, font=("times new roman", 10, "bold"))
        roll_entry_label.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # name
        name_label = Label(left_in_frame_attend, text="Name:", font=(
            "times new roman", 10, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        name_entry_label = ttk.Entry(
            left_in_frame_attend, width=20,textvariable=self.var_name, font=("times new roman", 10, "bold"))
        name_entry_label.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # department
        department_label = Label(left_in_frame_attend, text="Department:", font=(
            "times new roman", 10, "bold"), bg="white")
        department_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        department_entry_label = ttk.Entry(
            left_in_frame_attend, width=20,textvariable=self.var_dep, font=("times new roman", 10, "bold"))
        department_entry_label.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # date
        date_label = Label(left_in_frame_attend, text="Date:", font=(
            "times new roman", 10, "bold"), bg="white")
        date_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        date_entry_label = ttk.Entry(
            left_in_frame_attend, width=20,textvariable=self.var_date, font=("times new roman", 10, "bold"))
        date_entry_label.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # time
        time_label = Label(left_in_frame_attend, text="Time:", font=(
            "times new roman", 10, "bold"), bg="white")
        time_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        time_entry_label = ttk.Entry(
            left_in_frame_attend, width=20,textvariable=self.var_time, font=("times new roman", 10, "bold"))
        time_entry_label.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # attendence status
        attend_stat_label = Label(left_in_frame_attend, text="Attendence Status:", font=(
            "times new roman", 10, "bold"), bg="white")
        attend_stat_label.grid(row=3, column=0)

        self.attend_status = ttk.Combobox(left_in_frame_attend, width=20,textvariable=self.var_attend_stat, font=(
            "times new roman", 10, "bold"), state="readonly")
        self.attend_status["values"] = ("Status", "Present", "Absent")
        self.attend_status.grid(row=3, column=1, pady=5, padx=10)
        self.attend_status.current(0)

        # button frame
        btn_frame = Frame(left_in_frame_attend, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=210, width=630, height=33)

        import_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=21, font=(
            "times new roman", 10, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0, pady=1)

        export_btn = Button(btn_frame, text="Export csv",command=self.exportCsv, width=21, font=("times new roman", 10, "bold"), bg="blue",
                            fg="white")
        export_btn.grid(row=0, column=1, pady=1)

        update_btn = Button(btn_frame, text="Update", width=21, font=("times new roman", 10, "bold"), bg="blue",
                            fg="white")
        update_btn.grid(row=0, column=2, pady=1)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=21, font=("times new roman", 10, "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=3, pady=1)

        # Right lable frame
        right_frame_attend = LabelFrame(main_frame_attend, bd=2, bg="white", relief=RIDGE, text="Student's Attendence Details",
                                        font=("times new roman", 10, "bold"))
        right_frame_attend.place(x=680, y=10, width=desired_width+50, height=530)

        table1_frame = Frame(right_frame_attend, bd=2,
                             relief=RIDGE, bg="white")
        table1_frame.place(x=5, y=0, width=desired_width+50, height=500)

        scroll1_x = ttk.Scrollbar(table1_frame, orient=HORIZONTAL)
        scroll1_y = ttk.Scrollbar(table1_frame, orient=VERTICAL)

        self.attendence_table = ttk.Treeview(table1_frame, column=(
            "id", "roll", "name", "depart", "date", "time", "status"), xscrollcommand=scroll1_x.set, yscrollcommand=scroll1_y.set)
        scroll1_x.pack(side=BOTTOM, fill=X)
        scroll1_y.pack(side=RIGHT, fill=Y)
        scroll1_x.config(command=self.attendence_table.xview)
        scroll1_y.config(command=self.attendence_table.yview)

        self.attendence_table.heading("id", text="Student ID")
        self.attendence_table.heading("roll", text="Roll No.")
        self.attendence_table.heading("name", text="Name ")
        self.attendence_table.heading("depart", text="Department")
        self.attendence_table.heading("date", text="Date")
        self.attendence_table.heading("time", text="Time")
        self.attendence_table.heading("status", text="Attendence Status")

        self.attendence_table.column("id", width=120)
        self.attendence_table.column("roll", width=120)
        self.attendence_table.column("name", width=120)
        self.attendence_table.column("depart", width=120)
        self.attendence_table.column("date", width=120)
        self.attendence_table.column("time", width=120)
        self.attendence_table.column("status", width=120)

        self.attendence_table["show"] = "headings"
        self.attendence_table.pack(fil=BOTH, expand=1)
        self.attendence_table.bind("<ButtonRelease>",self.get_data)

    # data fetching from csv file
    def fetchData(self, rows):
        self.attendence_table.delete(*self.attendence_table.get_children())
        for i in rows:
            self.attendence_table.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(
        ), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "Error", "No data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(
            ), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","Data Exported Successfully to "+os.path.basename(fln),parent=self.root)
        except Exception as e:
            messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)

    def get_data(self,event=""):
        cursor_row=self.attendence_table.focus()
        content=self.attendence_table.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_roll_no.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_date.set(rows[5])
        self.var_time.set(rows[4])
        self.var_attend_stat.set(rows[6])


    def reset_data(self):
        self.var_attend_id.set("")
        self.var_roll_no.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_date.set("")
        self.var_time.set("")
        self.var_attend_stat.set("")

    def close_window(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()