#!/usr/local/bin/python3


import mysql.connector, sys


# connecting to the database
mydb = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root', # I am gROOT
    passwd = 'asd123', # it's not my most clever password
    database = 'jokes'
    ) # done
    

mycursor = mydb.cursor()  # a MySQLCursor object

try:
    value = sys.argv[1] # an argument must be provided
except:
    print('You must specify an email address')
else:
    if '@' in value:
	# the query
        query = "INSERT INTO jokes (email) VALUES ('" + value + "')"
        try:
            mycursor.execute (query)
        except:
            print('There was an error when we tried to add the email address in our database')
        else:
		# changes must be commited
            mydb.commit()
            print(mycursor.rowcount, 'record inserted.')
            mycursor.close()
            mydb.close()
    else:
        print('You must specify an email address')
