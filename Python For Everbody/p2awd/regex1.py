Learn more or give us feedback
import re
hand = open("mbox-short.txt")
numlist = list()

for line in hand:
    line = line.rstrip()
    # the line below is to search for the line that strats with X-DSPAM-Confidence then the number after :
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print(numlist)
print("Maximum:",max(numlist))
