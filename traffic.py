from PIL import Image, ImageTk
from tkinter import Tk, BOTH,X,Toplevel
import tkinter.ttk as ttk
from tkinter.ttk import Frame, Label, Style,Progressbar
import time
import pandas
import numpy
import herepy
import json
width=400
height=250
def location(place):
    geocoderApi = herepy.GeocoderApi('fywUFbdwhP7YRn5SZI2A-ZJ7te444T2vt3X5GWnveAE')
    response = geocoderApi.free_form(place)
    s=json.loads(str(response))


    lat = s["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]["Latitude"]
    lng = s["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]["Longitude"]
    lat="{0:.2f}".format(lat)
    lng="{0:.2f}".format(lng)
    return '{'+lat+','+lng+'}'
d={1:"Big Ben  "+location("Big Ben"), 2:"Gariahat  "+location("Gariahat"),3:"Jadavpur  "+location("Jadavpur"),4:"Times Square  "+location("Times Square"),5:"Rasbehari  "+location("Rasbehari"),6:"Garia  "+location("Garia"),7:"Tollygunge  "+location("Tollygunge"),8:"Chingrihata  "+location("Chingrihata"),9:"Saltlake  "+location("Salt Lake")}



class Traffic(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.title("TRAFFIC MANAGEMENT SYSTEM")
        self.configure(background="white")
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.initUI(1, 1, 1, 1)
        for i in range(1, 3):
            for j in range(1, 10):
                self.initUI(i, j, (j - 1) % 3 + 1, (j - 1) // 3 + 1)
            time.sleep(5)

    def initUI(self,path,pic,xi,yi):
        stgImg=Image.open(str((path-1)*5)+"//"+str(pic)+".jpg")
        # paths="/home/iamrishav/PycharmProjects/HelloWorld/0"
        stgImg=stgImg.resize((width,height),Image.ANTIALIAS)
        stgImg2=ImageTk.PhotoImage(stgImg)
        # frame=Frame(master,height=800)
        # frame.pack(fill=X)
        data=pandas.read_csv("output"+str((path-1)*5)+".csv",header=None)
        var=data.to_numpy()
        label=Label(self, image=stgImg2)
        label.image = stgImg2
        label.place(x=543*xi-543+20,y=280*yi-300+10) #-269
        label1=Label(self)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
        progress=Progressbar(label1,style="red.Horizontal.TProgressbar",length=100,mode='determinate')
        progress['value']=int(var[pic-1][1]*20)
        fn=str(var[pic-1][1])+" mins"
        fn1=d[pic]
        #progress=Progressbar(label1,length=200,mode='determinate')
        #progress['value']=path*33
        #fn=str(path*33)
        label2=Label(self,text=fn,font="arial 12 bold",background="#f0d630")

        label2.place(x=543*xi-317-90,y=280*yi-50+17)

        label3=Label(self,text=fn1,font="arial 12 bold",background="white")

        label3.place(x=543*xi-235.5-90,y=280*yi-50+18)

        progress.pack()
        label1.place(x=543*xi-540+20,y=280*yi-50+18)
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
