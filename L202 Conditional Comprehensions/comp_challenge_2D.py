# comp_challenge_2D.py

# Lesson 211: timeit Continued and Challenge

# Timing our previous code.
# We will make string variables out of our
# commands, and plug those vars into the
# the "timeit.timeit()" function.

# - Jim
# (Contact Info)

import timeit    # For timing functions.
import gc        # For managing garbage collection.

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}


def nested_loop():
    result = []
    for sorted_location in sorted(locations):
        # Create an empty list for eac location.
        # It will contain the locations that connect to it.
        exits_to_location = []
        
        for current_location in exits:
            
            # Is the location in the list of exist for your current location
            if sorted_location in exits[current_location].values():
                # Yes.
                # Add it to the list.
                exits_to_location.append((current_location, locations[current_location]))
        
        # List compiled for the "sorted_location".
        # Save it.
        result.append(exits_to_location)
    
    # Walk through the result before returning:
    # Just for timing the code "nested_gen()".
    # However, we need all the functions to perform
    # the same actions to compare apples to apples.
    for x in result:
        pass
    
    return result


def loop_comp():
    result = []
    for sorted_location in sorted(locations):
        exits_to_location = [(current_location, locations[current_location])
                             for current_location in exits
                             if sorted_location in exits[current_location].values()]
        result.append(exits_to_location)

    # Walk through the result before returning:
    # Just for timing the code "nested_gen()".
    # However, we need all the functions to perform
    # the same actions to compare apples to apples.
    for x in result:
        pass

    return result


def nested_comp():
    exits_to_location = [[(current_location, locations[current_location])
                          for current_location in exits
                          if sorted_location in exits[current_location].values()]
                         for sorted_location in sorted(locations)]
    
    # enumerate() goes through a list, and returns (counter, next item in list)
    # 0, exits_to_location[0]
    # 1, exits_to_location[1]
    # 2, exits_to_location[2]
    # etc.
    # for index, loc in enumerate(exits_to_location):
    #     print("Locations leading to {}:".format(index), end='\t')
    #     print(loc)

    # Walk through the result before returning:
    # Just for timing the code "nested_gen()".
    # However, we need all the functions to perform
    # the same actions to compare apples to apples.
    for x in exits_to_location:
        pass

    return exits_to_location


def nested_gen():
    exits_to_location = ([(current_location, locations[current_location])
                          for current_location in exits
                          if sorted_location in exits[current_location].values()]
                         for sorted_location in sorted(locations))
    
    # enumerate() goes through a list, and returns (counter, next item in list)
    # 0, exits_to_location[0]
    # 1, exits_to_location[1]
    # 2, exits_to_location[2]
    # etc.
    # for index, loc in enumerate(exits_to_location):
    #     print("Locations leading to {}:".format(index), end='\t')
    #     print(loc)
    
    # Walk through the result before returning:
    # Just for timing the code "nested_gen()".
    # However, we need all the functions to perform
    # the same actions to compare apples to apples.
    for x in exits_to_location:
        pass
    
    return exits_to_location


print(nested_comp())
print(nested_loop())
print(loop_comp())
#print(nested_gen())

# "timeit.timeit()" runs in its own area (name space).
# As a result, it will NOT know about variables in our main programs.
# Therefore, pass all of our globally defined variables to "timeit.timeit()" via:
# globals = globals()

# Default number of runs = 1,000,000 which can take a long time as we have print statements.
# Reducing to 1,000.

# Complete definition of timeit.timeit:
# timeit(stmt="pass", setup="pass", timer=default_timer,
#            number=default_number, globals=None)
# Note: You can pass it parameters as positional, or specify their names.

setup_var = """gc.enable()"""
result_3 = timeit.timeit(nested_comp, setup=setup_var, globals=globals(), number=10000)
result_1 = timeit.timeit(nested_loop, setup=setup_var, globals=globals(), number=10000)
result_2 = timeit.timeit(loop_comp, setup=setup_var, globals=globals(), number=10000)
result_4 = timeit.timeit(nested_gen, setup=setup_var, globals=globals(), number=10000)

print("Nested loop:\t{}".format(result_1))
print("Loop, and comp:\t{}".format(result_2))
print("Nested comp:\t{}".format(result_3))
print("Nested gen:\t\t{}".format(result_4))
