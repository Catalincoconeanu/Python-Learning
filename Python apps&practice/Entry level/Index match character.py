student_name = 'Catalin'
#We use .lower to convert to lower case
if student_name[0].lower() == 'a':
    print('Winner! Name starts with A', student_name)
elif student_name[0].lower() == 'c':
    print('Winner! Name starts with C', student_name)
else:
    print('Not a match, try again tomorrow', student_name)