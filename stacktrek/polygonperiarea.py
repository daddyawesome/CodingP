import math

test = True
x=[]
y=[]
n = 0
while test:
    xy = input("Enter a number: ")
    if xy == "stop":
        test = False
        continue

    num = float(xy)
    n += 1
    if  n % 2 == 0:
        y.append(num)
    else:
        x.append(num)

m = int(n/2)
distance = 0
area2 = 0

if m >= 3 and n % 2 ==0:
    for i in range(m):
        if (i+1) == m:
            distance =distance + math.sqrt((x[-1]-x[0])**2 + (y[-1]-y[0])**2)    
            area2 = area2 + ((x[-1]*y[0])- (y[-1]*x[0]))
        else:
            distance =distance + math.sqrt((x[i+1]-x[i])**2 + (y[i+1]-y[i])**2)
            area2 = area2 + ((x[i]*y[i+1])- (y[i]*x[i+1]))
    
    area = abs(area2/2)
    
    print(f"Perimeter: {distance}\nArea: {area}")
    

else:
    print("not a polygon / missing y")

    