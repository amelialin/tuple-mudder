def bazooolppAmeliaIsCute():
  try:
    bar()
  except ValueError:
    pass

def bar():
  print 'I like that Amelia is a fast learner'
  foo()
  print 'hello'

def foo():
  raise ValueError("hi!")

bazooolppAmeliaIsCute()
print "It's the end of the function and I know it!"
