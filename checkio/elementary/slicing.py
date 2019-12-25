#For example, you can now easily extract the elements of a list that have even indexes:

L = range(10)
x = L[::2]
print(x)

##Negative values also work to make a copy of the same list in reverse order:
y=L[::-1]
print(y)

#This also works for tuples, arrays, and strings:
s='abcd'
z =s[::2]
print(z)

xx = s[::-1]

print(xx)

##for odd index
xy =s[1::2] 
print(xy)
