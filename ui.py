from tkinter import Button

def create_button(master, text, command):
    btn = Button(master=master, text=text, command=command)
    return btn