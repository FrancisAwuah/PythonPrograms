help(round)
help(round(-2.01))
help(print)

#Defining functions
def least_difference(a, b, c):
    diff1 = abs(a -b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)

help(least_difference)


#Docstrings

#Python isn't smart enough to read a code into english description. However,
#when you write a function, you can provide a description in what's called the DOCSTRING

def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c

    >>>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a -b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)
#Python allows us to define such functions. the result of calling them is the special value None
#Without (return) statement, least_difference is completely pointless, but the function with side effects may do
#something useful without returning




help(least_difference)


#Functions that do not return
#What would happen if you didn't include the return keyword in our function
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c
    """

    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)

mystery = print()
print(mystery)

#Default Arguments
print(1, 2, 3, sep=' <') #Here we have spcified what should separate 1,2,3
print(1, 2, 3,) #Here no specification done

#Adding optional arguments with default values to the functions we define turns out to be pretty easy:
def greet(who="Collins"):
    print("Hello,",who)

greet()
greet(who="Kaggle")
#(In this case, we don't need to specify the name of the argument, because its's unambigious.)
greet("world")


#Functions Applied to Functions
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    "Call fn on arg"
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the resukt of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1),
    sep='\n', #'\n' is the newline character - it starts a new line

)

#Functions that operate on other functions are called "higher-order functions." You probably won't write your own for a little while.
#But there are higher-order functions built in Python that you might find useful to call
#Here is a an interesting example using the (max) function
#By default, max returns the largest of its arguments
#But  if we pass in a function using the optional key argument, it returns the argument x that maximizes key(x) (aka the 'argmax')

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo of 5',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)


help(round)

