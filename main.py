import tkinter as tk
from tkinter import messagebox as mb

root = tk.Tk()
root.geometry("600x400")

# for storing name and password
name_var = tk.StringVar()
passw_var = tk.StringVar()

# defining the login function
def login():
    name = name_var.get()
    password = passw_var.get()

    if (name == 'Bitspilani' and password == '12345'):
        mb.showinfo(message='Logged In Successfully')
    else:
        mb.showinfo(message='Incorrect Login ID/Password')

# creating a widget-labels
name_label = tk.Label(root, text='Username', font=('calibre', 10, 'bold'))

name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))

passw_label = tk.Label(root, text='Password', font=('calibre', 10, 'bold'))

passw_entry = tk.Entry(root, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')

# creating the login button
sub_btn = tk.Button(root, text='Login', command=login)

# placing the label in required position
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

# to display window
root.mainloop()