N = int(input("number of year: "))
X = float(input("washing machine: "))
P = float(input("number of dollar: "))

toy = 0
save = 0

for i in range(N):
    age = i + 1
    if age % 2 == 0:
        money = (age /2 ) * 10
        save = save + (money - 1)
    else:
        toy += 1
    
total = save + P*toy
left =total-X

if left < 0:
    print(f"No! you still need {abs(left):.2f}")
else:
    print(f"Yes! you still have {left:.2f} left")    