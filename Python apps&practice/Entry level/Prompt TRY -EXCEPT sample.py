#Try - Except sample app , this will ask you input a nr, if the nr is > 0 then will print "Nice work!", if you input a string instead you get printed the second one
#Try - Except is used when we have to try something and if blows then the program skips and continues to run instead of stopping and displaying error
x = input("Enter a number here: ")
try:
    y = int(x)
except:
    y = -1

if y > 0 :
    print("Nice work!")
else:
    print("Not a number")