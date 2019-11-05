#String Method Find

#Example: 1
print("Example: 1")
work_tip = "save your code"
print("Find the index of the first space")
print(work_tip.find(" "))
print()

#Example: 2
print("Example: 2")
work_tip = "good code has meaningful variable names"
print(work_tip)
code_here = work_tip.find("code")
print(code_here, "= starting index for code")
print()

#Example: 3
print("Example: 3")
print("work_tip: ", work_tip, "\n")
location = work_tip.find("o")
while location >= 0:
    print("o at index = ", location)
    location = work_tip.find("o", location + 1)
print("\nno more o's, -1 was returned")
print()

#Example: 4 
print("Example: 4")
print("search for 'meaning' in the sub-string:", work_tip[13:33], "\n")
meaning_here = work_tip.find("meaning", 13, 33)
print("'meaning' found in work_tip[13:33] sub-string search at index", meaning_here)