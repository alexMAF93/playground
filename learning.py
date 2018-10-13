#!/usr/local/bin/python3.7


import sys


def banner(string):
    print('\n' + "="*30)
    print(string)
    print("="*30 + '\n')


banner('Learning strings')
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


banner('Learning lists')
list1 = ['a', 'b', 'c']
print('Original list: ', list1)
list1[0] = 1
print('Modified list (part one) : ', list1) # lists are mutable
list1[1:] = [2, 3]
print('Modified list (part two) : ', list1) # slice + replace
list1[1:] = []
print('Modified list (part three) : ', list1) # slice + remove
list1[:] = []
print('Modified list (part four) : ', list1) # replace everything with an empty len
list2 = ['a', 'b', 'c']
list3 = [1, 2, 3]
list4 = [list2, list3]
print('A list made of lists : ', list4)