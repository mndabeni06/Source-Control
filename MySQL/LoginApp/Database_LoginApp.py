from tkinter import *
import mysql.connector
from tkinter import messagebox

root = Tk()

root.config(bg="goldenrod")


class Database:
    def __init__(self, master):
        self.root = root
        self.root.title('DataBase_LoginApp')
        self.root.geometry("500x360")

        self.username = Label(master, text="Please Enter Username", borderwidth=5)
        self.username.place(x=5, y=5)
        self.username_entry = Entry(master, borderwidth=5)
        self.username_entry.place(x=200, y=5)

        self.password = Label(master, text="Please Enter password", borderwidth=5)
        self.password.place(x=5, y=50)
        self.password_entry = Entry(master, borderwidth=5)
        self.password_entry.place(x=200, y=50)

        self.login_btn = Button(master, text="Login", borderwidth=5, command=self.login)
        self.login_btn.place(x=10, y=200)

        self.register_user_btn = Button(master, text="Register New User", borderwidth=5, command=self.register)
        self.register_user_btn.place(x=200, y=200)



    def login(self):

        hospital = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='hospital',
                              auth_plugin='mysql_native_password')
        mycursor=hospital.cursor()
        xy=mycursor.execute('Select * from Login')
        for x in mycursor:
            if x[1] == self.password_entry.get() and x[0] == self.username_entry.get():
                messagebox.showinfo("PERMISSION", "LOGIN SUCCESSFUL")
                root.destroy()
        if x[1] != self.password_entry.get() or x[0] != self.username_entry.get():
                    messagebox.showerror("STATUS", "ACCESS DENIED")
                    self.username_entry.delete(0, END)
                    self.password_entry.delete(0, END)

    def register(self):
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='hospital',
                              auth_plugin='mysql_native_password')

        mycursor = mydb.cursor()
        sql = "INSERT INTO Login (user, password) VALUE (%s, %s)"
        val = (self.username_entry.get(), self.password_entry.get())
        mycursor.execute(sql, val)
        messagebox.showinfo("PERMISSION", "YOU HAVE REGISTERED SUCCESSFULLY")
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        mydb.commit()








Y = Database(root)
root.mainloop()
