def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

def double_cheese(cheese_count):
	double_cheeses = cheese_count * 2
	return double_cheeses

cheeses = int(raw_input("How much cheese? ")) # if you want this to be blank you can simply enter 'prompt' as the argument, without quotes

# using the values directly
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# define values for variables, then plug in the variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# do math inside the arguments
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# more math inside the arguments
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# taking user input
print "And we can take user input:"
cheese_and_crackers(cheeses, 1)

# taking output of another function
print "And we can take the output from another function:"
cheese_and_crackers(double_cheese(cheeses), 1)