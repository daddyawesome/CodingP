test = True
c = 0
n = 0
m = 0
seniors = 0
while test:
    xy = input("Enter age: ")
    if xy == "end":
        test = False
        continue

    num = float(xy)
    
    if  num <= 2:
        c += 1

    elif  num > 2 and num <= 12:
        n += 1
        
    elif num >= 65:
        seniors += 1
        
    else:
        m += 1
        
cost = c * 0 + n * 14 + seniors * 18 + m * 23

print(f"{cost:.1f}")
