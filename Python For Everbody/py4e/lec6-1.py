#Manipulating String
#

greet = "Hello Bob"
zap = greet.lower()
print(zap)
print(greet)
shout = greet.upper()
print(shout)
print("Hi there".lower())

#Searching a String
fruit ='banana'
pos =fruit.find('na')
print(pos)

aa=fruit.find('z')
print(aa)

#Search and Replace
nstr = greet.replace('bob','Jane')
print(nstr)

nstr =greet.replace('o','X')
print(nstr)

#Stripping Whitespace
greeet = '    Hello Bob  '
strp = greeet.lstrip()
print(strp)
strp = greeet.rstrip()
print(strp)
strp = greeet.strip()
print(strp)


#finding a the hostname from email
##Parsing strings

print("find the host for below")
print("From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008")
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

#find the location of @#
atpos = data.find('@')
print(atpos)

#Find the location of space afte @
sppos = data.find(' ',atpos)
print(sppos)

#slice the data (after @ to space)#
host = data[atpos+1:sppos]
print(host)
#uct.ac.za
