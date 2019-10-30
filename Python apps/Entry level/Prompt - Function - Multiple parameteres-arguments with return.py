kl = input("Enter first nr:  ")
kp = input("Enter the second nr: ")
try:
    a = float(kl)
    b = float(kp)
except:
    print("Enter numberic values!!!")
    quit()
def xr(a, b):
    pl = a + b
    return pl
x = xr(a, b)
print(int(x))