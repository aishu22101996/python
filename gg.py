from tkinter import*
top=Tk()
top.geometry("400x500")
def Sum():
    res=int(e1.get())+int(e2.get())
    myText.set(res)
myText=StringVar()
Label(top,text="First").grid(row=0,sticky=W)
Label(top,text="Second").grid(row=1,sticky=W)
Label(top,text="Result").grid(row=3,sticky=W)
result=Label(top,text="",textvariable=myText).grid(row=3,pady=1,sticky=W)
e1=Entry(top)
e2=Entry(top)
e1.grid(row=0,pady=1)
e2.grid(row=1,pady=1)
def Sub():
    res=int(e1.get())-int(e2.get())
    myText.set(res)
def Mul():
    res=int(e1.get())*int(e2.get())
    myText.set(res)
def Div():
    res=int(e1.get())/int(e2.get())
    myText.set(res)
def Clr():
    e1.delete(0,END)
    e2.delete(0,END)   
menubar=Menu(top)
Calculation=Menu(menubar,tearoff=0)
Calculation.add_command(label="Summation",command=Sum)
Calculation.add_command(label="Subtration",command=Sub)
Calculation.add_command(label="multiplication",command=Mul)
Calculation.add_command(label="Division",command=Div)
Calculation.add_command(label="Clear",command=Clr)
menubar.add_cascade(label="Calculation",menu=Calculation)
top.config(menu=menubar)
top.mainloop()                    