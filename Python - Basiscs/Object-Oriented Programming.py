# Object-Oriented Programming

class Person:
    def getName(self):
        print("Cata")

    def getAge(self):
        print("Coco")


p = Person()
p.getName()  # This will return Cata
p.getAge()  # This will return Coco

# Initialization function:
# The init function is used:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        print("Cata")
    def getAge(self):
        print("Age")


p1 = Person("Bob", "22")
p1.getName()
p1.getAge()
# This will return Cata and Age words.

