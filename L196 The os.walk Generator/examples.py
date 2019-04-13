# examples.py

# Lesson 199: List Comprehensions

# - Jim
# (contact info)

print(__file__)

text = "What have the Romans ever done for us?"

capitals = [char.upper() for char in text]
print(capitals)

words = [word.upper() for word in text.split()]
print(words)

# The following is not needed:
lc_words = [word for word in text.split()]

# Use this instead:
lc_words = text.split()
print(lc_words)
