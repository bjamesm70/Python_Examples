# list_comp.py

# Lesson 199: List Comprehensions

# - Jim
# (contact info)

print(__file__)

number = int(input("Please enter a number to square: "))

# numbers = range(7)
numbers = [1, 2, 3, 4, 5, 6]

# squares = [number ** 2 for number in numbers]
# "number" below is local to the list comprehension!
squares = [number ** 2 for number in range(1, 7)]

index_position = numbers.index(number)
print(squares[index_position])