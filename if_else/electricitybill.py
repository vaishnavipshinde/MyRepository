unit=int(input("enter electricity unit charges: "))
if unit<=50:
    unit=unit*0.50
    bill=unit+(20/100)
    print(bill)
elif unit>=50 & unit<=100:
    unit=unit*0.75
    bill=unit+(20/100)
    print(bill)
elif unit>=100 & unit<=250:
    unit=unit*1.20
    bill=unit+(20/100)
    print(bill)
else:
    unit=unit*1.50
    bill=unit+(20/100)
    print(bill)
