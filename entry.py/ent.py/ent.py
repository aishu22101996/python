from tkinter import*
top=Tk()
top.geometry("400*250")
name=Label(top),text="Name").place(x=50,y=30)
email=Label(top,text="Email").place(x=50,y=60)
password=Label(top,text="Password").place(x=50,y=90)
b1=Button(top,text="Submit",active bg="Pink",active fg="Blue").place(x=120,y=120)
e1=Entry(top).place(x=120,y=30)
e2=Entry(top).place(x=120,y=60)
e3=Entry(top).place(x=120,y=90)
top.mainloop()