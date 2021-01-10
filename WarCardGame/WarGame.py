# WarGame.py

# This is an automated game.

# To speed up the automated game:
# 'WAR' results in 5 down cards not 3.
# If a player runs out of cards, during a 'WAR',
# that automated player loses the game.

# If no one has won after 1,000 rounds, then
# we call a draw.  This is in a variable: draw_rounds,
# and can be changed.

# -Jim

# from Card import *
from Player import *
from Deck import *

##############
# Game Setup #
##############

# Create the 2 players:

player_one = Player("One")
player_two = Player("Two")

# Create the new, shuffled deck:
new_deck = Deck()

# Call a draw at x rounds:
draw_rounds = 10000

# Number of cards to draw during war:
number_of_cards_during_war = 5  # last 1 up (used for comparison).

# Split the deck b/t the players:

for i in range(len(new_deck.current_deck) // 2):
    player_one.add_cards([new_deck.deal_one_card()])
    player_two.add_cards([new_deck.deal_one_card()])

# We want to keep track of how many rounds the
# game took.
round_counter = 0

game_in_progress = True

while game_in_progress:
    
    # Check for win condition:
    if len(player_one.all_cards) == 0:
        print()
        print("Player One out of cards.")
        print("Player Two wins!")
        
        # GAME OVER!
        game_in_progress = False
        exit()
    
    if len(player_two.all_cards) == 0:
        print()
        print("Player Two out of cards.")
        print("Player One wins!")
        
        # GAME OVER!
        game_in_progress = False
        exit()
    
    # TODO: Remove this at go live.  It's just for testing out the game.
    if round_counter == draw_rounds:
        print("\n")
        print("After {} rounds, no winner.".format(round_counter))
        print("Calling a draw!")
        exit()
    
    # No winner so far.
    # Play the next round:
    
    # As this is an automated game,
    # we are going to print out the game
    # as it goes along.
    round_counter += 1
    print("Currently on round: {}".format(round_counter))
    
    # Clear off the table from the previous round:
    player_one_live_cards = []
    player_two_live_cards = []
    
    # Cards doing battle for this round:
    # Put one card on the table face up:
    player_one_live_cards.append(player_one.remove_one())
    player_two_live_cards.append(player_two.remove_one())
    
    # We will keep drawing cards, for this round,
    # until 1 player wins the round:
    done_with_current_round = False
    
    while not done_with_current_round:
        
        # [-1] This means the top card on the table
        # for this player.  [-1] will work for conditions
        # when 1 card is dealt, or when we are at war.
        
        # Who won the round?
        if player_one_live_cards[-1].value > player_two_live_cards[-1].value:
            # Player 1 won this round.
            
            # Give him/her the cards.
            player_one.add_cards(player_one_live_cards)
            player_one.add_cards(player_two_live_cards)
            # print("player one deck length = {}".format(len(player_one.all_cards)))
            # print("player two deck length = {}".format(len(player_two.all_cards)))
            
            done_with_current_round = True
        
        elif player_one_live_cards[-1].value < player_two_live_cards[-1].value:
            # Player 2 won this round.
            
            # Give him/her the cards.
            player_two.add_cards(player_one_live_cards)
            player_two.add_cards(player_two_live_cards)
            # print("player one deck length = {}".format(len(player_one.all_cards)))
            # print("player two deck length = {}".format(len(player_two.all_cards)))
            
            done_with_current_round = True
        
        else:
            # Tie
            # Go to war.
            print("WAR!")
            
            # Check that both players have enough cards:
            if len(player_one.all_cards) < number_of_cards_during_war:
                # Not enjoy cards to play.
                # Player 2 wins.
                print("Player 1 ran out of cards during war.")
                print("Player 2 wins!")
                exit()
            
            if len(player_two.all_cards) < number_of_cards_during_war:
                # Not enjoy cards to play.
                # Player 2 wins.
                print("Player 2 ran out of cards during war.")
                print("Player 1 wins!")
                exit()
            
            # Draw the cards for both players, and then
            # go back to the top of our loop so that we
            # can perform the tests to see who won.
            
            for i in range(number_of_cards_during_war):
                player_one_live_cards.append(player_one.remove_one())
                player_two_live_cards.append(player_two.remove_one())
            
            # print("Player one cards on the table: ", player_one_live_cards)
            # print("Player two cards on the table: ", player_two_live_cards)
            
            # Going back to the top of the loop now so that we can
            # perform the comparison tests.
