# Card.py

# Our card class.

# - Jim

# Constants:

suits = ("Hearts", "Clubs", "Diamonds", "Spades")  # Tuple = Read-only list

# Strings allowed for the ranks.
# Tuple = Read-only list
ranks = ("Two",
         "Three",
         "Four",
         "Five",
         "Six",
         "Seven",
         "Eight",
         "Nine",
         "Ten",
         "Jack",
         "Queen",
         "King",
         "Ace")

# Number value for each string.
# Access it as: values[<some_card>.rank]
# Example: values[two_hearts.rank]
values = {"Two": 2,
          "Three": 3,
          "Four": 4,
          "Five": 5,
          "Six": 6,
          "Seven": 7,
          "Eight": 8,
          "Nine": 9,
          "Ten": 10,
          "Jack": 11,
          "Queen": 12,
          "King": 13,
          "Ace": 14}


class Card():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        # Return Example: "5 of hearts"
        return self.rank + " of " + self.suit
