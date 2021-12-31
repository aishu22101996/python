from tkinter import*
top=Tk()
top.geometry("1200x1000")
labelframe=LabelFrame(top,text="calculator")
labelframe.pack(fill="both",expand="yes")
e1=Entry(labelframe)
e1.pack()
def press1():
    myText=StringVar()    
b1=Button(labelframe,text="1",command=press1)
b1.pack()
top.mainloop()