# read three numbers and compares them using the max() function or min() function to get the smallest nr
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# check which one of the numbers is the greatest
# and pass it to the largest_number variable

largest_number = max(number1, number2, number3)

# print the result
print("The largest number is:", largest_number)