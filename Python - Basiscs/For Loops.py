# Samples:
list1 = ["Apples", "Bannanas", "Cherries"]
tup1 = (1, 2, 3)
for item in list1:
    print(item)
for item in tup1:
    print(item)
# This will print the list of Apples,Bannanas, Cherries

# Range function: as per example it goes 1 less, will print from 1 to 9

for i in range(0, 10):
    print(i)

# Range function: Skipp feature > as we add one more nr will be the counter, will print 0, 2, 4, 6, 8, 10

for x in range(0, 11, 2):
    print(x)

# Nested FOR loops:

for i in range(0, 5):
    for x in range(0, 3):
        print(i*x)
# This will print:
# 0
# 1
# 2
# 1
# 2
# 3
# 2
# 3
# 4
# 3
# 4
# 5
# 4
# 5
# 6