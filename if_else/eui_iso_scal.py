x=int(input("x: "))
y=int(input("y: "))
z=int(input("z: "))
if x==y==z:
    print("triangle is equilateral ")
elif x==y or y==z or x==z:
    print("triangle is isosceles ")
else:
    print("tinagle is scalene ")
    