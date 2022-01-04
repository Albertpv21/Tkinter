from tkinter import *
klik=0
def klikker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)
def klikker_minus(event):
    global klik
    klik-=1
    lbl.configure(text=klik)
    if klik==-100:
        klik=0
def txt_to_lbl(event):
   text_to_lbl=txt.get() #From Entry to text pass
   lbl.configure(text=text_to_lbl)
   txt.delete(0,END)
def valik():
    valik_=var.get()
    lbl.configure(text=valik_)
    txt.insert(0,valik_)
def geometry(event):
    geometry(str(aken_width()+10)+"x"+str(aken_height()+10))


    


        
       
aken=Tk()
aken.title("Akna nimetus")
aken.geometry("500x600")
nupp=Button(aken,text="Mina olen nupp\nValjuta mind!",font="Arial 20",fg="red",bg="lightblue",height=4,width=20,relief=GROOVE)#relief RAISED,SUNKEN
nupp.bind("<Button-1>",klikker)#LKM
nupp.bind("<Button-3>",klikker_minus)#PKM
nupp.bind("<Button-2>",geometry)
lbl=Label(aken,text="...",height=4,width=20,font="Arial 20",fg="yellow",bg="blue")
txt=Entry(aken,width=20,font="Arial 20",fg="black",bg="green",justify=CENTER)
txt.bind("<Return>",txt_to_lbl)#Enter
i1=PhotoImage(file="31313.png")
i2=PhotoImage(file="gggg.png")
i3=PhotoImage(file="s.png")
var=StringVar()
var.set("Üks")
r1=Radiobutton(aken,image=i1,variable=var,value="Üks",command=valik)
r2=Radiobutton(aken,image=i2,variable=var,value="Kaks",command=valik)
r3=Radiobutton(aken,image=i3,variable=var,value="Kolm",command=valik)





r=Radiobutton(aken,)
r1.pack(side=TOP)
r2.pack(side=TOP)
r3.pack(side=TOP)




lbl.pack()
nupp.pack()#side=LEFT,TOP,RIGHT
txt.pack()

aken.mainloop()
