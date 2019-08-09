# In-Build Python Functions
# Absolute function

abs(-23)
# Will return the positive version of nr, in this case 23

# Bool Function

bool(0)
# This will return False
bool(1)
# This will return True
bool(None)
# This will return False

# Dir function: will display usable functions:
dir("hello")

# Help function:
sent = "hello"
help(sent.upper)

# Another sample
help(sent.splitlines)
# This will display what splitlines function does.

# Eval function:
sent = 'print"Hi"'
eval(sent)

# Exec function, when we have multiple lines of code
exec(sent)
# How to convert to different values
a =  1  # if we want to convert to a string
str(a)   # if we want to convert into a string
float(a)  # if we want to convert into a float nr
int(a)    # if we want to convert into a integer