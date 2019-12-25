'''
Let's try some sorting. Here is an array with the specific rules.

The array (a tuple) has various numbers. You should sort it, but sort it by absolute value in ascending order. For example, the sequence (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20). Your function should return the sorted list or tuple.
'''
#sort by last digit for numbers from 10 to 99 only
sorted([11, 20, 54, 73], key=lambda x: str(x)[1]) == [20, 11, 73, 54]
#sort lists by sums
sorted([[90, 11], [99, 1], [200], [30, 50, 50]], key=sum) == [[99, 1], [90, 11], [30, 50, 50], [200]]

def checkio(numbers_array: tuple) -> list:
    return sorted(numbers_array, key=abs) 

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(list(checkio((-20, -5, 10, 15))))

    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")