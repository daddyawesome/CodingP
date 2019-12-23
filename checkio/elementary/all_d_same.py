def all_the_same(numbers):
    if len(numbers) == 0:
        return True
    else:
        nTemp = numbers[0]
            
        for n in numbers:
            print(n)
            print(nTemp)
            if nTemp == n:continue
            else:
                return False
        return True

         
print(all_the_same([1, 1, 1]))
print(all_the_same([1, 2, 1]))
print(all_the_same(['a', 'a', 'a']))
print(all_the_same([]))
print(all_the_same([1]))
