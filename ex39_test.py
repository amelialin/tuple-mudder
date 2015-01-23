import hashmap

# create a mapping of state to abbreviation
states = hashmap.new() # Initializes a Map with the given number of buckets.
hashmap.set(states, 'Oregon', 'OR') # In the Map, sets the key to the value, replacing any existing value.
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# create a basic set of states and their capitals
cities = hashmap.new()
hashmap.set(cities, 'CA', 'Sacramento')
hashmap.set(cities, 'MI', 'Lansing')
hashmap.set(cities, 'FL', 'Tallahassee')

# add some more capitals
print '-' * 10
print "NY State has: %s" % hashmap.get(cities, 'NY')
print "OR State has: %s" % hashmap.get(cities, 'OR')

# print some states
print '-' * 10
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

assert hashmap.get(states, 'Michigan') == 'MI'

# do it by using the state dict, then the cities dict
print '-' * 10
print "Michigan has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has: %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

# print every state abbreviation
print '-' * 10
hashmap.list(states)

# print every capital in each state
print '-' * 10
hashmap.list(cities)

print '-' * 10
state = hashmap.get(states, 'Texas')

if not state:
  print "Sorry, no Texas."

# default values using ||= with the nil result # what does this even mean?? Keir thinks Zed is confused
# can you do this on one line?
# city = hashmap.get(cities, 'TX', 'Does Not Exist')
# print "The city for the state 'TX' is: %s" % city
print "The city for the state 'TX' is: %s" % hashmap.get(cities, 'TX', 'Does Not Exist')

hashmap.dump(states)

# ====STUDY DRILLS=====

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
print states
print len(states)
states_copy = states.copy() # makes a copy
print states_copy
states_copy.clear() # clears entire dict, resets to: {}
print states_copy
print states.has_key('California') # returns T/F value
print states.items() # returns a LIST of all the dict's key-value TUPLE pairs
print states.keys() # returns a LIST of all the KEYS
print states.values() # returns a LIST of all the VALUES