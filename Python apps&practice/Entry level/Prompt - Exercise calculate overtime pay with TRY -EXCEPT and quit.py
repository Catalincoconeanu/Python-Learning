# Exercise: Write a pay computation that give to the employee 1.5 times the hourly rate for hours worked above 40 hours.
sh = input("Enter Hours:")
sr = input("Enter Rate:")
#If the input might be wrong, for example instead of numbers we input letters, then the app will throw error, to avoid error we use try-except to skip the error and keep executing
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    #To avoid the Traceback error we can use quit() to quit the program if the error occurs
    quit()
if fh > 40 :
    reg = fr * fh
    #Here we calculate the difference in overtime the surplus hours plus the fr * 0.5 > the overtime difference * rate 
    otp = (fh - 40.0) * (fr * 0.5)
    #Now we put in one variable the normal 40 hours work (hours * rate) + the calculated overtime 
    xp = reg + otp
else:
    xp = fh * fr
print("Pay: ", xp)