print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and  \t tabs.'

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
andrequires an explanation
\n\t\twhere there is none
"""

print "----------------"
print poem
print "----------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans,  jars, crates
	
start_point = 1000
beans, jars, crates = secret_formula(start_point)

print "With starting point: %d" % start_point
print "We have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do it this way: "
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)  