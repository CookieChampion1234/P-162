from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import webbrowser

root = Tk()
root.title("HTML Editor")
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background = "#d4fcf2")

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
run_img = ImageTk.PhotoImage(Image.open("run.png"))

label_file_name = Label(root, text = "File Name: ")
label_file_name.place(relx = 0.28, rely = 0.03, anchor = CENTER)

input_file_name = Entry(root)
input_file_name.place(relx = 0.46, rely = 0.03, anchor = CENTER)

my_text = Text(root, height = 30, width = 60, bg = "#cccaca")
my_text.place(relx = 0.5, rely = 0.55, anchor = CENTER)

name = ""
def open_file():
    global name
    input_file_name.delete(0, END)
    my_text.delete(1.0, END)
    html_file = filedialog.askopenfilename(title = "Open html File", filetypes = (("html Files", "*.html"),))
    print(html_file)
    name = os.path.basename(html_file)
    formatted_name = name.split('.') [0]
    input_file_name.insert(END, formatted_name)
    root.title(formatted_name)
    html_file = open(name, 'r')
    paragraph = html_file.read()
    my_text.insert(END, paragraph)
    html_file.close()
    
def save_file():
    input_name = input_file_name.get()
    file = open(input_name + ".html", 'w')
    data = my_text.get(1.0, END)
    print(data)
    file.write(data)
    input_file_name.delete(0, END)
    my_text.delete(1.0, END)
    messagebox.showinfo("Update", "Success")
    
def run_file():
    global name
    webbrowser.open(name)
    
open_btn = Button(root, image = open_img, command = open_file)
open_btn.place(relx = 0.05, rely = 0.03, anchor = CENTER) 
save_btn = Button(root, image = save_img, command = save_file)
save_btn.place(relx = 0.11, rely = 0.03, anchor = CENTER) 
run_btn = Button(root, image = run_img, command = run_file)
run_btn.place(relx = 0.17, rely = 0.03, anchor = CENTER) 

root.mainloop()