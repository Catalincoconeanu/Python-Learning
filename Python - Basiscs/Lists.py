# Lists of items, have order and index , a list is using square brackets
# Samples

shopList = ["apples", "oranges", "cheese"]
print(shopList)   #This will display the list

# we can use index values

shoplist[0]    # this will display the first item in the list > in this case Apples

# To add more items to an existing list

shopList.append("bannanas")  # The .append will add items in the list, at the end of the list

# To change an item based on index

shopList[0] = " Cherries"   # this will change apples string with cherries

# To delete an item

del shopList[1]   # This will delete from the list oranges, the corresponded of index 1

# To count the length of the list

len(shopList)

# To combine two or more lists
# create first and second lists first
shopList + shopList2     # the output will put all the items in the same output

# How to find the maximum nr from a list
# First we create the list

listNum = [1, 4, 7,23,6]
max(listNum)
# This will display the biggest number from the list