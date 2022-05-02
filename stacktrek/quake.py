quake = float(input("QUAKE:"))

if quake < 2.0:    
    print("Micro")

elif quake < 2.0:
    print("Very minor")

elif quake < 4.0:
    print("Minor")

elif quake < 5.0:
    print("Light")

elif quake < 6.0:
    print("Moderate")

elif quake < 7.0:
    print("Strong")

elif quake < 8.0:
    print("Major")

elif quake < 10.0:
    print("Great")

else:
    print("Meteoric")