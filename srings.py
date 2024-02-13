course = 'Python for Beginners'
print(course[-2])
print(course[0:3])
print(course[1:])
print(course[:5])
print(course[:])
another = course[:]
print(another)
name = 'Jennifer'
print(name[1:-1])
essay = '''
My name is Kofi Poku.
I come from Gyinyaase.
I am BSc. Statisitics Degree holder, pursuing MPhil Mathematical Statistics
Thank you.
'''
print(essay)

###Formated Strings######
first = 'Kofi'
last = 'Poku'
message = first + ' ['+ last + '] is a coder'
msg = f'{first} [{last}] is a coder' #formated stringd
print(message)
print(msg)
