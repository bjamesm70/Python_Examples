# main.py

# Lesson 128: Getters and Setters

# The main file for our game.

# - Jim
# (Contact Info)

from player import Player

tim = Player("Tim")

print(tim.name)
print(tim.lives)

tim.lives -= 1
print(tim.lives)

tim.lives -= 1
print(tim.lives)

tim.lives -= 1
print(tim.lives)

tim.lives -= 1
print(tim.lives)

print(tim)

tim.lives = 9
print(tim.lives)

tim.level += 5
print(tim)

tim.level = 0
print(tim)

tim.level -= 1
print(tim)

tim.score = 500
print(tim)