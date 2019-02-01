# CheckDB.py

# Lesson 156: Connections, Cursors, and Transactions

# Python script to check the values in our database
# file.

# - Jim
#(contact info)

import sqlite3

# Open the connection to the DB file.
db_conn = sqlite3.connect("contacts.sqlite")

input_name = input("Enter a name to lookup: ")


# Note: The comma is needed in the tuple!
result = db_conn.execute("SELECT * FROM contacts WHERE name LIKE ? ", (input_name,) )

for name, phone, email in result:
    print("{0:<20}: {1:<12}: {2}".format(name, phone, email))

# for row in db_conn.execute("select * from contacts"):
#
#     print(row)

db_conn.close()