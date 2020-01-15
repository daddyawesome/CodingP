#Same problem with exercise 3-1 but with try and except block
#

hrs = input("Enter Hours:")
rate = input("Enter your rate:")
try:
  h = float(hrs)
  r = float(rate)
except:
  print("Error, please enter numeric input")
  quit()

print(h, r)

if h > 40:
    reg = r * 40
    OTpay = (h-40) * (r * 1.5)
    pay = reg + OTpay
else:
    pay = h*r
print("Pay:",pay)
