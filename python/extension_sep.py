# Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename : abc.java
# Output : java

fName = input("please enter the filename:")
ext = fName.split(".")

print("Your file Extension is",ext[1])
