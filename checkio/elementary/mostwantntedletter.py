def checkio(words):
    str1 =str.lower(words)
    counts =dict()
    for n in str1:
        if(n.isalpha()):
            counts[n] = counts.get(n, 0) +1
        else: 
            continue
    print (counts)
    d3={v:k for k,v in counts.items()}
    return d3[max(d3)]

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

#count the alphabet, the numbers and the special
string = input("Please Enter your Own String : ")
alphabets = digits = special = 0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
        
print("\nTotal Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)
