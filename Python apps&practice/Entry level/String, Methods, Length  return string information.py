#String, Methods:Length > return string information
work_tip = "save your code"
print("Number of character in string", len(work_tip))

# Another example:
work_tip1 = "Good code is commented code!"
print("The sentence: \"" + work_tip1 + "\" has character length = ", len(work_tip1))

# Another example:
work_tip2 = "Good code is commented code"
lent_tip = len(work_tip2)
mid_pt = int(lent_tip/2)
print(work_tip2[:mid_pt])
print(work_tip2[mid_pt:])