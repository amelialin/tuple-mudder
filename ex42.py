## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    
    def __init__(self):
        print "Made an Animal"

## ?? Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## ?? Dog has-a name
        self.name = name
        print "Made a Dog named %s" % name

## ?? Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## ?? Cat has a name
        self.name = name
        print "Made a Cat named %s" % name

## ?? Person is a object
class Person(object):

    def __init__(self, name):
        ## ?? Person has a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None
        print "Made a Person named %s" % name

## ?? Employee is a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic? Popping up one level using super(), to Person; Person has a name.
        super(Employee, self).__init__(name)
        ## ?? Employee has a salary
        self.salary = salary
        print "Made an Employee with salary %d" % salary

## ?? Fish is an object
class Fish(object):
    
    def __init__(self):
        print "Made a Fish"

## ?? Salmon is a Fish
class Salmon(Fish):

    def __init__(self):
        print "Made a Salmon"

## ?? Halibut is a Fish
class Halibut(Fish):

    def __init__(self):
        print "Made a Halibut"


## rover is-a Dog that has a name Rover
rover = Dog("Rover")

## ?? satan is a Cat that has a name Satan
satan = Cat("Satan")

## ?? mary is a Person that has a name Mary
mary = Person("Mary")

## ?? mary has a pet, satan
mary.pet = satan
print "mary.pet", mary.pet

## ?? frank is an Employee that has a name Frank and salaray 120,000
frank = Employee("Frank", 120000)

## frank has a pet that we set equal to rover
frank.pet = rover
print "frank.pet", frank.pet

## flipper is a Fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is a Halibut
harry = Halibut()