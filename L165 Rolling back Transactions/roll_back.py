# roll_back.py

# Lesson 165: Rolling back Transactions

# Because floats, in python, may not be
# stored exactly as entered, we are going
# store the money as ints of pennies
# (100 * balance).

# So, "amount" hold the amount of pennies
# to add, and remove.  The "deposit", and
# "withdrawal" functions work in pennies,
# not dollars.

# - Jim
# (Contact Info)

import sqlite3
import datetime    # For time stamps.
import pytz        # For time stamps.

# Open the DB file for reading/writing:
# "detect_types=sqlite3.PARSE_DECLTYPES" --> sqlite doesn't know what a TIMESTAMP is.
# So, it stores it as a string.  The "PARSE_DECLTYPES" will convert the info back into
# a TIMESTAMP for us.
# See: "https://docs.python.org/3.7/library/sqlite3.htm" for more info.
db_conn = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

db_conn.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, "
                "balance INTEGER NOT NULL)")

db_conn.execute("CREATE TABLE IF NOT EXISTS history(time TIMESTAMP NOT NULL, "
                "account TEXT NOT NULL, "
                "amount INTEGER NOT NULL, "
                "PRIMARY KEY (time, account))")

# From: http://www.sqlitetutorial.net/sqlite-create-table/:
# The primary key of the table: is a column, or a group of
# columns that uniquely identifies a row in the table.  In
# case the primary key consists of multiple columns, you
# need to use "table constraint" instead of PRIMARY KEY
# "column constraint".

db_conn.execute("CREATE VIEW IF NOT EXISTS localhistory AS "
                "SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
                "history.account, history.amount FROM history ORDER BY history.time")

#####################
# Class Definitions #
#####################


class Account(object):

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())

    def __init__(self, name: str, opening_balance: int = 0):
    
        # 1st, check to see if the user is already in our DB.
        
        # Returns a pointer to a data stream.
        cursor = db_conn.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()
        cursor.connection.commit()

        # Was the name found?
        if row:
            # Yes.
            self.name, self._balance = row
            print("Retrieved record for {}.  ".format(self.name), end='')
        
        else:
            # New user!
            # Put the data into the DB, and then save the
            # DB immediately.
            self.name = name
            self._balance = opening_balance
            
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
        
            print("Account created for {}.  ".format(self.name), end='')
        
        # In either case, show the balance.
        self.show_balance()
    
    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = Account._current_time()
        
        try:
            db_conn.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            db_conn.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
        
        except sqlite3.Error:
            # "sqlite3.Error" is the parent class for all sqlite3 exceptions.
            db_conn.rollback()
        else:
            # No errors encountered.
            # Save the data.
            # Update the balance.
            
            # Notes:
            # 1) You can't use "finally" to update the balance
            # b/c finally is executed if there are
            # no errors, or if there are caught exceptions.
            # 2) The "else" clause goes after all "except" clauses,
            # and b/4 the "finally" clause.
            db_conn.commit()
            self._balance = new_balance
        finally:
            # The "finally" block is always executed (unless there is an uncaught
            # exception).  This means that, if code, in the "except" block, says to
            # terminate the program, the "finally" block will still be executed!
            # db_conn.commit()
            pass
        
    def deposit(self, amount: int) -> float:
    
        if amount > 0.0:
            # new_balance = self._balance + amount
            # deposit_time = Account._current_time()
            # db_conn.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db_conn.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
            # db_conn.commit()
            # self._balance = new_balance
            self._save_update(amount)
            
            print("{:.2f} deposited".format(amount/100))
    
        return self._balance/100

    def withdraw(self, amount: int) -> float:
    
        if 0 < amount < self._balance:
            # We have a valid amount to withdraw.
            
            # new_balance = self._balance - amount
            # withdrawal_time = Account._current_time()
            #
            # db_conn.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db_conn.execute("INSERT INTO history VALUES(?, ?, ?)", (withdrawal_time, self.name, -amount))
            # db_conn.commit()
            # self._balance = new_balance
            
            self._save_update(-amount)
            
            print("{:.2f} withdrawn".format(amount/100))
            
            return amount/100
            
        else:
            print("The amount must be greater than 0, and no more than your account balance.")
            return 0.0
    
    def show_balance(self):
        
        print("Balance on account {} is {:.2f}.".format(self.name, self._balance/100))


##################
# End of Classes #
##################
    
# For testing out the code.
# This section does not get executed if this file is imported
# as a library.

if __name__ == '__main__':
    
    # Note deposits, and withdrawals are
    # in pennies not dollars!
    
    john = Account("John")    # Testing for the default value of 0.0.
    
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    
    john.withdraw(30)
    john.withdraw(0)
    
    john.show_balance()
    
    terry = Account("TerryJ")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)
    michael = Account("Michael")
    terryG = Account("TerryG")
    
    db_conn.close()
