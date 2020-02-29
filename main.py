import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Tk, BOTH,X
from traffic import  Traffic
from tkinter.ttk import Frame, Label, Style,Progressbar
import time
width=300
height=200

from past.builtins import execfile


# from tk import *

from tkinter import Label,Entry,Frame,Button,X
class Application(object):
    def __init__(self, master):
        self.master = master

        self.topFrame = Frame(master, height=200, bg="white")
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(master, height=600, bg="#f0eec5")
        self.bottomFrame.pack(fill=X)
        self.label1 = Label(self.topFrame, text="CENTRALLISED TRAFFIC MANAGEMENT", font="arial 33 bold", bg="white",
                            fg="blue")
        self.label1.place(x=250, y=50)

        self.name = Label(self.bottomFrame, text="NAME", font="arial", bg="#f0eec5", fg="black")
        self.name.place(x=450, y=120)
        self.entry_name = Entry(self.bottomFrame)
        self.entry_name.place(x=550, y=122, width=120, height=20)
        self.entry_pwd = Entry(self.bottomFrame,show="*",width=120)
        self.entry_pwd.place(x=550, y=150, width=120, height=20)
        self.password = Label(self.bottomFrame, text="PASSWORD", font="arial", bg="#f0eec5", fg="black")
        self.password.place(x=450, y=150)
        self.button_register = Button(self.bottomFrame, text="ENTER", font="arial 16 bold ", fg="red",command=self.getThere)
        self.button_register.place(x=540, y=200)

    def getThere(self):
        # execfile('traffic.py')
        there=Traffic()

# class newWindow(object):
#     def __init__(self, master):
#         object.__init__(self)
#         w, h = object.winfo_screenwidth(), object.winfo_screenheight()
#         object.geometry("%dx%d+0+0" % (w, h))
#         object.mainloop()
#         w, h = object.winfo_screenwidth(), object.winfo_screenheight()


def main(master):
    app = Application(master)

    master.title("My First GUI")
    #     w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    #     root.geometry("%dx%d+0+0" % (w, h))

    master.geometry('1000x500')

    master.mainloop()


root=tk.Tk()
main(root)