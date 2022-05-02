humanyr=int(input("Enter human year:"))

if humanyr <= 2:
    dogyr = humanyr * 10.5
else:
    dogyr = (humanyr -2)*4 + 21

print(dogyr)
