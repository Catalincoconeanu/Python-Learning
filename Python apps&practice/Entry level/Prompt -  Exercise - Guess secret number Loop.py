secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
x = int(input("Enter your number: "))
while x != 777:
    print("Ha ha! You're stuck in my loop!")
    x = int(input("Enter your number: "))
else:
    print("Well done, muggle! You are free now.")