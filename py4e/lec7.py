#fhand is just a file handler
fhand = open('mbox-short.txt')

#this will not print the text inside the file
print(fhand)


count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)
        count = count + 1
print(count)
