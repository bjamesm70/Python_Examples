# Deck.py

# Our deck class.

# - Jim

import random  # To shuffle the deck.
import Card  # Our card class.


class Deck():
    
    def __init__(self):
        
        # Creates a new deck, and shuffles it afterward.
        
        self.current_deck = []
        
        # Create all the cards for the "new deck".
        # NOT SHUFFLED!
        for suit in Card.suits:
            
            for rank in Card.ranks:
                self.current_deck.append(Card.Card(suit, rank))
        
        # Shuffle the new deck.
        self.shuffle_me()
    
    def shuffle_me(self):
        # Shuffle a deck.
        # Used when we have a new deck out of the wrapper.
        
        # Note: random.shuffle is IN PLACE!
        random.shuffle(self.current_deck)
    
    def deal_one_card(self):
        # Removes the top card from the deck.
        # Note: pop(): Defaults to removing the last card.
        return self.current_deck.pop(0)
