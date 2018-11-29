# Modular_Blackjack_Game.py

# From Lesson 108: Blackjack Setup -> Lesson 108.
# Converting the game so that it can be imported
# in a library --> "import Modular_Blackjack_Game"

# Giving credit: the excellent cards are from:

# http://svg-cards.sourceforge.net
# designed by David Bellot

# To find the version of tkinter:
# "print(tkinter.TkVersion)"
# For most other libraries: it's print(libName.__Version__)

# tkinter version 8.6, and a/v is required for .png images.
# B/l 8.6, use .ppm images.

# - Jim

import tkinter  # For graphics.
import random  # For getting a random card

# by calling "shuffle".


#############
# Variables #
#############

extension = "ppm"  # What type of image files are we using (ppm, or png)?
cards = []  # A list of tuples.

# # Scores at start of game:
# player_score = 0
# dealer_score = 0

# All these are lists of tuples.
deck = []  # It will be the active deck w/ cards being taken out.
dealer_hand = []
player_hand = []


#############
# Functions #
#############


def load_images(card_images):
    global extension  # Use the global variable.  Don't create a local copy.
    
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']
    
    # tkinter version 8.6, and higher can handle "png" files.
    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'
    
    # Loop through the suits retrieve all the cards.
    # "png" images are stored in "cards_png".
    # "ppm" images are stored in "cards_ppm".
    # File names are: value_suit.ext --> 5_spade.png
    for suit in suits:
        
        # First process the numbered cards
        for number in range(1, 11):
            # "number" needs to be a string in the step below.
            name = 'cards_{2}/{0}_{1}.{2}'.format(str(number), suit, extension)
            
            # Load the image into memory.
            image = tkinter.PhotoImage(file=name)
            
            # Save the image to our dictionary.
            card_images.append((number, image,))
        
        # Pull in the face cards.
        for face in face_cards:
            name = 'cards_{2}/{0}_{1}.{2}'.format(face, suit, extension)
            
            # Load the image into memory.
            image = tkinter.PhotoImage(file=name)
            
            # Save the image to our dictionary.
            
            card_images.append((10, image,))


def deal_a_card(input_frame):
    # Take the top card off of the random deck.
    # Note: pop() takes the last element.
    # Note: pop(0) takes the 0th element.
    next_card = deck.pop(0)
    
    # Add the card's image to the frame.
    # tkinter.Labels can hold text, or images!
    # Apparently, pack is easier if your frame just has 1 image.
    tkinter.Label(input_frame, image=next_card[1], relief='raised').pack(side='left')
    
    # Return the top card.
    return next_card


def calculate_score_hand(input_hand):
    # Sums up the total score for the given list.
    # Only 1 ace will have an 11 per hand.
    # Also, the ace will be converted to 1 if the hand would bust
    # with it being 11.
    
    total_score = 0
    any_aces = False  # Keep tract if we have any aces.
    
    # Loop through the card list, and sum up the hand
    # converting aces to 1 as needed.
    for card in input_hand:
        
        card_value = card[0]
        
        # In the deck, aces are stored with a value of 1.
        if (card_value == 1) and (not any_aces):
            any_aces = True
            card_value = 11
        
        total_score += card_value
        
        # See if we went bust, and can fix it by converting an ace to 1.
        if (total_score > 21) and (any_aces):
            total_score -= 10
            any_aces = False
    
    # Done with for loop.
    # Return the calculated score:
    return total_score


def deal_to_dealer():
    # Creating this function because: You assign an action to
    # a tkinter object via "command=functName".  If you try
    # functName(val1, val2), then functName(val1, val2) is
    # executed, and the result is assigned to "command".
    
    # Add a card, and calculate the dealer's new total.
    
    # Update the dealer's score.
    dealer_score = calculate_score_hand(dealer_hand)
    
    # The dealer must hit at 16, or b/l.
    while dealer_score < 17:
        dealer_hand.append(deal_a_card(dealer_card_frame))
        
        # Remember to update the total score, or you
        # will be stuck here forever.
        dealer_score = calculate_score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    
    # See who won.
    # Get the player's hand:
    player_score = calculate_score_hand(player_hand)
    
    if player_score > 21:
        result_text.set("Dealer wins!")
    elif (dealer_score > 21) or (dealer_score < player_score):
        result_text.set("Player wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
    else:
        # A tie
        result_text.set("Draw!")


# def deal_to_player():
#     # Creating this function because: You assign an action to
#     # a tkinter object via "command=functName".  If you try
#     # functName(val1, val2), then functName(val1, val2) is
#     # executed, and the result is assigned to "command".
#
#     # Use the global variables.
#     # Otherwise, the function will create a local var
#     # as soon as you change the values.
#     global player_score, player_has_an_ace
#
#     # Remember "deal_a_card" returns a tuple.
#     card_value = deal_a_card(player_card_frame)[0]
#
#     # If the player has 0 aces, then the 1st ace starts
#     # with a value of 11.  Later, if we go bust, then we
#     # convert the ace to a 1.
#     if (card_value == 1) and (not player_has_an_ace):
#         card_value = 11
#         player_has_an_ace = True
#
#     player_score = player_score + card_value
#
#     # Has the player gone bust?
#     # If yes, do they have an ace?
#     if (player_score > 21) and (player_has_an_ace):
#         # Yes.
#         # Convert the ace from '11' to '1'.
#         player_score = player_score - 10
#         player_has_an_ace = False
#
#     # Update the score on the gui.
#     player_score_label.set(player_score)
#
#     # See if the player has bust:
#     if player_score > 21:
#         # Yes.
#
#         result_text.set("Dealer wins!")
#     print(locals())


def deal_to_player():
    player_hand.append(deal_a_card(player_card_frame))
    
    # Note: local var.  No shadowing
    player_score = calculate_score_hand(player_hand)
    
    player_score_label.set(player_score)
    
    if player_score > 21:
        result_text.set("Dealer Wins!")


def initial_deal():
    # Show starting cards.
    # We don't "deal_to_dealer()" b/c that tries to
    # see who wins.
    deal_to_player()

    dealer_hand.append(deal_a_card(dealer_card_frame))
    dealer_score_label.set(calculate_score_hand(dealer_hand))

    deal_to_player()


def new_game():
    # Creates a new game.
    
    # We need to clear some global variables:
    global dealer_card_frame, player_card_frame
    global dealer_hand, player_hand
    global deck
    
    # Remove, and create the dealer's frame, and player's frame that hold the cards.
    # This action will reset each to be empty.
    
    # Dealer's cards:
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
    
    # Player's cards:
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)
    
    # Reset the Game Result text at the top of the game:
    result_text.set("")
    
    # Clear, and create a new deck.
    deck = []
    
    # list(inputList) creates a new list from the input list.
    deck = list(cards)
    shuffle_deck()
    
    dealer_hand = []
    player_hand = []
    
    initial_deal()
    

def shuffle_deck():
    # Needed b/c button's command option can't take parameters.
    random.shuffle(deck)


def play():
    # Used to play the game if this file is imported as a library file.

    initial_deal()

    ###########################
    # Display the main window #
    ###########################

    main_window.mainloop()


####################
# End of Functions #
####################


##########################
# Create the main window #
##########################

main_window = tkinter.Tk()

# Set up the screen, and frames for the dealer, and player.

main_window.title("Blackjack")
main_window.geometry("640x480")
main_window.configure(background='green')

###################
# Text to display #
###################

result_text = tkinter.StringVar()
result = tkinter.Label(main_window, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

####################
# Background Frame #
####################

card_frame = tkinter.Frame(main_window, relief="sunken", borderwidth=1, background="green")

# When you add the card_frame to the main window, add it to
# row, and column location, have it stick East, and West, and
# have it occupy 2 rows (up/down), and 3 columns (left/right).
card_frame.grid(row=1, column=0, sticky="ew", rowspan=2, columnspan=3)

###################
# Vars for dealer #
###################

dealer_score_label = tkinter.IntVar()
dealer_header = tkinter.Label(card_frame, text="Dealer", background="green", fg="white")
dealer_header.grid(row=0, column=0)
dealer_score = tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white")
dealer_score.grid(row=1, column=0)

####################################
# Frame to hold the dealer's cards #
####################################

dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

#######################
# Vars for the player #
#######################

player_score_label = tkinter.IntVar()
# player_has_an_ace = False    # Does the player have an ace?  Ace can be 1, or 11.

player_header = tkinter.Label(card_frame, text="Player", background="green", fg="white")
player_header.grid(row=2, column=0)
player_score_text = tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white")
player_score_text.grid(row=3, column=0)

####################################
# Frame to hold the player's cards #
####################################

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

##################
# Adding buttons #
##################

# Our frame for the buttons is 3 columns wide.
button_frame = tkinter.Frame(main_window)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

# Create buttons to be in the "button_frame", and then
# locate w/i the button frame.

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_to_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_to_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=2)

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle_deck)
shuffle_button.grid(row=0, column=3)

####################################
# Pull in the images for the cards #
####################################

load_images(cards)

###############################
# Create a new, shuffled deck #
###############################

# Clear, and create a new deck.
deck = []

# list(inputList) creates a new list from the input list.
deck = list(cards)
shuffle_deck()

##################
# Start the game #
##################

# If this is not imported in a library call,
# the start the game.
if (__name__ == "__main__"):
    play()
