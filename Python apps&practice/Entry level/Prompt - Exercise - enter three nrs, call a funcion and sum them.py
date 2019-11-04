def func(a, b, c):
    xr = a + b + c
    return xr
xp = input("Enter first nr:")
xt = input("Enter the second nr:")
xl = input("Enter the thrid nr:")
try:
    x = float(xp)
    z = float(xt)
    y = float(xl)
except:
    print("Please enter only numeric values!")
    quit()
print(func(x, z, y))