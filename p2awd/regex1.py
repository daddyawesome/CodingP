import re
hand = open("mbox-short.txt")
numlist = list()

for line in hand:
    line = line.rstrip()
    # the line below is to search for the line that strats with X-DSPAM-Confidence then the number after :
    stuff = re.findall('href=".+"', line)
   
    if len(stuff) < 1: continue
    print(stuff)
 
    #num = float(stuff[0])
    #numlist.append(num)
print(stuff)
#print("Maximum:",max(numlist))
