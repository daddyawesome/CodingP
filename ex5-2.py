init = input("Enter a number:")
try:
  init1 = int(init)
except:
  print("Invalid input")

smallest = init1
largest = smallest

while True:
  sval = input("Enter a number:")
  if sval == "done":
    break
  try:
    ival = int(sval)
  except:
    print("Invalid input")
    
  
  if ival > largest:
    largest = ival

  if ival < smallest:
    smallest = ival
  
print("Maximum is", largest)
print("minimum is", smallest)
