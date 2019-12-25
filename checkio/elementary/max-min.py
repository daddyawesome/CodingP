def checkio(*args):
    try:
        max1 =max(args)
        min1 =min(args)
        
        x = max1 - min1
    except:
        x = ""
    return x

if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
        
    print('Example:')
    print(checkio(1, 2, 3))
