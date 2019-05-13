# Conditional_Comprehension.py

# Lesson 202: Conditional Comprehensions

# It's common to put an "if" clause inside of a "for" loop.
# You can do that inside of a list comprehension, too.
# It is called "Conditional Comprehensions".

# Format: myList = [ var1 for var1 in inputList if_clause ]
# Example: no_spam = [ meal for meal in menu if 'spam' not in meal ]
# Notes:
# 1) Only add var1 to the list if the "if" condition is true.
# 2) "if" is a filter only.

# Goes over "else" cause in a list conditional.

# - Jim
# (Contact Info)

menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["eggs"],
    ["eggs", "bacon"],
    ["chicken", "chips"]]

# Find all the meals w/o 'spam' in them.
for meal in menu:
    if 'spam' not in meal:
        print(meal)

print("*" * 40)

without_spam = [meal for meal in menu if 'spam' not in meal and 'chicken' not in meal]

for meal in without_spam:
    print(meal)

print("*" * 40)

# It must have spam, or eggs, and not have both bacon, and sausage together.
fussy_meals = [meal for meal in menu if ('spam' in meal or 'eggs' in meal)
               and not ("bacon" in meal and "sausage" in meal)]

# You could have used:
# and ("bacon" not in meal or "sausage" not in meal)]

for fussy in fussy_meals:
    print(fussy)

meals = []

# We don't want "spam"!
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("a meal was skipped")

for i in meals:
    print(i)

print("*" * 40)

# no_spam = [item for item in menu if not "spam" in item]
no_spam = [item for item in menu if "spam" not in item]

for i in no_spam:
    print(i)

x = 15
result = "twelve" if x == 12 else "unknown"
print(result)

no_spam_2 = [item if "spam" not in item else "a meal was skipped" for item in menu]

for i in no_spam_2:
    print(i)

for item in menu:
    print(item, "contains chicken" if "chicken" in item
                else "contains bacon" if "bacon" in item
                else "contains egg")

print("*" * 40)

# A set is a list where all elements are unique.
# Items can be added, and removed but not altered.
# Sets have {}.
items = set()    # Empty Set.

# Get a list of all the food items on the menu.
for meal in menu:
    for item in meal:
        items.add(item)

print(items)

print("*" * 40)

for meal in menu:
    
    for item in items:
        
        if item in meal:
            
            print("'{}' contains '{}'.".format(meal, item))
            break    # Don't search any more in this meal.

for x in range(0, 31):
    
    fizzbuzz = "fizz buzz" if (x % 15 == 0) else \
                "fizz" if (x % 3 == 0) else \
                "buzz" if (x % 5 == 0) else \
                str(x)
    print(x, fizzbuzz)
