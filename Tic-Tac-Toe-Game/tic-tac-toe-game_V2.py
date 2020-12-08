# tic-tac-toe-game_V2.py

# From Jose Portilla's udemy class.
# I changed up the code to fit my
# style as best I could.

# - Jim

###########
# Imports #
###########


import random  # To decide who goes 1st.


#############
# Functions #
#############

def display_board(board):
    print("\n")
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("- - -")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("- - -")
    print(board[7] + "|" + board[8] + "|" + board[9])


def player_input():
    """
    For choosing if a player takes 'X', or 'O'.
    OUTPUT = Player 1 Marker, Player 2 Marker
    """
    
    marker = ""
    
    while marker not in ["X", "O"]:
        marker = input("Player 1, choose 'X', or 'O': ").upper()
    
    player1 = marker
    
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    
    return player1, player2


def place_marker(board, marker, position):
    # Updates 1 element on the board.
    # Valid positions are 1-9.
    board[position] = marker


def win_check(board, mark):
    # WIN TIC-TAC-TOE?
    # Check all rows to see if any row has the same marker.
    # Check all cols to see if any col has the same marker.
    # Check the 2 diagonals if either has the same marker.
    
    # Check each row:
    if (mark == board[1] == board[2] == board[3]) or \
            (mark == board[4] == board[5] == board[6]) or \
            (mark == board[7] == board[8] == board[9]):
        
        # 1 row is the same.
        return True
    
    # Check each column:
    elif (mark == board[1] == board[4] == board[7]) or \
            (mark == board[2] == board[5] == board[8]) or \
            (mark == board[3] == board[6] == board[9]):
        
        # 1 column the same.
        return True
    
    # Check the 2 diagonals.
    elif (mark == board[1] == board[5] == board[9]) or \
            (mark == board[3] == board[5] == board[7]):
        
        # 1 diagonal the same:
        return True
    
    else:
        
        # No match.
        return False


def choose_first():
    # Randomly choose who goes 1st.
    
    # Note: "randint is inclusive of the end range.
    # Unusual for python.
    coin_flip = random.randint(0, 1)
    
    if coin_flip == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    # See if a spot, on the board, is free.
    return board[position] == " "


def full_board_check(board):
    # Are all the positions taken:
    # " " is used for an empty space.
    print((" " in board))
    return not (" " in board)


def player_choice(board):
    # Ask the player for a position to put put their marker,
    # and check that it's available.
    
    # Start out w/ an invalid position:
    position = 0
    
    # Check for invalid position, or not free space.
    while not (position in range(1, 10) and space_check(board, position)):
        # Invalid location.
        
        # Either not a valid position, or not a free square:
        position = int(input("Choose a position: (1-9): "))
    
    # If you are here, then the user select a valid position, and
    # it's free.  Return the position:
    return position


def replay():
    choice = "Blah"
    
    # Keep asking until the player responds with a
    # response starting with "y", or "n".
    while choice[0].upper() not in ["Y", "N"]:
        choice = input("Play Again (Y/N)? ")
    
    # Return True, or False.
    return choice[0].upper() == "Y"


#################
# Play the game #
#################

print("Welcome to TIC TAC TOE!\n")

# Yes, I know the "while test" is always
# True.  We break out of it when we ask
# the players to replay, and they say "no".
while True:
    # Start a new game.
    # 1) Set up a blank board
    # 2) Choose markers
    # 3) Choose 1st player --> It's random.
    
    # Set up the blank board:
    game_board = [" "] * 10  # Spots 0-9, ignoring 0.
    # We need to set spot 0 to something other " "
    # b/c we check to see if there are no spaces
    # let in 1-9 by looking for a " ".
    game_board[0] = "*"
    
    # Choose markers:
    p1_marker, p2_marker = player_input()
    print("P1", p1_marker)
    print("P2", p2_marker)
    
    # Random who will go 1st:
    turn = choose_first()
    print(":" + turn + ":" + " will go first.")
    
    # Play the game:
    game_on = True
    
    while game_on:
        # Take turns until the end.
        
        # Display updated board.
        display_board(game_board)
        
        # Reset the marker, and position choose.
        marker = " "
        position = 0
        
        # I'm not a fan of repeated code.
        # However, this is how he did it,
        # and he is far smarter than I.
        if turn == "Player 1":
            # Player 1 chooses.
            print("{}'s turn.".format(turn))
            position = player_choice(game_board)
            marker = p1_marker
        
        else:
            # Player 2 chooses.
            # Not a fan of repeated code.
            # I cleaned up most of it.
            print("{}'s turn.".format(turn))
            position = player_choice(game_board)
            marker = p2_marker
        
        # Update the board after the choice.
        place_marker(game_board, marker, position)
        
        # Check for a winner.
        if win_check(game_board, marker):
            # We have a winner.
            
            # Show the winner:
            display_board(game_board)
            
            print("{} has won!!".format(turn))
            
            # Done with this game.
            game_on = False
        
        # Is the game a tie?
        elif full_board_check(game_board):
            # Full board.  Tie game.
            display_board(game_board)
            print("Tie game!!")
            
            # Done with this game.
            game_on = False
        
        else:
            # Next player's turn.
            if turn == "Player 1":
                turn = "Player 2"
            else:
                turn = "Player 1"
    
    # Current game over.
    if not replay():
        # Get out of the game.
        break
