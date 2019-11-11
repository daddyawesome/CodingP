# This one is like your script with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# This one takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
# This one takes no argument
def print_none():
	print "I got Nothing."

	
print_two("Mark", "Russel")
print_two_again("Mark", "Russel")
print_one("First!")
print_none() 