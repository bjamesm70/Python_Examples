# tz_check.py

# Lesson 173: Challenge

# - Jim
# (Contact Info)

import sqlite3
import pytz
import pickle

db_conn = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# From: https://www.sqlite.org/lang_datefunc.html
# strftime(format, timestring, modifier, modifier, modifier, ...)
# %f = fractional seconds: SS.SSS
#for row in db_conn.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
#                           "history.account, history.amount FROM history ORDER BY history.time"):
for row in db_conn.execute("SELECT * FROM history"):
    utc_time = row[0]
    pickled_zone = row[3]
    zone = pickle.loads(pickled_zone)
    # zone = pytz.timezone("America/Chicago")
    # zone = pytz.timezone("EST")
    
    local_time = pytz.utc.localize(utc_time).astimezone(zone)
    
    print("{}\t{}\t{}".format(utc_time, local_time, local_time.tzinfo))


# Remember to close a db when done:
db_conn.close()
