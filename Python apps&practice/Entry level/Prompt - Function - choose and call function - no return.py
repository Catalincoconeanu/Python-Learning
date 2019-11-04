def hello(x):
    if x == 'es':
        print("You choose Spanish!")
    elif x == 'en':
        print("You choose English!")
    elif x == 'fr':
        print("You choose French!")
    else:
        print("Some other language")
x = input("Choose between es, en and fr language:  ")
hello(x)