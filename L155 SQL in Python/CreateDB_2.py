# CreateDB_2.py

# Lesson 156: Connections, Cursors, and Transactions
# Using commit(), and replacements w/i a db query.

# - Jim
#(contact info)

import sqlite3

# Using the same db file, and table from the previous backup.
db_conn = sqlite3.connect("contacts.sqlite")

# # The following returns a cursor object:
# results = db_conn.execute("SELECT * FROM contacts")

# An update string to run later.
new_email = "new@update.com"
phone = input("Please enter the phone number: ")
#update_sql = "UPDATE contacts SET email = '{}' WHERE contacts.phone = {}".format(new_email, phone)
update_sql = "UPDATE contacts SET email = ? WHERE contacts.phone = ?"

# Note: When you use place holders/variable substitution (as a/v), python 3
# sanitizes your input against injection attacks.

print("'update_sql' var is:", update_sql)

cursor_object = db_conn.cursor()
#cursor_object.execute(update_sql)
cursor_object.execute(update_sql, (new_email, phone))

print("{} rows updated.".format(cursor_object.rowcount))

print()
print("Are connections the same? ", cursor_object.connection == db_conn )
print()

# Save the changes, to the DB, via the cursor object:
cursor_object.connection.commit()

# Close the cursor.
cursor_object.close()

for name, phone, email in db_conn.execute("select * from contacts"):
    
    print(name)
    print(phone)
    print(email)
    print("=" * 30)

# Save the changes, to the DB, via the connection object:
db_conn.commit()

db_conn.close()
