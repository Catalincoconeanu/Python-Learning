# Every dictionary has a key and a value, always must use {}

students = { "Bob":12, "Cata":31}

# To access a specific value

students{"Bob"}   # This will return the value 12 assigned to Bob


# To change a value of an item in dictionaries

students["Cata"] =  15   # Now the value of item "Cata" will be changed to 15

# Remove items from dictionaries

del students["Bob"]    # This will remove "Bob" from the dictionary

# To count the nr of items in a dictionary
len(students)

# We cannot have multiple keys assigned to same item
students = {"Bob":12, "Bob""14", "Bob":16}   # this is wrong, it will return only 16

