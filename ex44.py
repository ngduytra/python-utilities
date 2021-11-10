class Parent(object):
    
    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("Parent implicit()")

    def altered():
        print("PARENT altered()")

class Child(Parent):
    def override(self):
        print("CHILD override()")
    
    def altered():
        pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

""" We have MRO definition in Python to handle Multiple Inheritance"""
