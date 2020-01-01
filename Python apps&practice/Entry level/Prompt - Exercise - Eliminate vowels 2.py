# Your task here is even more special than before: you must redesign the (ugly) vowel eater from the previous lab (3.1.2.10) and create a better, upgraded (pretty) vowel eater! Write a program that uses:
# a for loop;
# the concept of conditional execution (if-elif-else)
# the continue statement.
# Your program must:
# ask the user to enter a word;
# use userWord = userWord.upper() to convert the word entered by the user to upper case;
# use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
# assign the uneaten letters to the wordWithoutVovels variable and print the variable to the screen.
# Look at the code in the editor. We've created wordWithoutVovels and assigned an empty string to it. Use concatenation operation to ask Python to combine selected letters into a longer string during subsequent loop turns, and assign it to the wordWithoutVovels variable.

wordWithoutVowels = ""

userWord = input("Enter your word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        wordWithoutVowels += letter
		
print(wordWithoutVowels)