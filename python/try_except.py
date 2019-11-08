#Try and Except block. 
#Sample program to avoid traceback.

num = input("please enter a number:")

try:
    ival = int(num)
except:
    ival = -1
    
if ival>0:
    print("Thank You for giving me a number")
else:
    print("Nice try dude! You're not giving me a number.")

