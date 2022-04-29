books =int(input("Number of books:"))
cprice = 24.95
discountp = 24.95 * (100-40)/100

ship_1stbook = 3.00
shipping = (books-1) * 0.75

total = (books * discountp) + ship_1stbook + shipping

print(total)