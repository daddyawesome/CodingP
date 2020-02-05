import re
hand = open("mbox-short.txt")
email = list()

for line in hand:
    line = line.rstrip()
    # the line below is to search that starts with From: then space 
    stuff = re.findall('^From (\S+@\S+)', line)
    if len(stuff) != 1: continue
    
    email.append(stuff)
print(email)
