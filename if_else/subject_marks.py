phy=int(input("enter phy marks: "))
che=int(input("enter che marks: "))
bio=int(input("enter bio marks: "))
mat=int(input("enter mat marks: "))
com=int(input("enter com marks: "))
total=phy+che+bio+mat+com
per=(total/500)*100
if per>=90:
    print("you have got GRADE A")
elif per>=80:
    print("you have got GRADE B")
elif per>=70:
    print("you have got GRADE C")
elif per>=60:
    print("you have got GRADE D")
elif per>=40:
    print("you have got GRADE E")
else:
    print("you have got GRADE F")
