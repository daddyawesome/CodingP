num = int(input("enter number: "))
male = 0
female = 0
i = 1

while i <= num:
    fm = input("m/f: ") 

    if fm == "F" or fm == "f":
        female += 1
    elif fm == "M" or fm == "m":
        male += 1
    else:
        print("Only choose m or f")
        exit()
    i += 1

if female == 0:
    print(f"Males: {male}\nFemales: {female}\nAll males")
elif male == 0:
    print(f"Males: {male}\nFemales: {female}\nAll females")
else:
    
    if male < female:
        d = male
    else:
        d = female

    test = True
    while test:
        n = male % d
        m = female % d
        if n== 0 and m == 0:
            test = False
        else:
            d -= 1
    
    ratio = f"{int(male/d)}:{int(female/d)}"
    print(f"Males: {male}\nFemales: {female}\n{ratio}")