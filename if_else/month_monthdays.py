month=input("enter month ")
if month=="FEBRUARY":
    print("it has 28/29 days")
elif month in ("APRIL", "JUNE", "SEPTEMBER", "NOVEMBER"):
    print("it has 30 days")
elif month in ("JANUARY", "MARCH", "MAY", "JULY", "AUGUST", "OCTOBER", "DECEMBER"):
    print("it has 31 days")
