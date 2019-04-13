# list_for.py

# Lesson 199: List Comprehensions

# - Jim
# (contact info)

print(__file__)

input_number = int(input("Please enter a number to square: "))
# numbers = range(1, 7)
numbers = [1, 2, 3, 4, 5, 6]

squares = []

for number in numbers:
    
    squares.append(number * number)

index_position = numbers.index(input_number)
print(squares[index_position])
