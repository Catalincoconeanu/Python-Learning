#String Method: Count
work_tip = "save your code"
print("Letter "," e " "occurrence ", work_tip.count("e") )
work_tip.count("e")
print()

#Another example:
print("Another example:1")
print(work_tip)
print("how many w's?", work_tip.count("w"))
print("how many o's", work_tip.count("o"))
print("uses code,", "how many times?", work_tip.count("code"))

#Another example:
print()
print("Another example:2")
print(work_tip[:7])
print("# o's in first half")
print(work_tip[:7].count("o"))
print()
print(work_tip[7:])
print("# o's in second half")
print(work_tip[7:].count("o"))