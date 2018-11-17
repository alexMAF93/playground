#!/usr/local/bin/python3


import os, sys

# text decorations
BOLD_UND='\033[1m\033[4m\033[94m'
END='\033[0m'


def usage():
    print("""
Prints the directory tree in an easy to read format.
It also makes a clear disctinction between a file and a directory.

Usage:
    {} [DIR_NAME]
    
    
The Directory for which you want to see the structure is an argument to this command and it is optional. If it is not specified, the current directory will be used.
You can see the structure for one directory at a time.
Maybe this will be upgraded in the near future.
""".format(sys.argv[0]))


def walking_through(directory, number_of_del):
    reset_number_of_del = number_of_del
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory,item)):
            print('   ' * number_of_del + '|——f—— ' + item)
        elif os.path.isdir(os.path.join(directory,item)):
            print('   ' * number_of_del + '|——d—— ' + BOLD_UND + item + '/' + END)
            if len(os.listdir(os.path.join(directory,item))) > 0:
                number_of_del += 1
                walking_through(os.path.join(directory,item), number_of_del)
            else:
                print('   ' * number_of_del + '|    *empty directory*')
        number_of_del = reset_number_of_del


if len(sys.argv) > 1 and len(sys.argv) < 3:
    directory = sys.argv[1]
elif len(sys.argv) == 1:
    directory = '.'
else:
    usage()
    sys.exit(0)
    
if os.path.isdir(directory):
    print(BOLD_UND + directory + END)
    print('|')
    number_of_del = 0
    walking_through(directory, number_of_del)
else:
    print('ERROR: The argument you provided is not a directory\n\n\n')
    sys.exit(7)
