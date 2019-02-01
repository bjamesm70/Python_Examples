# CreateDB.py

# Lesson 155: SQL in Python

# Intro to SQLite3 in python

# Note on "cursors:
# - Cursors use "generators" to get 1 line of
# output to handle the fact that the output,
# from an sqlite command, could be 1,000,000 lines.  long.
#
# Note: As a result, you can't go back to previous records!
# So, a "cursor" is a pointer to the list of results!

# - Jim
# (Contact Info)

import sqlite3

# "connect" will create a DB file if it does not
# exist, or open(connect) to the file if it does.
db_conn = sqlite3.connect("contacts.sqlite")

db_conn.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")

# Add a record:
db_conn.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6546548, 'tim@email.com')")
db_conn.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@myemail.com')")

# Display the results:

cursor = db_conn.cursor()

results = cursor.execute("select * from contacts")

#print(isinstance(results,))
#cursor.execute("select * from contacts")

# Note: If you don't give a variable for the output
# data to go into, then the output is held in the
# cursor object; in our case: 'cursor'.

# Alternate way to do the a/v:
# - From python 3's documentation: (https://docs.python.org/3.7/library/sqlite3.html#connection-objects)
#
# execute(sql[, parameters])
# This is a nonstandard shortcut that creates a cursor object,
# by calling the cursor() method, calls the cursor’s execute()
# method with the parameters given, and returns the cursor.

# From me: So, it creates a temp 'cursor' object,
# runs the command, and returns the results.  This
# means that you don't need to create a cursor
# object if you don't want to.

##results = db_conn.execute("select * from contacts")

# To download all the results:
#mylist = cursor.fetchall()

# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())

#for row in cursor:
#for row in results:
for name, phone, email in results:
    
    print("{0:<20}: {1:<12}: {2}".format(name, phone, email))

# As this is a 'cursor', the cursor advances.
# The a/v 'for' loop walked us through all the results.
# No output.
for name, phone, email in results:
    print("{0:<20}: {1:<12}: {2}".format(name, phone, email))

# All done.  Close the save the data, and the connections.
cursor.close()

db_conn.commit()
db_conn.close()