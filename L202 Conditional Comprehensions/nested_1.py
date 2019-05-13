# nested_1.py

# Lesson 207: Nested Comprehensions

# Burger Menus.

# - Jim
# (Contact Info)

burgers = ['beef', 'chicken', 'spicy bean']
toppings = ['cheese', 'egg', 'beans', 'spam']

# Nested listed comprehension:
#meals = [(burger, topping) for burger in burgers for topping in toppings]
for meal in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meal)
    
print("*" * 40)

# "for" loop version:

# # Empty out the menu list.
# meals = []
# for burger in burgers:
#     for topping in toppings:
#         meals.append((burger, topping))
#
# for item in meals:
#     print(item)

# Apparently, it starts with the outside 'for' loop 1st.
for nested_meal in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(nested_meal)

print("*" * 40)

for nested_meal in [[(burger, topping) for topping in toppings] for burger in burgers]:
    print(nested_meal)