# main.py

# Lesson 128: Getters and Setters

# The main file for our game.

# - Jim
# (Contact Info)

from player import Player
from enemy import Enemy, Troll, Vampyre, VampyreKing  # Importing more than 1 class.

tim = Player("Tim")

print(tim.name)
print(tim)

random_monster = Enemy("Basic Enemy", 12, 1)
print(random_monster)

print("")

ugly_troll = Troll("Pugg")

print("Ugly Troll: {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another Troll: {}".format(another_troll))
another_troll.take_damage(18)
print("Another Troll: {}".format(another_troll))


brother = Troll("Urg")

print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

vamp1 = Vampyre("Vlad")
print(vamp1)

vamp1.take_damage(5)
print(vamp1)

print("-" * 40)
another_troll.take_damage(30)
print(another_troll)

while vamp1._alive:
    vamp1.take_damage(1)

KingOfLA = VampyreKing("Eric")
print(KingOfLA)

for i in range(7):
    KingOfLA.take_damage(20)
    print(KingOfLA)

