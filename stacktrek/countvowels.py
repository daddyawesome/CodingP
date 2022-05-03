aString = input("text:")
lowercase = aString.lower()

a = "a"
e = "e"
i = "i"
o = "o"
u = "u"

x = 0

if a in lowercase:
    x = x + 1
if e in lowercase:
    x = x + 1
if i in lowercase:
    x = x + 1
if o in lowercase:
    x = x + 1
if u in lowercase:
    x = x + 1

if x == 1:
    print("There is only one different vowel in the string.")
else:
    print(f"There are {x} different vowels in the string.")