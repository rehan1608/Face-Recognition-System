from cProfile import label
from cgitb import text
from email.mime import image
from tkinter import *
from tkinter import ttk
from traceback import format_exc
from turtle import color
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class StudentDetails:
    def __init__(self, root):
        self.root = root
        self.root.geometry("{width}x{height}+0+0".format(width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight()))
        self.root.wm_iconbitmap("face.ico")
        self.root.title("Face Recognition Attendence System Software")

        # -----Declaring text variable to fill data from database-------
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

        main_image1 = Image.open(r"images\stdDtl1.jpg")
        main_image1 = main_image1.resize((515, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(main_image1)
        first_label = Label(self.root, image=self.photoimg1)
        first_label.place(x=0, y=0, width=515, height=130)

        main_image = Image.open(r"images\stdDtl3.jpg")
        main_image = main_image.resize((515, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(main_image)
        second_label = Label(self.root, image=self.photoimg)
        second_label.place(x=515, y=0, width=515, height=130)

        main_image2 = Image.open(r"images\stdDtl2.png")
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
            text="Student Details",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="red",
        )
        titl_lbl.place(x=0, y=0, width=1530, height=45)

        back_btn = Button(titl_lbl, text="Back", command=self.close_window,width=21,
            font=("times new roman", 10, "bold"),
            bg="Red",
            fg="white",)
        back_btn.place(x=30,y=5)

        # frame on bg image
        main_frame = Frame(bg_label, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1515, height=645)

        # left label frame onto the main_frame
        left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 12, "bold"),
        )
        left_frame.place(x=10, y=10, width=700, height=620)

        left_image = Image.open(r"images\left_label.jpg")
        left_image = left_image.resize((680, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(left_image)
        left_label = Label(left_frame, image=self.photoimg_left)
        left_label.place(x=10, y=0, width=680, height=130)

        # Current Course info onto the left_frame
        courseInfoframe = LabelFrame(
            left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Current Course",
            font=("times new roman", 10, "bold"),
        )
        courseInfoframe.place(x=10, y=140, width=680, height=150)

        # making different labels onto the courseInfoframe
        # 1-Department label
        dep_label = Label(
            courseInfoframe,
            text="Department",
            font=("times new roman", 10, "bold"),
            bg="white",
        )
        dep_label.grid(row=0, column=0, padx=2, pady=10)

        dep_combo = ttk.Combobox(
            courseInfoframe,
            textvariable=self.var_dep,
            font=("times new roman", 10, "bold"),
            width=17,
            state="readonly",
        )
        dep_combo["values"] = ("Select Department", "ECE", "CSE", "ME", "EE", "CIVIL")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # 2-course
        course_lable = Label(
            courseInfoframe,
            text="Course",
            font=("times new roman", 10, "bold"),
            bg="white",
        )
        course_lable.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(
            courseInfoframe,
            textvariable=self.var_course,
            font=("times new roman", 10, "bold"),
            state="readonly",
            width=17,
        )
        course_combo["values"] = (
            "Select Course",
            "BEE",
            "HUMANTIES",
            "Programming",
            "Physics",
            "Mathematics",
        )
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        Year_lable = Label(
            courseInfoframe,
            text="Year",
            font=("times new roman", 10, "bold"),
            bg="white",
        )
        Year_lable.grid(row=1, column=0, padx=10, sticky=W)

        Year_combo = ttk.Combobox(
            courseInfoframe,
            textvariable=self.var_year,
            font=("times new roman", 10, "bold"),
            state="readonly",
            width=17,
        )
        Year_combo["values"] = (
            "Select Year",
            "2020-21",
            "2021-22",
            "2022-23",
            "2023-24",
        )
        Year_combo.current(0)
        Year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        Semester_lable = Label(
            courseInfoframe,
            
            text="Semester",
            font=("times new roman", 10, "bold"),
            bg="white",
        )
        Semester_lable.grid(row=1, column=2, padx=10, sticky=W)

        Semester_combo = ttk.Combobox(
            courseInfoframe,
            textvariable=self.var_semester,
            font=("times new roman", 10, "bold"),
            state="readonly",
            width=17,
        )
        Semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2")
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class_Student_Information
        Class_Student_frame = LabelFrame(
            left_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Class Student Information",
            font=("times new roman", 10, "bold"),
        )
        Class_Student_frame.place(x=10, y=300, width=680, height=280)

        # student id
        id_lable = Label(
            Class_Student_frame,
            text="Student ID :",
            font=("times new roman", 10, "bold"),
            bg="white",
        )
        id_lable.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        id_entry_label = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_std_id,
            width=20,
            font=("times new roman", 10, "bold"),
        )
        id_entry_label.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # student name
        name_lable = Label(
            Class_Student_frame,
            text="Student Name :",
            font=("times new roman", 10, "bold"),
            bg="white",
        )
        name_lable.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        name_entry_label = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_std_name,
            width=20,
            font=("times new roman", 10, "bold"),
        )
        name_entry_label.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # class division
        division_lable = Label(
            Class_Student_frame,
            text="Class Division :",
            font=("times new roman", 10, "bold"),
            bg="white",
        )
        division_lable.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        div_combo = ttk.Combobox(
            Class_Student_frame,
            textvariable=self.var_div,
            font=("times new roman", 10, "bold"),
            state="readonly",
            width=17,
        )
        div_combo["values"] = ("Select Division", "A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No.
        rollno_lable = Label(
            Class_Student_frame,
            text="Roll No. :",
            font=("times new roman", 10, "bold"),
            bg="white",
        )
        rollno_lable.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        rollno_entry_label = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_roll,
            width=20,
            font=("times new roman", 10, "bold"),
        )
        rollno_entry_label.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        Gender_lable = Label(
            Class_Student_frame,
            text="Gender :",
            font=("times new roman", 10, "bold"),
            bg="white",
        )
        Gender_lable.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(
            Class_Student_frame,
            textvariable=self.var_gender,
            font=("times new roman", 10, "bold"),
            state="readonly",
            width=17,
        )
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # D.O.B
        dob_lable = Label(
            Class_Student_frame,
            text="D.O.B :",
            font=("times new roman", 10, "bold"),
            bg="white",
        )
        dob_lable.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry_label = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_dob,
            width=20,
            font=("times new roman", 10, "bold"),
        )
        dob_entry_label.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # E-mail
        mail_lable = Label(
            Class_Student_frame,
            text="E-mail :",
            font=("times new roman", 10, "bold"),
            bg="white",
        )
        mail_lable.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        mail_entry_label = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_email,
            width=20,
            font=("times new roman", 10, "bold"),
        )
        mail_entry_label.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No.
        pn_lable = Label(
            Class_Student_frame,
            text="Phone No. :",
            font=("times new roman", 10, "bold"),
            bg="white",
        )
        pn_lable.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        pn_entry_label = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_phone,
            width=20,
            font=("times new roman", 10, "bold"),
        )
        pn_entry_label.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        addr_lable = Label(
            Class_Student_frame,
            text="Address :",
            font=("times new roman", 10, "bold"),
            bg="white",
        )
        addr_lable.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        addr_entry_label = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_address,
            width=20,
            font=("times new roman", 10, "bold"),
        )
        addr_entry_label.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher's Name
        tne_lable = Label(
            Class_Student_frame,
            text="Teacher's Name :",
            font=("times new roman", 10, "bold"),
            bg="white",
        )
        tne_lable.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        tne_entry_label = ttk.Entry(
            Class_Student_frame,
            textvariable=self.var_teacher,
            width=20,
            font=("times new roman", 10, "bold"),
        )
        tne_entry_label.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio button
        self.var_r1 = StringVar()
        rb1 = ttk.Radiobutton(
            Class_Student_frame,
            variable=self.var_r1,
            text="Take Photo Sample",
            value="Yes",
        )
        rb1.grid(row=6, column=0, padx=10, pady=10)

        rb2 = ttk.Radiobutton(
            Class_Student_frame,
            variable=self.var_r1,
            text="No Photo Sample",
            value="No",
        )
        rb2.grid(row=6, column=1)

        # button frame
        btn_frame = Frame(Class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=190, width=630, height=33)

        save_btn = Button(
            btn_frame,
            text="Save",
            command=self.fill_data,
            width=21,
            font=("times new roman", 10, "bold"),
            bg="blue",
            fg="white",
        )
        save_btn.grid(row=0, column=0, pady=1)

        update_btn = Button(
            btn_frame,
            command=self.up_data,
            text="Update",
            width=21,
            font=("times new roman", 10, "bold"),
            bg="blue",
            fg="white",
        )
        update_btn.grid(row=0, column=1, pady=1)

        delete_btn = Button(
            btn_frame,
            text="Delete",
            command=self.del_but,
            width=21,
            font=("times new roman", 10, "bold"),
            bg="blue",
            fg="white",
        )
        delete_btn.grid(row=0, column=2, pady=1)

        reset_btn = Button(
            btn_frame,
            text="Reset",
            command=self.rest_data,
            width=21,
            font=("times new roman", 10, "bold"),
            bg="blue",
            fg="white",
        )
        reset_btn.grid(row=0, column=3, pady=1)

        # 2nd button frame
        btn1_frame = Frame(Class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn1_frame.place(x=5, y=226, width=630, height=32)

        take_photo_btn = Button(
            btn1_frame,
            text="Take Photo Sample",
            command=self.gen_data,
            width=43,
            font=("times new roman", 10, "bold"),
            bg="blue",
            fg="white",
        )
        take_photo_btn.grid(row=0, column=0, pady=1)

        update_photo_btn = Button(
            btn1_frame,
            text="Update Photo Sample",
            width=44,
            font=("times new roman", 10, "bold"),
            bg="blue",
            fg="white",
        )
        update_photo_btn.grid(row=0, column=1, pady=1)

        # right label frame
        right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 12, "bold"),
        )
        right_frame.place(x=750, y=10, width=750, height=620)

        img_right = Image.open(r"images\right_frame_img.jpg")
        img_right = img_right.resize((730, 130), Image.LANCZOS)
        self.photoimage_right = ImageTk.PhotoImage(img_right)

        right_lbl = Label(right_frame, image=self.photoimage_right)
        right_lbl.place(x=10, y=0, width=730, height=130)

        # search system
        search_Student_frame = LabelFrame(
            right_frame,
            bd=2,
            bg="white",
            relief=RIDGE,
            text="Search System",
            font=("times new roman", 10, "bold"),
        )
        search_Student_frame.place(x=10, y=140, width=730, height=70)

        search_lable = Label(
            search_Student_frame,
            text="Search By ",
            font=("times new roman", 10, "bold"),
            bg="white",
        )
        search_lable.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(
            search_Student_frame,
            font=("times new roman", 10, "bold"),
            state="readonly",
            width=15,
        )
        search_combo["values"] = ("Select", "Roll No.", "Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        sarch_entry_label = ttk.Entry(
            search_Student_frame, width=20, font=("times new roman", 10, "bold")
        )
        sarch_entry_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(
            search_Student_frame,
            text="Search",
            width=15,
            font=("times new roman", 10, "bold"),
            bg="blue",
            fg="white",
        )
        search_btn.grid(row=0, column=3, padx=10)

        show_all_btn = Button(
            search_Student_frame,
            text="Show All",
            width=15,
            font=("times new roman", 10, "bold"),
            bg="blue",
            fg="white",
        )
        show_all_btn.grid(row=0, column=4, padx=10)

        # table frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=220, width=730, height=360)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            column=(
                "Dept",
                "Course",
                "Year",
                "Sem",
                "ID",
                "Name",
                "Div",
                "Roll No.",
                "Gender",
                "DOB",
                "E-mail",
                "Phone",
                "Address",
                "Teacher",
                "Photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dept", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("ID", text="Student ID")
        self.student_table.heading("Name", text="Student Name")
        self.student_table.heading("Div", text="Division")
        self.student_table.heading("Roll No.", text="Roll No.")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("E-mail", text="E-mail")
        self.student_table.heading("Phone", text="Contact No.")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table.heading("Photo", text="PhotoSampleStatus")

        self.student_table.column("Dept", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Div", width=100)
        self.student_table.column("Roll No.", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("E-mail", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Teacher", width=100)
        self.student_table.column("Photo", width=150)

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.update_data)
        self.fetch_data()

    # --------------Function declaration to add data from database=----------
    def fill_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="@INDIA12tnb", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
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
                    self.var_r1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student details has been addedd Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to : {str(es)}", parent=self.root)
    # fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="@INDIA12tnb", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

     # update data cursor
    def update_data(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
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
        self.var_r1.set(data[14])

    # data update function
    def up_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                updated = messagebox.askyesno(
                    "Update", "Do you want to update the details", parent=self.root)
                if updated > 0:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="@INDIA12tnb", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set `Dep`=%s,`Course`=%s, `Year`=%s,`Semester`=%s,`Name`=%s,`Div`=%s,`RollNum`=%s,`Gender`=%s,`DOB`=%s,`Email`=%s,`Phone`=%s,`Address`=%s,`Teacher`=%s,`PhotoSample`=%s where `Student_iD`=%s", (
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
                        self.var_r1.get(),
                        self.var_std_id.get()

                    ))
                else:
                    if not updated:
                        return
                messagebox.showinfo(
                    "Success", "Updated Successfully.", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to : {str(es)}", parent=self.root)


    # delete function
    def del_but(self):
        if self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "Student ID is required", parent=self.root)
        else:
            try:
                delt = messagebox.askyesno(
                    "Warnng!", "Do you want to delete this data?", parent=self.root)
                if delt > 0:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="@INDIA12tnb", database="face_recognizer")
                    my_cursor = conn.cursor()
                    que = "delete from student where `Student_iD`=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(que, val)
                else:
                    if not delt:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Deleted", "Details deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to : {str(es)}", parent=self.root)
    # reset data

    def rest_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_r1.set("")
    
    def close_window(self):
        self.root.destroy()
    
    # genearate dataset and photo Sample
    def gen_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="@INDIA12tnb", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                fetching_all = my_cursor.fetchall()
                id = 0
                for i in fetching_all:
                    id += 1
                my_cursor.execute("update student set `Dep`=%s,`Course`=%s, `Year`=%s,`Semester`=%s,`Name`=%s,`Div`=%s,`RollNum`=%s,`Gender`=%s,`DOB`=%s,`Email`=%s,`Phone`=%s,`Address`=%s,`Teacher`=%s,`PhotoSample`=%s where `Student_iD`=%s", (
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
                    self.var_r1.get(),
                    self.var_std_id.get() == id+1

                ))
                conn.commit()
                self.fetch_data()
                self.rest_data
                conn.close()

                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def img_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)

                    for (x, y, w, h) in faces:
                        img_cropped = img[y:y+h, x:x+w]
                        return img_cropped

                vid_cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = vid_cap.read()
                    if img_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(
                            img_cropped(my_frame), (400, 400))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        img_strd_path = "data/user." +str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(img_strd_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Crooped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                vid_cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Collected", "Images Collection completed successfully",parent=self.root)

            except Exception as e:
                messagebox.showerror("Error", f"Due to : {str(e)}",parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = StudentDetails(root)
    root.mainloop()
