# Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in lower case. Use the file words.txt to produce the output below.
fname = input("Enter file name: ")
fhand = open(fname)
for line in fhand:
    #remove the white after each line
    line = line.rstrip()
    print(line.lower())
