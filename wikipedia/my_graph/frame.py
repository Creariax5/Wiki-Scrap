from tkinter import *


def create_frame():
    frame = Tk()
    frame.title("graphic visualiser")
    frame.geometry("600x400")
    frame.minsize(300, 300)
    frame.iconbitmap("img/logo.ico")
    frame.config(background="#232323")
    return frame


def create_cell(canvas):
    cell = canvas.create_oval(190, 365, 210, 385, fill='red', outline='red')
    return cell


def create_text(txt, frame, x, y):
    text = Label(frame, text=txt, font=("Courrier", 20), bg="#232323", foreground="#FFFFFF")
    text.place(relx=x, rely=y)
    text.pack()
    return text
