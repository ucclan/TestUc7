# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 17:27:55 2023

@author: Sreenivas
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import os
import webbrowser

root = Tk()
root.title("HTML IDE")
root.minsize(650, 650)
root.maxsize(650, 650)
root.configure(background="yellow")

Run = ImageTk.PhotoImage(Image.open("run.jpg"))
Open = ImageTk.PhotoImage(Image.open("open.png"))
Save = ImageTk.PhotoImage(Image.open("save.png"))
Exit = ImageTk.PhotoImage(Image.open("exit.jpg"))

file_name_display = Label(root, text="File Name: ")
file_name_display.place(relx=0.28,rely=0.03,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03,anchor= CENTER)

my_text= Text(root,height=35,width=80,fg="black")
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)

name = ""
def openFile():
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0, END)
    html_file = filedialog.askopenfilename(title="Open Html File", filetypes=(("html Files", "*.html"),))
    print(html_file)
    name = os.path.basename(html_file)
    formatted_name = name.split('.')[0]
    input_file_name.insert(END, formatted_name)
    root.title(formatted_name)
    html_file = open(name, 'r')
    paragraph = html_file.read()
    my_text.insert(END, paragraph)
    
def save():
    input_name = input_file_name.get()
    file = open(input_name + ".html", "w")
    data = my_text.get(1.0, END)
    print(data)
    file.write(data)
    input_file_name.delete(0, END)
    my_text.delete(1.0, END)
    messagebox.showinfo("Update", "Success!")

def run_html_file():
    global name
    webbrowser.open(name)
open_button = Button(root, image=Open, command=openFile)
open_button.place(relx=0.05, rely=0.03)
save_button = Button(root, image=Save, command=save)
save_button.place(relx=0.11, rely=0.03)
run_button = Button(root, image=Run, command=run_html_file)
run_button.place(relx=0.17, rely=0.03)

root.mainloop()