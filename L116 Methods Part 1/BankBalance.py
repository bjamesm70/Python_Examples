# BankBalance.py

# Lesson 116: Methods Part 1

# - Jim

import pytz
import datetime


###########
# Classes #
###########


class Account:
    """ A simple account class with _balance """
    
    # Class function for finding the time:
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    
    def __init__(self, name, balance):
        
        self._name = name
        self._balance = balance
        self._transaction_list = []
        print("Account created for: " + self._name)
        # Store the transaction as a tuple.
        self._transaction_list.append((Account._current_time(), self._balance))
        self.show_balance()
    
    def deposit(self, amount):
        
        # Check for positive values.
        if amount > 0:
            self._balance += amount
            self.show_balance()
            # Store the transaction as a tuple.
            self._transaction_list.append((Account._current_time(), amount))
            
    def withdrawal(self, amount):
        
        # Check for positive values.
        if amount < 0:
            print("Please provide a positive amount to withdraw.")
            return
        
        # Check for enough $$ in the account.
        if self._balance < amount:
            print("You can not withdraw: {}".format(amount))
            self.show_balance()
            return
        
        self._balance -= amount
        self.show_balance()
        # Store the transaction as a tuple.
        self._transaction_list.append((Account._current_time(), -amount))
    
    def show_balance(self):
        
        print("The _balance is : {}".format(self._balance))
        
    def show_transactions(self):
        
        tran_type = ""
        for date, amount in self._transaction_list:
            if amount >= 0:
                tran_type = "deposited"
                
            else:
                tran_type = "withdrawn"
                amount = -amount
            
            print("{:9} {} on {} (local time was {}".format(amount, tran_type, date, date.astimezone()))
  
          
###############
# End Classes #
###############


if __name__ == "__main__":
    tim = Account("Tim", 0)
    #tim.show_balance()
    
    tim.deposit(1000)
    #tim.show_balance()
    
    tim.withdrawal(500)
    #tim.show_balance()
    
    tim.show_transactions()
    
    steph = Account("Steph", 800)
    steph.deposit(100)
    steph.withdrawal(200)
    steph.show_transactions()
    
    print(steph.__dict__)