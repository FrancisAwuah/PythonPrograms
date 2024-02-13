### LISTS AND TUPLES ####
# Lists and the things you can do with them. Includes indexing, slicing and mutating
# Lists in Python represent ordered sequences of values. Here is example of how to create them:

primes = [2, 3, 5, 7]
print(primes)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets)

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'],  # (Comma after the last element is optional)
]

# (I could also have written this on one line, but it can get hard to read)
print(hands)

my_favourite_things = [32, 'raindrops on roses', help]
# (Yes, Python's help function is *definitely* one of my favourite things)
print(my_favourite_things)

### INDEXING ####
print(planets[0])
print(planets[1])

### SLICING ####
# What are the first three planets? We can answer this question using slicing.

print(planets[0:3])

#If I leave out the end index, it's assumed to be the lenght of the list.

print(planets[3:0])


#i.e. the expression above means "give me all the planets from index 3 onward"

#We can also use negative indices when slicing:
print(planets[-1:1])
print(planets[-3:])


### CHANGING LISTS ####
# Lists are "mutable", meaning they can be modified "in place"
# One way to modify a list is to assign to an idex or slice expression
# For example, let's saye we want to rename Mars:
planets[3] = 'Malacandra'
print(planets)


#that's quite a mouthful. Let's compensate by shortening the names of the first 3 planets.
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars']
print(planets)

### LIST FUNCTIONS ####
# Python has several useful functions for working with lists.
# "len" gives the length of a list:
# How many planets are there?
print(len(planets))

# "sorted" returns a sorted version of the lsit:
# The planets sorted in aplhabetical order
print(sorted(planets))

# "sum" does what you might expect
primes = [2, 3, 5, 7]
print(sum(primes))

# 'min' for minimum & 'max' for maximum
print(min(primes))
print(max(primes))

# Interlude: Objects
#In short, objects carry some things around with them.
#You access that stuff using Python's dot syntax.
#For example, numbers in Python carry around an associated variable called 'imag' representing their imaginary part.
#(You'll probably never need to use this unless you're doing some very weird math.)

x = 12
#x is a real number, so its imaginary part is 0
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)

#The things an object carries around can also include functions.
#A function attached to an object is called a 'method'.
#(Non-function things attached to an object, such as 'imag', are called attributes)
#For example, numbers have a method called 'bit_length'.
#Again, we access it using dot syntax:
print(x.bit_length())
help(x.bit_length)


# LIST METHODS

#list.append modifies a list by adding an item to the end:
print(planets.append('Pluto'))


#list.pop removes and returns the last element of a list:
print(planets.pop())


#Where does Earth fall in the order of planets? We can get its index using the list.index method.

print(planets.index('Earth'))

#we can use the in operator to determine whether a list contains a particular value:

# Is Earth a planet?
print("Earth" in planets)

# Is Calbefraques a planet?
print("Calbefraques" in planets)



# TUPLES #
# Tuples are almost exactly the same as lists. They differ in just two ways.
# 1: The syntax for creating them uses parentheses instead of square brackets

print(t = (1, 2, 3))




