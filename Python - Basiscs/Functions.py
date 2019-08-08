# Functions: after creating the function we must call the function

def HelloWord():
    print("Hello World!")


HelloWord()


# Another example: This will print: " Hi Cata!
def Greeting(name):
    print("Hi " + name + "!")


Greeting("Cata")


# Sample: This will print out num1 + num2 =  10 +  15 =  25
def Add(num1, num2):
    print(num1 + num2)


Add(10, 15)


# RETURN statement: associate a value to a variable, in python is return statement is present will not pass to the second statement, the process will stopp at return
def returnAdd(num1, num2):
    return(num1 + num2)
    print("Hello World")

sum = returnAdd(12, 14)
print(sum)
