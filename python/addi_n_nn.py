# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
#Sample value of n is 5
#Expected Result : 615

#My Codes#
num=input("please inter and interge:")
inum=int(num)
n =inum
nn = inum*10 + inum
nnn =inum*100 + inum*10 + inum
print('#My Codes#')
print('n + nn + nnn =', n + nn + nnn)

#Other python Codes simpler#
n1 = int( "%s" % inum )
n2 = int( "%s%s" % (inum,inum) )
n3 = int( "%s%s%s" % (inum,inum,inum) )
print('#other code#')
print('n + nn + nnn = ', n1+n2+n3)
