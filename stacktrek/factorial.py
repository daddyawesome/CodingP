num = int(input("Enter a number: "))
fc = num

while num > 1:
    num -= 1
    fc = fc * num

print(fc)