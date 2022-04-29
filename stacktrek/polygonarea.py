import math

n = int(input("number of sides: "))
l = float(input("the length of a side: "))
polygonarea = (l * (n**2)) / (4 * math.tan(math.pi / l))
polygonarea2 = (n * (l)) / (4 * math.tan(math.pi / l))
print(round(polygonarea,2))
print(polygonarea2)