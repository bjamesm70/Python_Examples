# ExceptionHandlingExamples.py

# Lesson 159: Exceptions

# - Jim
#(Contact Info)

def factorial(n):
    # n! can also be defined as n * (n - 1)!

    """ Calculates n! recursively """
    
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print("")

try:
    print(factorial(10))
    print(1000/0)
    print("hi")
except (RecursionError, OverflowError):
    # A/v are the errors we want to capture.
    # B/l is the code to run if we encounter them.
    # Note: if we capture the an error, the program
    # will continue on after the 'try/except' block.
    # Note: OverflowError very unlikely but putting it
    # in an an example of how to list > 1 error on a line.
    print("This program can not calculate factorials that large.")
except ZeroDivisionError:
    print("What are you doing dividing by '0'?!")

print("\nAfter 'try/except', program ending.")