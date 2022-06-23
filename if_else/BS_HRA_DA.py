bs=float(input("Enter basic salary"))
if bs<=10000:
    DA = bs*0.8
    HRA = bs*0.2
    total = bs+DA+HRA
    print("total salary is", total)
elif bs<=20000:
    DA=bs*0.9
    HRA=bs*0.25
    total=bs+DA+HRA
    print("total salary is",total)
else:
    DA=bs*0.95
    HRA=bs*0.3
    total=bs+DA+HRA
    print("total salary is",total)