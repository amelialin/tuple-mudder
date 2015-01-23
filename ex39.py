# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states in a different dict and their capitals
cities = {
    'CA': 'Sacramento',
    'MI': 'Lansing',
    'FL': 'Tallahassee'
}

# add some more cities!
cities['NY'] = 'Albany' # notice no comma here
cities['OR'] = 'Salem'

# print out some cities
print '-' * 10 # print out the underscore 10 times
print 'NY State has: ', cities['NY']
print 'OR State has: ', cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# now do it by using the state dict first, then the cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florda has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items(): # this seems a bit ruby-like! iterate over all states?
    print "%s is abbreviated as %s" % (state, abbrev)

# print every city in a state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the capital %s" % (abbrev, city)

# now do both at the same time
print '_' * 10
for state, abbrev in states.items(): # states.items() unpacks the dict into a list of tuples like [('Oregon', 'OR'), ('Florida', 'FL'), etc.]. Looping over them will unpack each tuple into 'state' and 'abbrev'
    print "%s state is abbreviated as %s and has the capital %s" % (state, abbrev, cities[abbrev]) # notice that we can use state, abbrev straight out of the states dict, but we must reference cities[abbrev]; this is because we've only defined our variables based on what our script can "see" in states.items(). We haven't told it before to look at the cities dict, so it wouldn't know the names of the cities and it wouldn't have assigned them to any variable yet.

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state: # if that returns FALSE:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist') # first input says what to look for, second value is the default return value
print "The capital for the state 'TX' is: %s" % city