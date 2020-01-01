#Let's have a look at a short program whose task is to write some of the first powers of two:
pow = 1
for exp in range(16):
    print("2 to the power of", exp, "is", pow)
    pow *= 2