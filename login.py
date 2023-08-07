from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from time import strftime
from datetime import datetime
import tkinter
import mysql.connector
import os
from main import Main
from main import Main



def main():
    win = Tk()
    log_win = Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login/SignUp")
        self.root.geometry("{width}x{height}+0+0".format(width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight()))
        self.root.wm_iconbitmap("face.ico")

        width_complete=self.root.winfo_screenwidth()
        height_complete=self.root.winfo_screenheight()
        half_width=width_complete//2

        bg_image=Image.open("images/bgimage.jpg")
        bg_image=bg_image.resize((width_complete,height_complete),Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_image)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=half_width-150, y=150, width=330, height=430)

        user_img = Image.open("images/user_input.png")
        user_img = user_img.resize((90, 90), Image.LANCZOS)
        self.photoimage_user = ImageTk.PhotoImage(user_img)
        lbl_user = Label(frame,image=self.photoimage_user, bg="black", borderwidth=0)
        lbl_user.place(x=120, y=0, width=90, height=90)

        get_str = Label(frame, text="Get Started", font=(
            "times new roman", 18, "bold"), fg="white", bg="black")
        get_str.place(x=105, y=95)

        # username Label and icon
        user_label = Label(frame, text="Usernmae", font=(
            "times new roman", 13, "bold"), fg="white", bg="black")
        user_label.place(x=50, y=145)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 13, "bold"))
        self.txtuser.place(x=30, y=170, width=250, height=25)

        user_icon = Image.open("images/user_input_1.png")
        user_icon = user_icon.resize((20, 13), Image.LANCZOS)
        self.photoicon_user = ImageTk.PhotoImage(user_icon)
        lbl_user_icon = Label(
            frame, image=self.photoicon_user, bg="black", borderwidth=0)
        lbl_user_icon.place(x=30, y=152, width=20, height=13)

        # password Label and icon
        pass_label = Label(frame, text="Password", font=(
            "times new roman", 13, "bold"), fg="white", bg="black")
        pass_label.place(x=50, y=210)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 13, "bold"))
        self.txtpass.place(x=30, y=235, width=250, height=25)

        pass_icon = Image.open("images/pass.png")
        pass_icon = pass_icon.resize((20, 13), Image.LANCZOS)
        self.photoicon_pass = ImageTk.PhotoImage(pass_icon)
        lbl_pass_icon = Label(
            frame, image=self.photoicon_pass, bg="black", borderwidth=0)
        lbl_pass_icon.place(x=30, y=217, width=20, height=13)

        # buttons
        login_but = Button(frame, command=self.login_button, text="Login", font=("times new roman", 13, "bold"), bd=3,
                           relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        login_but.place(x=100, y=280, width=110, height=30)

        new_but = Button(frame, command=self.register_win, text="New User Register", font=("times new roman", 10, "bold"),
                         borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        new_but.place(x=17, y=330, width=140)

        forget_but = Button(frame, command=self.forg_pass, text="Forget Password", font=("times new roman", 10, "bold"),
                            borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forget_but.place(x=11, y=350, width=140)

        # login working

    def register_win(self):
        self.new_win = Toplevel(self.root)
        self.app = Register(self.new_win)

    def login_button(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror(
                "Error", "Username and Password can't be empty",parent=self.root)
        elif self.txtuser.get() == "Rehan" and self.txtpass.get() == "@INDIA12tnb":
            messagebox.showinfo(
                "Success", "Welcome to Face Recognition Automatic Attendence System")
        else:
            conn_database = mysql.connector.connect(
                host="localhost", user="root", password="@INDIA12tnb", database="face_recognizer")
            my_cursor = conn_database.cursor()
            my_cursor.execute("select * from register_details where Email=%s and Password=%s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))
            rows = my_cursor.fetchone()
            if rows == None:
                messagebox.showerror("Invalid", "Check username and password")
            else:
                open_main = messagebox.askyesno(
                    "Warning!", "Access only for admin")
                if open_main > 0:
                    # self.new_win = Toplevel(self.root)
                    self.app = Main(self.root)
                else:
                    if not open_main:
                        return
            conn_database.commit()
            conn_database.close()

    # reset password
    def reset_pass(self):
        if self.combo_ssq.get() == "Select Qs.":
            messagebox.showerror(
                "Error", "Select valid security question", parent=self.root2)
        elif self.sqa.get() == "":
            messagebox.showerror(
                "Error", "Security answer can't be empty", parent=self.root2)
        elif self.new_pass.get() == "":
            messagebox.showerror(
                "Error", "New password can't be empty", parent=self.root2)
        elif len(self.new_pass.get())<8:
            messagebox.showerror("Error","Password must be at least 8 characters long!")
        else:
            conn_database = mysql.connector.connect(
                host="localhost", user="root", password="@INDIA12tnb", database="face_recognizer")
            curs = conn_database.cursor()
            qry = (
                "select * from register_details where Email=%s and `Security Qs`=%s and `Security Ans`=%s")
            val = (self.txtuser.get(), self.combo_ssq.get(), self.sqa.get())
            curs.execute(qry, val)
            row = curs.fetchone()
            if row == None:
                messagebox.showerror(
                    "Check!", "Please check all the values correctly", parent=self.root2)
            else:
                qurey = ("update register_details set Password=%s where Email=%s")
                values = (self.new_pass.get(), self.txtuser.get())
                curs.execute(qurey, values)

                conn_database.commit()
                conn_database.close()
                messagebox.showinfo(
                    "Success", "Password Reset successfull, Please login with new password", parent=self.root2)

                self.root2.destroy()

    def forg_pass(self):
        if self.txtuser.get() == "":
            messagebox.showerror(
                "Error", "Please enter correct email address to reset password", parent=self.root)
        else:
            conn_database = mysql.connector.connect(
                host="localhost", user="root", password="@INDIA12tnb", database="face_recognizer")
            curs = conn_database.cursor()
            res_query = ("select * from register_details where Email=%s")
            value = (self.txtuser.get(),)
            curs.execute(res_query, value)
            roww = curs.fetchone()

            if roww == None:
                messagebox.showerror(
                    "Username Error", "Please enter correct email address to reset password", parent=self.root)
            else:
                conn_database.close()
                self.root2 = Toplevel()
                self.root2.title("Reset Password")
                self.root2.geometry("330x440+500+160")

                l = Label(self.root2, text="Reset Password", font=(
                    "times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=10, relwidth=1)

                # select security qs
                ssq = Label(self.root2, text="Select Security Qs.",
                            font=("times new roman", 15, "bold"), bg="white")
                ssq.place(x=50, y=80)
                self.combo_ssq = ttk.Combobox(self.root2, font=(
                    "times new roman", 13, "bold"), state="readonly")
                self.combo_ssq["values"] = (
                    "Select Qs.", "Birth Month", "Bestfriend", "Sport", "Subject")
                self.combo_ssq.place(x=50, y=110, width=240)
                self.combo_ssq.current(0)
                # security answer
                sqa = Label(self.root2, text="Security Answer",
                            font=("times new roman", 15, "bold"), bg="white")
                sqa.place(x=50, y=150)
                self.sqa = ttk.Entry(self.root2, font=(
                    "times new roman", 15, "bold"))
                self.sqa.place(x=50, y=180, width=240)

                # new password
                new_pass = Label(self.root2, text="New Password",
                                 font=("times new roman", 15, "bold"), bg="white")
                new_pass.place(x=50, y=220)
                self.new_pass = ttk.Entry(self.root2, font=(
                    "times new roman", 15, "bold"))
                self.new_pass.place(x=50, y=250, width=240)

                # reset button
                btn = Button(self.root2, command=self.reset_pass, text="Reset", font=(
                    "times new roman", 15, "bold"), fg="white", bg="green")
                btn.place(x=120, y=320)


# seperate
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("New User Registeration")
        self.root.geometry("{width}x{height}+0+0".format(width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight()))

        width_complete=self.root.winfo_screenwidth()
        height_complete=self.root.winfo_screenheight()
        half_width=width_complete//2

        # text variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_secq=StringVar()
        self.var_seca=StringVar()
        self.var_pass=StringVar()
        self.var_cnfpass=StringVar()


        bg_image=Image.open("images/registeration_bg.png")
        bg_image=bg_image.resize((width_complete,height_complete),Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_image)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        register_left=Image.open("images/register_left.jpg")
        register_left=register_left.resize((width_complete//3-100,height_complete//2+250),Image.LANCZOS)
        self.register_left = ImageTk.PhotoImage(register_left)
        register_left_lbl = Label(self.root, image=self.register_left)
        register_left_lbl.place(x=width_complete//3-200, y=100, width=width_complete//3-100, height=height_complete//2+150)

        frame = Frame(self.root, bg="white")
        frame.place(x=width_complete//3-200+width_complete//3-100, y=100, width=width_complete//3-50, height=height_complete//2+150)

        register_lbl_right = Label(frame, text="REGISTER HERE", font=(
            "times new roman", 18, "bold"), fg="black", bg="white")
        register_lbl_right.place(x=105, y=50)

        # label and entry
        fname=Label(frame,text="First Name : ",font=(
            "times new roman", 12, "bold"), fg="black",bg="white")
        fname.place(x=70,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=(
            "times new roman", 12, "bold"))
        fname_entry.place(x=220,y=100)

        lname=Label(frame,text="Last Name : ",font=(
            "times new roman", 12, "bold"), fg="black",bg="white")
        lname.place(x=70,y=150)

        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=(
            "times new roman", 12, "bold"))
        lname_entry.place(x=220,y=150)

        mob_num=Label(frame,text="Mobile Num : ",font=(
            "times new roman", 12, "bold"), fg="black",bg="white")
        mob_num.place(x=70,y=200)

        mob_num_entry=ttk.Entry(frame,textvariable=self.var_contact,font=(
            "times new roman", 12, "bold"))
        mob_num_entry.place(x=220,y=200)

        mail=Label(frame,text="E-mail : ",font=(
            "times new roman", 12, "bold"), fg="black",bg="white")
        mail.place(x=70,y=250)

        mail_entry=ttk.Entry(frame,textvariable=self.var_email,font=(
            "times new roman", 12, "bold"))
        mail_entry.place(x=220,y=250)

        security_qs=Label(frame,text="Security Qs : ",font=(
            "times new roman", 12, "bold"), fg="black",bg="white")
        security_qs.place(x=70,y=300)

        self.combo_sec_qs=ttk.Combobox(frame,textvariable=self.var_secq,font=(
            "times new roman", 12, "bold"),state="readonly")
        self.combo_sec_qs["values"]=("Select","Birth Month","Bestfriend","Sport","Subject")
        self.combo_sec_qs.current(0)
        self.combo_sec_qs.place(x=200,y=300)

        sec_ans=Label(frame,text="Security Ans : ",font=(
            "times new roman", 12, "bold"), fg="black",bg="white")
        sec_ans.place(x=70,y=350)

        sec_ans_entry=ttk.Entry(frame,textvariable=self.var_seca,font=(
            "times new roman", 12, "bold"))
        sec_ans_entry.place(x=220,y=350)
        
        password=Label(frame,text="Password : ",font=(
            "times new roman", 12, "bold"), fg="black",bg="white")
        password.place(x=70,y=400)

        password_entry=ttk.Entry(frame,textvariable=self.var_pass,font=(
            "times new roman", 12, "bold"))
        password_entry.place(x=220,y=400)

        cnf_password=Label(frame,text="Confirm Password : ",font=(
            "times new roman", 12, "bold"), fg="black",bg="white")
        cnf_password.place(x=70,y=450)

        cnf_password_entry=ttk.Entry(frame,textvariable=self.var_cnfpass,font=(
            "times new roman", 12, "bold"))
        cnf_password_entry.place(x=220,y=450)

        # buttons
        register_img=Image.open("images/register_form.png")
        register_img=register_img.resize((200,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(register_img)
        register_bttn=Button(frame,command=self.register_data,image=self.photoimage,borderwidth=0,cursor="hand2",font=(
            "times new roman", 12, "bold"))
        register_bttn.place(x=50,y=500)

        login_img=Image.open("images/login_form.png")
        login_img=login_img.resize((200,50),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(login_img)
        login_bttn=Button(frame,command=self.return_login,image=self.photoimage1,borderwidth=0,cursor="hand2",font=(
            "times new roman", 12, "bold"))
        login_bttn.place(x=250,y=500)
    
    # Fucntion declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_secq.get()=="Select" or self.var_seca.get()=="":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
            return
        if len(self.var_pass.get())>=8:
            if self.var_pass.get()!=self.var_cnfpass.get():
                messagebox.showerror("Error","Password and Confirm Password are not same!",parent=self.root)
                return
            else:
                conn=mysql.connector.connect(host="localhost",user="root",password="@INDIA12tnb",database="face_recognizer")
                cur=conn.cursor()
                query=("select * from register_details where Email=%s")
                value=(self.var_email.get(),)
                cur.execute(query,value)
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User Already exist, Please Login!",parent=self.root)
                    return
                else:
                    cur.execute("insert into register_details values(%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_secq.get(),
                        self.var_seca.get(),
                        self.var_pass.get()
                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registeration Successfull",parent=self.root)
        else:
            messagebox.showerror("Error","Password Length must be greater than or equal to 8!",parent=self.root)
            return
    
    def return_login(self):
        self.root.destroy()

# main project
if __name__ == "__main__":
    main()