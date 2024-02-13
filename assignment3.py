print("""Q1""")
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    total_candies = 91
    number_sharing = 3
    print("Splitting", total_candies, "candies")
    sharing_equally = round(total_candies / number_sharing)
    print("Each one had ",sharing_equally)
    print(total_candies % 3)
    return total_candies % 3

to_smash(91)



print("""Q2""")
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candies == 1:
        print("Splitting", total_candies, "candy")
    else: print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)
to_smash(1)



print("""Q3""")
def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = True
rain_level = 7.5
have_hood = True
is_workday = True

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

print("""Q4""")
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return (number < 0, TRUE)# Your code goes here (try to keep it to one line!)
    print(concise_is_negative)


print("""Q5""")
def onionless(x, y, z):
    """Return whether the customer doesn't want onions.
    """
    print(x, y, z)

onionless("ketchup", "mustard", " ")

def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    if ketchup == True:
        print("ketchup")
    elif ketchup == False:
        print("no ketchup")
    if mustard == True:
        print("mustard")
    elif mustard == False:
        print("no mustard")
    if onion == True:
        print("onions")
    elif onion == False:
        print("no onions")

onionless(True, True, False)


def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    if ketchup == True:
        print("ketchup")
    elif ketchup == False:
        print("no ketchup")
    if mustard == True:
        print("mustard")
    elif mustard == False:
        print("no mustard")
    if onion == True:
        print("onions")
    elif onion == False:
        print("no onions")

wants_all_toppings(True, True, True)

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    if ketchup == True:
        print("ketchup")
    elif ketchup == False:
        print("no ketchup")
    if mustard == True:
        print("mustard")
    elif mustard == False:
        print("no mustard")
    if onion == True:
        print("onions")
    elif onion == False:
        print("no onions")

wants_plain_hotdog(False, False, False)
    
def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    if ketchup == True:
        print("ketchup")
    elif mustard == True:
        print("mustard")
    else:
        onion == True,
        print("onions")


exactly_one_sauce(True, False, False)
exactly_one_sauce(False, False, False)



