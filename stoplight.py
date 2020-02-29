# import tkinter as tk
# from tkinter import Label
# import time
# from PIL import Image, ImageTk
# def initUI(path,pic,xi,yi):
#     stgImg=Image.open("C://Users//chira//OneDrive//Desktop//"+str((path-1)*5)+"//"+str(pic)+".jpg")
#
#     stgImg=stgImg.resize((400,200),Image.ANTIALIAS)
#     stgImg2=ImageTk.PhotoImage(stgImg)
#     label=Label(root, image=stgImg2)
#     label.image = stgImg2
#     label.place(x=543*xi-496.5,y=288*yi-269)
#     root.update_idletasks()
#
#
# root=tk.Tk()
# root.title("Portal")
# w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# root.geometry("%dx%d+0+0" % (w, h))
# initUI(1,1,1,1)
# for i in range(1,4):
#     for j in range(1,10):
#         initUI(i,j,(j-1)%3 +1,(j-1)//3 +1)
#     time.sleep(3)
#
#
# root.mainloop()
























# from tkinter import Tk,Frame,Radiobutton,Canvas,StringVar
#
# class TrafficLights:
#
#     def __init__(self):
#
#         window = Tk()
#         window.title("Traffic Light")
#
#         frame = Frame(window)
#         frame.pack()
#
#         self.color = StringVar()
#
#         radio_red = Radiobutton(frame, text="Red", bg="red", variable=self.color, value="R", command=self.on_RadioChange)
#         radio_red.grid(row=10, column=1)
#
#         radio_yellow = Radiobutton(frame, text="Yellow", bg="yellow", variable=self.color, value="Y", command=self.on_RadioChange)
#         radio_yellow.grid(row = 10, column = 2)
#
#         radio_green = Radiobutton(frame, text="Green", bg="green", variable=self.color, value="G", command=self.on_RadioChange)
#         radio_green.grid(row = 10, column = 3)
#
#         self.canvas = Canvas(window, width=450, height=300, bg="white")
#         self.canvas.pack()
#
#         self.oval_red = self.canvas.create_oval(10, 10, 110, 110, fill="white")
#         self.oval_yellow = self.canvas.create_oval(120, 10, 220, 110, fill="white")
#         self.oval_green = self.canvas.create_oval(230, 10, 330, 110, fill="white")
#
#         self.color.set('R')
#         self.canvas.itemconfig(self.oval_red, fill="red")
#
#         window.mainloop()
#
#     def on_RadioChange(self):
#         color = self.color.get()
#
#         if color == 'R':
#             self.canvas.itemconfig(self.oval_red, fill="red")
#             self.canvas.itemconfig(self.oval_yellow, fill="white")
#             self.canvas.itemconfig(self.oval_green, fill="white")
#         elif color == 'Y':
#             self.canvas.itemconfig(self.oval_red, fill="white")
#             self.canvas.itemconfig(self.oval_yellow, fill="yellow")
#             self.canvas.itemconfig(self.oval_green, fill="white")
#         elif color == 'G':
#             self.canvas.itemconfig(self.oval_red, fill="white")
#             self.canvas.itemconfig(self.oval_yellow, fill="white")
#             self.canvas.itemconfig(self.oval_green, fill="green")
#
#
# TrafficLights()




import tkinter as tk
from tkinter.font import *

class traffic_signal:
  def __init__(self,name,C,offset):
    self.name = name # name used as a label over the top of the signal
    self.C = C # canvas to draw on
    self.offset = offset # position left to right for this instance to draw its light
    name_font = Font(family="Helvetica",size=20, weight="bold")
    C.create_text(offset+50,15,font=name_font,text=name)
    C.create_rectangle(offset+0,30,offset+100,370,fill="black")
    C.create_oval(offset+3,40,offset+100,140,fill="grey")
    C.create_oval(offset+3,150,offset+100,250,fill="grey")
    C.create_oval(offset+3,260,offset+100,360,fill="grey")
    self.redLight = self.C.create_oval(self.offset+3,40,self.offset+100,140,fill="red")
    self.yellowLight = self.C.create_oval(self.offset+3,150,self.offset+100,250,fill="yellow")
    self.greenLight = self.C.create_oval(self.offset+3,260,self.offset+100,360,fill="green")

  def setRed(self):
    self.redLight = self.C.create_oval(self.offset+3,40,self.offset+100,140,fill="red")

  def setYellow(self):
    self.yellowLight = self.C.create_oval(self.offset+3,150,self.offset+100,250,fill="yellow")

  def setGreen(self):
    self.greenLight = self.C.create_oval(self.offset+3,260,self.offset+100,360,fill="green")

  def clearAll(self):
    self.C.delete(self.redLight)
    self.C.delete(self.yellowLight)
    self.C.delete(self.greenLight)

# street_intersection controls a group of four traffic signals
# it also provides the top level logic and timer for the simulation
class street_intersection:
  def __init__(self,top):
    self.top = top # hold a window frame
    self.C = tk.Canvas(self.top, bg="white", height=370, width=430)
    self.light={} # hold four traffic signals
    self.light["North"] = traffic_signal("North",self.C,0)
    self.light["South"] = traffic_signal("South",self.C,110)
    self.light["East"] = traffic_signal("East",self.C,220)
    self.light["West"] = traffic_signal("West",self.C,330)
    self.C.pack()

    # Create a statemachine here

    self.C.after(0,self.timerExpire) #create first event in simulation
  def timerExpire(self) :
    # send an timer event to your statemachine here

    self.C.after(5000, self.timerExpire)  #create next event in simulation execute after 5 seconds

# start simulation
top = tk.Tk() # create a window frame
si = street_intersection(top) # construct intersection
top.mainloop() # start GUI



















