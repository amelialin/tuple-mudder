# =======================
# == With-As Statement ==
# =======================

# still not sure how this works??

class controlled_execution:
    def __enter__(self):
        pass
        # set things up
        # return things
    def __exit__(self, type, value, traceback):
        pass
        # tear things down

with controlled_execution() as thing:
    pass
    # do something

# =======================
# == Defining A Class === # when do you use this?
# =======================

class Loaf: # the most basic and useless implementation
    pass

# something more sophisticated:

from UserDict import UserDict

class FileInfo(UserDict):
    """store file metadata"""
    def __init__(self, filename=None): # init is always called immediately after an instance of the class is created. First argument is always called "self". Init methods can take any # of arguments, and you can give them default values if you want. The init method never returns a value.
        UserDict.__init__(self) # what is going on here?
        self["name"] = filename # we've said this class will act like a dictionary. So in this line, we're saying please pair the key "name" with the value "filename".

# another example

class Team(object): # what is this "object" thing our Team class is inheriting characteristics from?
    def __init__(self, name=None, logo=None, members=0):
        self.name = name
        self.logo = logo
        self.members = members

# how you'd use it:

team = Team("Soccer Team", "http://logo.png", 5)
team2 = Team()
team2.name = "Basketball Team"
team3 = Team(name="Football Team", members=12)

# =======================
# == Using Continue======
# =======================

# continue pops you out of a loop. Good in situations where you have a lot of conditions to fulfill, so that you can avoid heavily nested code.

for x in range(20):
    if x < 3:
        continue
    if x > 10:
        continue
    if x % 2 != 0:
        continue
    print x # only runs if x is between 3 and 10 and is even

# =======================
# ==Using Exec and Eval==
# =======================

exec 'print "hello"'

# ==========================
# ==Using Lambda Functions==
# ==========================

def multiply_by(n): return lambda x: x * n # define what paramenter in the function will vary

f = multiply_by(2) # function f now multiplies argument by 2
g = multiply_by(3) # function g now multiplies argument by 3

print "f(2):", f(2), "g(2):", g(2)
print "multiply_by(2)(12):", multiply_by(2)(12)

# =======================
# ==Using Yield==========
# =======================

mylist = [1, 2, 3] # lists are an iterable
for i in mylist:
    print i
for i in mylist:
    print i # you'll get 2 copies of the list

mygenerator = (x*x for x in range(3)) # generators are iterators BUT you can only iterate over them *once* bc they generate values on the fly
for i in mygenerator:
    print i
for i in mygenerator: # this 2nd round won't return anything!
    print i*2

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator() # create a generator
print mygenerator

for i in mygenerator:
    print i
for i in mygenerator: # wait! this still doesn't work! why? I thought it was supposed to?
    print i*2
