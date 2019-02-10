# get_ints.py

# Lesson 160: Exceptions Challenge

# Example of error handling.
# Handles invalid text inputs,
# and division by 0.  It also
# handles ctl-d (Simulates "End of File" entered).

# ctl-d --> return 1
# divide by 0 --> return 2

# - Jim

import sys    # for the "exit" command.


def get_int(prompt):
    
    while True:
        
        try:
            # int() does NOT convert a float to an int!
            number = int(input(prompt))
            return number
        
        except ValueError:
            print("Invalid number entered.  Please enter an integer.")
        except EOFError:
            # "ctl-d" entered.
            # Exit gracefully but pass an error code of "1".
            sys.exit(1)
        finally:
            print("The 'finally' clause is always executed (unless there is an uncaught exception).")


first_number = get_int("Please input the 1st integer: ")
second_number = get_int("Please input the 2nd integer: ")

try:
    print("{} divided by {} is {}.".format(first_number, second_number, (first_number / second_number)))

except ZeroDivisionError:
    print("Can not divide by 0.")
    # Exit gracefully but pass an error code of "2".
    sys.exit(2)

else:
    print("division successful.")

finally:
    print("The 'finally' clause is always executed (unless there is an uncaught exception).")
    print("This will be executed even if an 'except' block exits the program!")
