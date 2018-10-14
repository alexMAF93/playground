#!/usr/local/bin/python3.7


import sys


def banner(string):
    print('\n' + "="*30)
    print(string.center(30))
    print("="*30 + '\n')


banner('Strings')
print (r'acesta este un \text care co\ntine escapari puse aiurea') # raw string
print("Usage : ", sys.argv[0], " [OPTIONS]")
print("""OPTIONS:
	-v,
		verbose
	-x,
		execute
	""")
	
# with "+" you concatenate strings -- both operands must be strings

string1 = "Python"
print(string1[:3])
print(string1[3:])  # always string1[:i] + string1[i:] = string1


banner('Lists')
list1 = ['a', 'b', 'c']
print('Original list: ', list1)
list1[0] = 1
print('Modified list (part one) :', list1) # lists are mutable
list1[1:] = [2, 3]
print('Modified list (part two) :', list1) # slice + replace
list1[1:] = []
print('Modified list (part three) :', list1) # slice + remove
list1[:] = []
print('Modified list (part four) :', list1) # replace everything with an empty len
list2 = ['a', 'b', 'c']
list3 = [1, 2, 3]
list4 = [list2, list3]
print('A list made of lists :', list4)


banner('The FOR loop')
for n in range(2,10):
    for x in range(2, n):
	     if n % x == 0:
		     break
    else:
        print(n, 'is a prime number')  
		# you can use else for a for loop :O. Else clause runs when no break occurs

		
banner('Functions')
# Functions without a return value, return None by default
# The execution of a function introduces a new symbol table used for the local variables of the function. More precisely, all variable assignments in a function store the value in the local symbol table; whereas variable references first look in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names. Thus, global variables cannot be directly assigned a value within a function (unless named in a global statement), although they may be referenced.

#A function definition introduces the function name in the current symbol table. The value of the function name has a type that is recognized by the interpreter as a user-defined function. This value can be assigned to another name which can then also be used as a function.

def func1 ():
    """
	test function 
	""" # it seems that it's good practice to document functions
    print('\tThis is a test function to see if the renaming mechanism works!')


print('Documentation :', func1.__doc__)
print('This is the func1 function output:')
func1()
ffunc1 = func1
print('This is the ffunc1 (defined like this: ffunc1 = func1) output:')
ffunc1()


banner('PEP8')
print("""Use 4 spaces indentation and no tabs
Lines shoudn't exceed 79 characters
Comments on a line of their own
Use docstrings
""")


banner('Tuples')
t = 12345, 44, 'hello'  # this operation is called packing
print('This is the t tuple', t)
print('The tuple t was defined like this: t = 12345, 44, \'hello\'')
# tuples are immutable but they contain muttable objects (e.g.: lists)
# empty tuple : empty = ()
# single element tuple: singleton = 'abc', 
at, bt, ct = t # this operation is called unpacking
print("Unpacking the t tuple in 3 variables:") 
print("at =", at)
print("bt =", bt)
print("ct =", ct)


banner("Sets")
# Unordered collection with no duplicate elements
# Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
print('Creating an empty set : aset = set()')
aset = set()
print(aset)
print("Creating a set with 3 elements : bset = {'a', 1, 'c'}")
bset = {'a', 1, 'c'}
print(bset)


banner("Dictionaries")
# Dictionaries are indexed by keys
# Only immutable objects can be used as keys: strings, numbers, tuples
# If a tuple contains a mutable object it cannot be used as a key
print('Creating an empty dictionary : ad = {}')
ad = {}
print(ad)
print("Creating a simple dictionary with 3 values: bd = {1:'a', 2:'b', 3:'c'}")
bd = {1:'a', 2:'b', 3:'c'}
print(bd)
print('A list with the keys : ', list(bd))


banner("in / not in")
# These are comparison operators
# You can check if a value occurs or not in a sequence
# They check if two objects are really the same object; only for mutable objects
print ('Defining an integer, ai = 2')
ai = 2
print('Defining a list, bi = [1, 2, 3]')
bi = [1, 2, 3]
print('Checking if ai is in bi')
if ai in bi:
    print('It is!!!')
else:
    print('It is not')
print('The condition is true because ai is not mutable; ai and the 2 in bi are the same object. They have the same id:')
print('id(ai) =',id(ai))
print('id(bi[1]) =', id(bi[1]))
print('Defining a list : ci = [1, 2]')
ci = [1, 2]
print('Checking if ci is in bi')
if ci in bi:
    print('It is!!!')
else:
    print('It is not')
print('The condition is false because ci is mutable; ci and [1, 2] in bi are different objects. They have different ids:')
print('id(ci) =',id(ci))
print('id(bi[:2]) =',id(bi[:2]))

banner("Modules")