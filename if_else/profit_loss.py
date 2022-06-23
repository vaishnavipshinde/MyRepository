cp=float(input("enter the cost price: "))
sp=float(input("enter the sell price: "))
if cp==sp:
    print("no profit no loss")
elif sp>cp:
    print("profit of ", sp-cp)
else:
    print("loss of ",cp-sp)