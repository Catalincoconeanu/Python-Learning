xnr = input("Enter a nr: ")
try:
    znr = float(xnr)
except:
    print("Please enter a numberic value!")
    quit()
if znr <= 20:
    print("The nr is smaller or equal to 20")
elif znr <= 50 :
    print("The nr is smaller or equal to 50")
elif znr >= 100 :
    print("The nr is bigger or equal to 100 ")
else :
    print("Error")