from turtle import*
clear()
pensize(3)
clr=["blue","green","yellow","orange","red","purple"]
for i in clr:
    rt(60)
    color("black",i)
    begin_fill()
    for j in range(4):
        fd(100)
        rt(90)
        end_fill()