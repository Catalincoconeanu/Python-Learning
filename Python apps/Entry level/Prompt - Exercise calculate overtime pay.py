# Exercise: Write a pay computation that give to the employee 1.5 times the hourly rate for hours worked above 40 hours.
sh = input("Enter Hours:")
sr = input("Enter Rate:")
fh = float(sh)
fr = float(sr)
# print(fh, fr)
if fh > 40 :
    # print("Overtime")
    reg = fr * fh
    #Here we calculate the difference in overtime the surplus hours plus the fr * 0.5 > the overtime difference * rate 
    otp = (fh - 40.0) * (fr * 0.5)
    # print (reg,otp)
    #Now we put in one variable the normal 40 hours work (hours * rate) + the calculated overtime 
    xp = reg + otp
else:
    # print("Regular")
    xp = fr * fr
print("Pay: ", xp)