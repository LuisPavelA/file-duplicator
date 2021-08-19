import shutil
import datetime 
import time
from tkinter import *
import pyglet, os

pyglet.font.add_file('Anton-Regular.ttf')  # Your TTF file name here

background = "#202124"
lyorange = "#fac00c"
error_text = ""
# Congifuration

root = Tk()
root.geometry('400x650') 
root.title("File Duplicator")
root.resizable(False, True)
root.wm_iconbitmap("Luis.ico")
root.configure(bg=background)

# Title

title = Label(root, text="File Duplicator", bg=background, foreground=lyorange, font=("Anton", 34))
title.pack()

# Name

file_name_title = Label(root, text="File Name (without extension)", bg=background, foreground=lyorange, font=("Anton", 18), pady=12)
file_name_title.pack()

file_name_input = Entry(root, bg=background, foreground=lyorange, font=("Anton", 15), highlightthickness=2, highlightbackground = lyorange, highlightcolor= lyorange)
file_name_input.pack()

# Extension

file_extension_title = Label(root, text="File extension (without dot)", bg=background, foreground=lyorange, font=("Anton", 18), pady=12)
file_extension_title.pack()

file_extension_input = Entry(root, bg=background, foreground=lyorange, font=("Anton", 15), highlightthickness=2, highlightbackground = lyorange, highlightcolor= lyorange)
file_extension_input.pack()

# Extension

copies_title = Label(root, text="Copies", bg=background, foreground=lyorange, font=("Anton", 18), pady=12)
copies_title.pack()

copies_input = Entry(root, bg=background, foreground=lyorange, font=("Anton", 15), highlightthickness=2, highlightbackground = lyorange, highlightcolor= lyorange)
copies_input.pack()

# Duplication Function

def duplication():
    file_name = file_name_input.get()
    file_extension = file_extension_input.get()
    
    number_of_copies = copies_input.get()

    tic = time.perf_counter()
    
    # For Loop
    for i in range(0, int(number_of_copies)):
        i += 1
        shutil.copy(f'{file_name}.{file_extension}', f'{file_name}{i}.{file_extension}')
    
    toc = time.perf_counter()
    global error_label
    error_label.configure(text=f"{number_of_copies} copies of {file_name}.{file_extension} were created! Check Logs.txt for more info.")
    # Logs
    f = open("Logs.txt", "a")
    f.write(f"- [{datetime.datetime.now()}] {number_of_copies} copies of {file_name}.{file_extension} were created.\n- {number_of_copies} files created in {toc-tic} seconds.\n\n")
    f.close()

# Error / Message

error_label = Label(root, text=error_text, bg=background, foreground=lyorange, font=("Anton", 15), pady=12, wraplength=300)
error_label.pack()

# Button

button = Button(root, command=duplication, text="Duplicate", bg=background, foreground=lyorange, font=("Anton", 18), highlightthickness=2, highlightbackground = lyorange, highlightcolor= lyorange)
button.pack()

root.mainloop()
