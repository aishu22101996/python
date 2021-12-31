mal=int(input("enter first subject mark:"))
eng=int(input("enter second subject mark:"))
mat=int(input("enter third subject mark:"))
cs=int(input("enter forth subject mark:"))
tot=mal+eng+mat+cs
avrg=tot/4
per=tot*100/400
print("total:",tot)
print("average:",avrg)
print("percentage:",per)
if per>=80:
    print("A grade")
elif per>=60:
    print("B grade")
elif per>=40:
    print("C grade")
elif per>=20:
    print("D grade")
else:
    print("Failed")                 