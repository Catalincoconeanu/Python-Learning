#Finding the Largest Value from a list
x = -1
print("Before", x)
for y in [2,4,5,6,77,78,99]:
    if y > x:
        x = y
    print(x, y)
print("After", x)