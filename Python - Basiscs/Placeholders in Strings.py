# Samples:

name = "Cata"
name + " is 31 years old!"


# This will return: " Cata is 31 years old!
sent = "%s is 31 years old!"
print(sent%name)
# This will print the " Cata is 31 years old!
sent%("Cata")


# If we have more variables a string and an integer
sent = "%s %s is %d years old!"
sent2 = sent%("Cata Coconeanu", 31)
print(sent2)