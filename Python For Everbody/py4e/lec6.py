word = "banana"
count = 0

for letter in word:
    if letter == "a":
        count = count + 1
    print(letter)

print(count)

#Print out every call on reference

print("\n From here we write using reference")
print(word[0])
print(word[2])
print(word[5])

#Slicing Strings
s = "Monty Python"
 
print("\n slicing strings")
print(s[0:4])
print(s[6:7])
print(s[6:20])
