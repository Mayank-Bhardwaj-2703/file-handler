import os
import glob
import tkinter as tk
from tkinter import filedialog
from tkinter import *


top=tk.Tk()
top.geometry('1200x700')
top.title('File Sort....X')
top.configure(background='#2F4F4F')
label=Label(top,background='#2F4F4F', font=('georgia',20,'bold'))
sign_image = Label(top)

def create_fresh_directories():

    files_list = glob.glob("*")

    extension_set = set()

    for file in files_list:
        extension = file.split(sep=".")
        try:
            extension_set.add(extension[1])
        except IndexError:
            continue


    def createDirs():
        for dir in extension_set:
            try:
                os.makedirs(dir+"_files")
            except FileExistsError:
                continue

 
    def arrange():
        for file in files_list:
            fextension = file.split(sep=".")
            try:
                os.rename(file, fextension[1]+"_files/"+file)
                print('success....!')
            except (OSError, IndexError):
                continue

    createDirs()
    arrange()

upload=Button(top,text="create directories for scattered files",command=create_fresh_directories,padx=10,pady=10)
upload.configure(background='#FEBD07', foreground='#2F4F4F',font=('georgia',15,'bold'))
upload.pack(side=BOTTOM,pady=50)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="scattered directories sorted",pady=20, font=('georgia',30,'bold'))
heading.configure(background='#2F4F4F',foreground='#FFD700')
heading.pack()

top.mainloop()

