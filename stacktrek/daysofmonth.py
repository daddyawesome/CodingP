enter_month = int(input("Month Number:"))

modmonth = enter_month % 12

if modmonth == 1:
    print("31 days")
elif modmonth == 2:
    print("28 or 29 days")
elif modmonth == 3:
    print("31 days")
elif modmonth == 4:
    print("30 days")
elif modmonth == 5:
    print("31 days")
elif modmonth == 6:
    print("30 days")
elif modmonth == 7:
    print("31 days")
elif modmonth == 8:
    print("31 days")
elif modmonth == 9:
    print("30 days")
elif modmonth == 10:
    print("31 days")
elif modmonth == 11:
    print("30 days")
else: 
    print("31 days")