from cmath import sqrt

import math 
v_i = 0
d = float(input("what is distance form earth:"))
a = 9.8

v_f =math.sqrt(v_i**2 + 2 * a*d)

print(f"{v_f:.2f}")