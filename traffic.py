from PIL import Image, ImageTk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style
import time
width=400
height=200



def initUI(path,pic,xi,yi):
    stgImg=Image.open("C://Users//chira//OneDrive//Desktop//"+str((path-1)*5)+"//"+str(pic)+".jpg")

    stgImg=stgImg.resize((width,height),Image.ANTIALIAS)
    stgImg2=ImageTk.PhotoImage(stgImg)
    label=Label(root, image=stgImg2)
    label.image = stgImg2
    label.place(x=543*xi-496.5,y=288*yi-269)
    root.update_idletasks()



root = Tk()
root.title("Traffic")
root.configure(background="white")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
initUI(1,1,1,1)
for i in range(1,4):
    for j in range(1,10):
        initUI(i,j,(j-1)%3 +1,(j-1)//3 +1)
    time.sleep(3)



root.mainloop()