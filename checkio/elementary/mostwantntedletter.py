def checkio(words):
    str1 =str.lower(words)
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    print (dict)
    d3={v:k for k,v in dict.items()}
    return d3[max(d3)]
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
