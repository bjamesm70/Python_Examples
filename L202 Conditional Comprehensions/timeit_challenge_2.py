# timeit_challenge_2.py

# Lesson 212: timeit Challenge

# 2nd way to do the timeit.

# - Jim
# (contact info)

# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.

import timeit  # for timing our functions.
import gc      # garbage collector


def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

 
setup_var = """gc.enable()"""

# result_3 = timeit.timeit(nested_comp, setup=setup_var, globals=globals(), number=10000)
# result_1 = timeit.timeit(nested_loop, setup=setup_var, globals=globals(), number=10000)
# result_2 = timeit.timeit(loop_comp, setup=setup_var, globals=globals(), number=10000)
# result_4 = timeit.timeit(nested_gen, setup=setup_var, globals=globals(), number=10000)

# print(timeit.timeit(     fact_test, setup=setup_var, globals=globals(), number=10000))
# print(timeit.timeit(factorial_test, setup=setup_var, globals=globals(), number=10000))

# Only run the timeit's if the program is run, and not imported as a library.
if __name__ == "__main__":
    print(timeit.timeit("x = fact(130)", setup="from __main__ import fact", number=10000))
    print(timeit.timeit("y = factorial(130)", setup="from __main__ import factorial", number=10000))

    # timeit.repeat(...) runs "timeit.timeit" x number of times.  It defaults to 5.
    print(timeit.repeat("x = fact(130)", setup="from __main__ import fact", number=10000))
    print(timeit.repeat("y = factorial(130)", setup="from __main__ import factorial", number=10000))