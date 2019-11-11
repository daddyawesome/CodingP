people = float(raw_input("people: "))
cats = float(raw_input("cats: "))
dogs = float(raw_input("dogs: "))

if people < cats:
	print "Too many cats the world is doomed!"
	
if people > cats:
	print "The world is saved!"
	
if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry."
	
dogs += 5

print "People: %d, dogs: %d, cats: %d" % (people, dogs, cats)

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs:
	print "People are lesser than or equal to dogs."
	
if people == dogs:
	print "People are dogs."