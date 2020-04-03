class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

num = int(input("Kindly type an integer: "))
z =py_solution().int_to_Roman(num)
print("The roman numeral of your number is", z)
num2 = int(input("\n Kindly type again an integer: "))
z2 =py_solution().int_to_Roman(num2)
print("The roman numeral of your number is", z2)
