def all_the_same(numbers):
        x =None
    for n in numbers:
        x = x+n    
        if x is None or x == n: continue
        else:
            return False


#all_the_same([1, 1, 1]) == True
#all_the_same([1, 2, 1]) == False
#all_the_same(['a', 'a', 'a']) == True
#all_the_same([]) == True

print(all_the_same([1, 2, 1]))
