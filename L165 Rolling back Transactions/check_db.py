# check_db.py

# Lesson 171: Displaying Time in Different Timezones

# - Jim
# (Contact Info)

import sqlite3

db_conn = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# From: https://www.sqlite.org/lang_datefunc.html
# strftime(format, timestring, modifier, modifier, modifier, ...)
# %f = fractional seconds: SS.SSS
#for row in db_conn.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
#                           "history.account, history.amount FROM history ORDER BY history.time"):
for row in db_conn.execute("SELECT * FROM localhistory"):
    print(row)


# Remember to close a db when done:
db_conn.close()