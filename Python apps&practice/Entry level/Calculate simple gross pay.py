#This app will prompt you for hours and rate per hour then will compute gross pay.
xh = input("Enter Hours: ")
xz = input("Enter Rate: ")
#Here we must convert the string to float nrs, since rate can be set as decimal value, example: 3.75
xp = float(xh) * float(xz)
print("Your pay is: ", xp ,"$") 