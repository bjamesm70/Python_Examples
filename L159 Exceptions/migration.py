# migration.py

# Lesson 162: Raising Exceptions

# - Jim
# (contact info)

import ducks

# Create a flock, and some ducks.
flock = ducks.Flock()

donald = ducks.Duck()
daisy = ducks.Duck()
daffy = ducks.Duck()
count_duckula = ducks.Duck()
aflac = ducks.Duck()
rubber = ducks.Duck()
ScroogeMcDuck = ducks.Duck()
percy = ducks.Mallard()
henry = ducks.Penguin()

# Add ducks to the flock.
flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(daffy)
flock.add_duck(count_duckula)
flock.add_duck(henry)    # The Penguin.
flock.add_duck(percy)
flock.add_duck(aflac)
flock.add_duck(rubber)
flock.add_duck(ScroogeMcDuck)

flock.migrate()
