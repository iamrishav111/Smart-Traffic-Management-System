from PIL import Image, ImageTk
from tkinter import Tk, BOTH,X,Toplevel
from tkinter.ttk import Frame, Label, Style,Progressbar
import time
width=300
height=200


class Traffic(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.title("Traffic")
        self.configure(background="#f0eec5")
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.initUI(1, 1, 1, 1)
        for i in range(1, 3):
            for j in range(1, 10):
                self.initUI(i, j, (j - 1) % 3 + 1, (j - 1) // 3 + 1)
            time.sleep(3)

    def initUI(self,path,pic,xi,yi):
        stgImg=Image.open(str((path-1)*5)+"//"+str(pic)+".jpg")
        # paths="/home/iamrishav/PycharmProjects/HelloWorld/0"
        stgImg=stgImg.resize((width,height),Image.ANTIALIAS)
        stgImg2=ImageTk.PhotoImage(stgImg)
        # frame=Frame(master,height=800)
        # frame.pack(fill=X)
        label=Label(self, image=stgImg2)
        label.image = stgImg2
        label.place(x=543*xi-495.5,y=288*yi-269)
        label1=Label(self)
        progress=Progressbar(label1,length=200,mode='determinate')
        progress['value']=path*33
        fn=str(path*33)
        label2=Label(self,text=fn,font="arial 12 bold",background="yellow")

        label2.place(x=543*xi-240.5,y=288*yi-49)

        progress.pack()
        label1.place(x=543*xi-495.5,y=288*yi-49)
        self.update_idletasks()


# root = Tk()
# root.title("Traffic")
# root.configure(background="#f0eec5")
# root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
# initUI(root,1,1,1,1)
# for i in range(1,3):
#     for j in range(1,10):
#         initUI(root,i,j,(j-1)%3 +1,(j-1)//3 +1)
#     time.sleep(3)
# root.mainloop()