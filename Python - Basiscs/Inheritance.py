# Inheritance
# A child class gets the properties of the parent class
# Sample:

class Parent:
    def __init__(self):
        print("This is the parent class")

    def parentFunc(self):
        print("This the parent func")


p = Parent()    # This will return: This is the parent class
p.parentFunc()  # This is the parent func


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("This is the child class")

    def childFund(self):
        print("This is the child function")


c = Child()     # This will return: This is the child class
c.childFund()   # This will return: This is the child function
c.parentFunc()  # This will return: This is the parent function

# Another example:
class plmclass:
    def __init__(self):
        print(" This is the Plm class")
    def plmFunction(self):
        print(" This is the Plm Function")


p = plmclass()
p.plmFunction()

class childclass(plmclass):
    def __init__(self):
        print(" This is the Child Class of plm class")
    def childclassFunction(self):
        print(" This is the function of child class")


c = childclass()
c.childclassFunction()
c.plmFunction()
