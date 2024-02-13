spam_amount = 0
print(spam_amount)
print(type(spam_amount))

      
#Ordering Spam, egg, Spam, Spam, bacon and Spam ( 4 more servings of spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam" * spam_amount
print(viking_song)


hat_height_cm = 25
my_height_cm = 190
# How tall a, i, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")
print("Height in meters = " + str(total_height_meters) + " ?") #Here total_height_meters was to be converted into strings for this to happen


total_height_meters = (hat_height_cm + my_height_cm) / 100 #Paranthesis are useful here for sub-expressions
print("Height in Meters =", total_height_meters) #Difference in answer from first code, correct answer here.


#Builtin functions for working with numbers
#min and max
print(min(1, 2, 3))
print(max(1, 2, 3))


#abs returns the absolute value of an argument:
print(abs(32))
print(abs(-32))

#float and int
print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)

