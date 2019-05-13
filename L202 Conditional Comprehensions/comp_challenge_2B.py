# comp_challenge_2B.py

# Lesson 208: Nested Comprehensions Challenge

# - Jim
# (Contact Info)

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

print("*****************")
print("NESTED FOR LOOPS.")
print("*****************")

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
    # Print it:
    print("Locations leading to {}:".format(sorted_location), end='\t')
    print(exits_to_location)

print()

print("--------------------------------------")
print("List comprehension inside a 'for' loop")
print("--------------------------------------")

exits_to_location = []

for sorted_location in sorted(locations):
    exits_to_location = [(current_location, locations[current_location])
                         for current_location in exits
                         if sorted_location in exits[current_location].values()]
    print("Locations leading to {}:".format(sorted_location), end='\t')
    print(exits_to_location)

print()

print("*********************")
print("Nested Comprehensions")
print("*********************")

exits_to_location = [[(current_location, locations[current_location])
                      for current_location in exits
                      if sorted_location in exits[current_location].values()]
                     for sorted_location in sorted(locations)]

# enumerate() goes through a list, and returns (counter, next item in list)
# 0, exits_to_location[0]
# 1, exits_to_location[1]
# 2, exits_to_location[2]
# etc.
for index, loc in enumerate(exits_to_location):
    print("Locations leading to {}:".format(index), end='\t')
    print(loc)