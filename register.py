from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter as tk
from tkinter import ttk

root = Tk()
root.geometry('1920x1080')
root.title('Liqour')
root.configure(bg='#EEEBEB')
root.state('zoomed')

box = tk.Frame(root, width=500, height=600, bg='#FFFFFF')
box.place(relx=0.5, rely=0.5, anchor='center')

register = Label(root, text='REGISTER', font=('Montserrat Black', 30), bg='#FFFFFF')
register.place(relx=0.5, y=90, anchor='center')

first_name = Label(root, text='First name', font=('Montserrat', 12), fg='#413F3F', bg='#FFFFFF')
first_name.place(relx=0.355, y=140)
first_name_entry = Entry(root, width=10, font=('Montserrat Light', 16), bg='#fdfdfd')
first_name_entry.place(relx=0.409, y=180, anchor='center')

second_name = Label(root, text='Second name', font=('Montserrat', 12), fg='#413F3F', bg='#FFFFFF')
second_name.place(relx=0.515, y=140)
second_name_entry = Entry(root, width=10, font=('Montserrat Light', 16), bg='#fdfdfd')
second_name_entry.place(relx=0.57, y=180, anchor='center')

email = Label(root, text='Email', font=('Montserrat', 12), fg='#413F3F', bg='#FFFFFF')
email.place(relx=0.355, y=230)
email_entry = Entry(root, width=26, font=('Montserrat Light', 16), bg='#fdfdfd')
email_entry.place(relx=0.49, y=270, anchor='center')

role = Label(root, text='Role', font=('Montserrat', 12), fg='#413F3F', bg='#FFFFFF')
role.place(relx=0.355, y=320)
clicked = tk.StringVar()

role_menu = ttk.Combobox(root, textvariable=clicked, values=['Admin', 'User'], font=('Montserrat Light', 16), width=25, state='readonly')
role_menu.place(relx=0.49, y=360, anchor='center')

def password_visibility():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        hide_button.config(text='Show', font=('Montserrat Light', 10))
    else:
        password_entry.config(show='')
        hide_button.config(text='Hide', font=('Montserrat Light', 10))

password = Label(root, text='Password', font=('Montserrat', 12), fg='#413F3F', bg='#FFFFFF')
password.place(relx=0.355, y=410)
password_entry = Entry(root, width=26, font=('Montserrat Light', 16), bg='#fdfdfd')
password_entry.place(relx=0.49, y=450, anchor='center')

hide_button = tk.Button(root, text='Hide', font=('Montserrat Light', 10), height=1, width= 4, command = password_visibility, bg='#FFFFFF')
hide_button.place(relx=0.593, y=435)

def confirm_password_visibility():
    if confirm_password_entry.cget('show') == '':
        confirm_password_entry.config(show='*')
        hide_button2.config(text='Show', font=('Montserrat Light', 10))
    else:
        confirm_password_entry.config(show='')
        hide_button2.config(text='Hide', font=('Montserrat Light', 10))

confirm_password = Label(root, text='Confirm password', font=('Montserrat', 12), fg='#413F3F', bg='#FFFFFF')
confirm_password.place(relx=0.355, y=500)
confirm_password_entry = Entry(root, width=26, font=('Montserrat Light', 16), bg='#fdfdfd')
confirm_password_entry.place(relx=0.49, y=540, anchor='center')

hide_button2 = tk.Button(root, text='Hide', font=('Montserrat Light', 10), height=1, width= 4, command = confirm_password_visibility, bg='#FFFFFF')
hide_button2.place(relx=0.593, y=525)

login_button = Button(root, width=26, text='Create my account', font=('Montserrat', 12), fg='#FFFFFF', bg='black')
login_button.place(relx=0.49, y=610, anchor='center')

root.mainloop()