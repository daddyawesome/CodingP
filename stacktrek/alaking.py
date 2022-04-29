import math
v0 = float(input("what is the initial velocity:"))
DEG_theta = float(input("what is the angle:"))
theta = DEG_theta * math.pi /180 
t = float(input("what is the time:"))
g = 9.81

x = round(v0*math.cos(theta)*t,0) 
y = round(v0*math.sin(theta)*t - 0.5*g*t**2,0)

print(f"{int(x)}, {int(y)}")
print(math.cos(theta))
print(y)