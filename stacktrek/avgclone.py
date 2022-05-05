num = int(input("Enter a number: "))
if num == 0:
    print("No entries")
    exit()
else:
    test = True

x = 2
avg = num

while test:
    num1 = int(input("Enter a number: "))
    num = num + num1

    if num1 == 0:
        test = False
    else:
        x += 1
        avg = num / x
        test = True
    
print(avg)