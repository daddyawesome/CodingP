word = input("enter your word: ")
num = int(input("enter num: "))
temp =list(word)
index = 0

for i in temp:
    i_num = ord(i)
    
    # check if they are in alphabet
    if i_num > 64 and i_num < 91 or i_num > 96 and i_num < 123 :
        j_ord = i_num + num
        
        #check if they ar ein alphabet after adding number
        if j_ord > 90 and j_ord < 97 or j_ord > 122:
            j_ord = j_ord - 26
        j =chr(j_ord)
    
    else:
        j = i
    
    temp[index] = j
    str = "".join(temp)
    index += 1

print(str)