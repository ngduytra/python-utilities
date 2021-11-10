## Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
    def __init__(self, name):
        self.name = name
        

## ??
class Dog(Animal):
    def __init__(self, name):
        ## ??
        super(Dog, self).__init__(name)
    
    def speak(self):
        print("Mowwwwwwww, i am %s" % self.name)
## ??
class Cat(Animal):

    def __init__(self, name):
        super(Cat, self).__init__(name)

    def speak(self):
        print("Mowwwwwwww, i am %s" % self.name)

## ??
class Person(object):
    def __init__(self, name):
        ## ??
        self.name = name
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")
rover.speak()

## ??
satan = Cat("Satan")
satan.speak()

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flippper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
