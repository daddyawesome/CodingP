m=int(input("M: "))
n=int(input("N: "))
p=int(input("P: "))

for i in range(m,n+1):
    powprint = i**2
    for j in range(3, p+1):
        pow= i ** j
        powprint = f"{powprint}, {pow}"
    print(powprint)

