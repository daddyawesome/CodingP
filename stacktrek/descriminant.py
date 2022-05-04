import math

a = float(input("a = "))
if a == 0:
    print("a cannot be zero")
    exit()

b = float(input("b = "))
c = float(input("c = "))

NoSol = b**2 - 4*a*c

if NoSol < 0:
    print("There are no solutions")
elif NoSol > 0:
    sol1 = (-b + math.sqrt(NoSol))/(2*a)
    sol2 = (-b - math.sqrt(NoSol))/(2*a)
    print(f"There are two solutions , namely {sol1} and {sol2}")
else:
    sol = -c/b
    print(f"There is only one solution , {sol}")
