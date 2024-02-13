### Booleans #####
#Python has a type of variable called (bool). It has two possibles values: True and False

x = True
print(x)
print(type(x))

# Rather than puttingg True or False directly in our code, we usually get the boolean operators.
# These are operators that answer yes/no questions. We'll go through some of these operators below
# a == b -> a equals to b
# a < b -> a less than b
# a <= b -> a less than or equal to b
# a != b -> a not equal to b
# a > b -> a greater than b
# a >= b -> a greater than or equal b

def can_run_for_president(age):
    """ Can someone of the given age run for president in the US?"""
    # The US Constitution says you must be at least 35 years old
    return age >= 35

print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))


print(3.0 == 3)
print('3' == 3)


def is_odd(n):
    return (n % 2) == 1

print("Is 100 0dd?", is_odd(100))
print("Is -1 0dd?", is_odd(-1))


def can_run_for_president(age, is_natural_born_citizen):
    """ Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be at least 35 years old
    return is_natural_born_citizen and (age >= 35)


print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))

print(True or True and False) #Here note that there is an order of operation and 'and' is evaluated before 'or'
# This is why the results expression of the above is 'True'

#consider the expression below
have_umbrella = True
def rain_level(x):
    if x < 2.5:
        print('Cloudy Day')
    elif 2.5 < x < 7.6:
        print('Heavy Rain')
    elif 7.6 < x < 10:
        print('Violent Rain')
    else:
        print('No rain')
    return x
have_hood = True
prepared_for_weather = have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

#I'm trying to say that I'm safe from ytoday's weather....
# 1. if i have an umbrella...
# 2. or if the rain isn't too heavy and i have a hood...
# 3. otherwise, I'm still fine unless it's raining and it's workday
#But not only is my Python code hard to read, it has a bug. We can address both problems by adding parentheses:

prepared_for_weather = have_umbrella or ((rain_level < 5) and have_hood) or (not (rain_level > 0 and is_workday))

# or
prepared_for_weather = (
    have_umbrella
    or ((rain_level < 5) and have_hood)
    or (not (rain_level > 0 and is_workday))
)



### CONDITIONS ###
#Booleans are most useful when combined with conditional statments, using the keywords 'if', 'elif', and 'else'.
#Conditional statements, often referred to as if-then statements, let you control what pieces of code are run based on the value of some Boolean condition.
#Here's an example:

def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anythinh I've ever seen.....")
        
inspect(0)
inspect(-15)


def f(x):
    if x > 0:
        print("Only printed when x is positive; x =" , x)
        print("Also only printed when x is positive; x =", x)
    print("Always printed, regardless of x's value; x =", x)

f(1)
f(0)
f(-2)
f(10)


### BOOLEAN CONVERSION ####
#Python has 'bool()' function whuch turns things into bools.

print(bool(1)) # all the numbers are treated as true, except 0
print(bool(0))
print(bool("asf")) # all strings are treated as true, except the empty string ""
print(bool(""))

# Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
# are "falsey" and the rest are "truthy"


if 0:
    print(0)
elif "spam":
    print("spam")
    
