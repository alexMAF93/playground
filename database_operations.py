#!/usr/local/bin/python3


import mysql.connector, sys


def usage():
    """
    this function displays the
    options of this script
    """
    print("Usage:", sys.argv[0], "OPTION [ARGUMENT]")
    print("""
    OPTION:
        -a,
            add an email address to the database;
            this option requires an argument, and it must be the email address;
        -r,
            read the email addresses from the database;
            this option does not require an argument;
            
    """)


def database_ops(option, value=""):
    """
	this function allows you to add
	a new entry in the jokes database
	or read all the entries from it
	"""
    mydb = mysql.connector.connect(host = '127.0.0.1', 
        user = 'root', 
        passwd = 'asd123', 
        database = 'jokes')
    mycursor = mydb.cursor()

    if option == "-a":
        query = "INSERT INTO jokes (email) VALUES ('" + value + "')"
    elif option == "-r":
        query = "SELECT email, reg_date FROM jokes"
    try:
        mycursor.execute (query)
    except:
        print('There was an error when we tried to add the email address in our database')
    else:
        if option == "-a":
            mydb.commit()
            print(mycursor.rowcount, 'record inserted.')
        elif option == "-r":
            for (email, reg_date) in mycursor:
                print(email, 'registered at',reg_date)
        mycursor.close()
        mydb.close()


if len(sys.argv) == 3:
    if sys.argv[1] == "-a": 
        value = sys.argv[2]
        if '@' in value:
            database_ops("-a", value)
        else:
            print('You must specify an email address')
    else:
        usage()
elif len(sys.argv) == 2:
    if sys.argv[1] == "-r":
        database_ops("-r")
    else:
        usage()
else:
    usage()
