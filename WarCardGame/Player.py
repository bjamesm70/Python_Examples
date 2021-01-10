# Player.py

# Defines the "Player" class.
# Holds the player's cards, and
# has functions to add, and remove
# cards from the player's hand.

# - Jim


class Player():
    
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        # Removes the TOP card, and returns it.
        return self.all_cards.pop(0)
    
    def add_cards(self, cards_to_add: list):
        self.all_cards.extend(cards_to_add)
        pass
    
    def __str__(self):
        return "Player {} has {} cards.".format(self.name, len(self.all_cards))
