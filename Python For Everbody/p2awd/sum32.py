import re
hand = open("sum32.txt")
numlist = list()

for line in hand:
    line = line.rstrip()
    # the line below is to search for the line with numbers
    stuff = re.findall('[0-9]+', line)
    if len(stuff) < 1: continue
    for x in stuff:
        num = int(x)
        numlist.append(num)
print(numlist)
print("The sum:",sum(numlist))
