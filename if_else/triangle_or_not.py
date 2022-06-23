a=int(input("enter the 1st angle of triangle "))
b=int(input("enter the 2nd angle of triangle "))
c=int(input("enter the 3rd angle of triangle "))
total=a+b+c
if total==180:
    print("\nThis is a valid triangle")
else:
    print("\nThis is not valid triangle")