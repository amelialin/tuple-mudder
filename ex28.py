# Establish whether the following boolean logic statements will evaluate to 
# TRUE or FALSE

assert (True and True) # True
assert not (False and True) # False
assert not (1 == 1 and 2 == 1)
# True and False
# False
assert ("test" == "test")
# True
assert (1 == 1 or 2 != 1)
# True or True
# True
assert (True and 1 == 1)
# True
assert not (False and 0 != 0)
# False
assert (True or 1 == 1)
# True
assert not ("test" == "testing")
# False
assert not (1 != 0 and 2 == 1)
# True and False
# False
assert ("test" != "testing")
# True
assert not ("test" == 1)
# False
assert (not (True and False))
# not False
# True
assert not (not (1 == 1 and 0 != 1))
# not (True and True)
# False
assert not (not (10 == 1 or 1000 == 1000))
# not (False or True)
# not True
# False
assert not (not (1 != 10 or 3 == 4))
# not (True or False)
# False
assert (not ("testing" == "testing" and "Zed" == "Cool Guy"))
# not (True and False)
# not False
# True
assert (1 == 1 and (not ("testing" == 1 or 1 == 0)))
# True and (not (False or False))
# True and (not False)
# True
assert not ("chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
# False
assert not (3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))
# True and (not (True or False))
# True and (not True)
# True and False
# False