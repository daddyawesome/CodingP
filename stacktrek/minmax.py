num = float(input("enter a number:"))
max = num
min = num
x = 0
if num % 3 == 0:
    x = 1

for i in range(9):
    
    num = float(input("enter a number:"))
    if num % 3 == 0:
        x += 1

    if num > max:
        max = num

    if num < min:
        min = num

print(f"Highest: {int(max)}\nLowest: {int(min)}\n{int(x)} numbers divisible by 3")