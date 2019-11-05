#Iterate a String set an identified letter to upper case
student_name = "Catalin"
new_name = ""
for ltr in student_name:
    if ltr.lower() == "t":
        new_name += ltr.upper()
    else:
        new_name += ltr
print(student_name,"to " , new_name)