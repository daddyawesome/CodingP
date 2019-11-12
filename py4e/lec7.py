#fhand is just a file handler
fhand = open('mbox-short.txt')

#this will not print the text inside the file
print(fhand)


count = 0
for line in fhand:
    #remove the white after each line
    line = line.rstrip()
    #print all lines that starts with From
    if line.startswith('From:'):
        print(line)
        count = count + 1
print(count)
