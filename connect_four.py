#NOTES:

# Built the game Connect 4 during Hackbright Academy's Prep Course 01/2020 - 02/2020
# 01/13/2020 is project presentation day 
# First coding project 

###################################################################

#PSEUDOCODE: 

#Create my game board and identify any variables I will need 
#Functions that I need (display board, player move, check for win, next turn, play game)

#Display board prints my board 
#Player move handles the current player's move
#Check winner checks which player has four tokens connected
#Check for win checks the game board to see there are four tokens connected (horizontally, vertically, or diagonally)
#Next turn handles what to do for the next turn 
#Play game calls each function and allows both players to play a game 

###################################################################

import sys

class NewGame:
    """Game for playing connect four."""

    
    def __init__(self):
        """Initialize variables & create board."""

        self.turn = 0
        self.player = "Red"
        self.token = " X "
        self.winner = "   "
        
        self.board = [
            ["   ", "   ", "   ","   ", "   ", "   ", "   "],
            ["   ", "   ", "   ","   ", "   ", "   ", "   "],
            ["   ", "   ", "   ","   ", "   ", "   ", "   "],
            ["   ", "   ", "   ","   ", "   ", "   ", "   "],
            ["   ", "   ", "   ","   ", "   ", "   ", "   "],
            ["   ", "   ", "   ","   ", "   ", "   ", "   "]
            ]
        
            
    def display_board(self):
        """Shows the game board for connect four."""

        for row in range(len(self.board)):
            print("|", end="")
            for column in range(len(self.board[row])):
                print(self.board[row][column], end="|")
            print("\n-----------------------------")
        print(" (1) (2) (3) (4) (5) (6) (7) \n")


    def player_move(self):
        """Handles the current players move."""

        while True:
            location = input("Choose which column to drop your token (1-7)\n")
            if ((len(location) != 1) or (location not in ["1","2","3","4","5","6","7"])):
                print("Choose a column 1-7\n")
                continue
            elif self.board[0][(int(location)-1)] != "   ":
                print("Spot Taken.\n")
                continue
            else:    
                break
        
        drop = int(location) - 1
        for row in range((len(self.board) - 1), -1, -1):
            if self.board[row][drop] == "   ":
                self.board[row][drop] = self.token
                break
            else:
                continue
    

    def check_winner(self, red_test, yellow_test):
        """Checking if either of the players have won."""

        if red_test == 4:
            self.display_board()
            print("\n\nRed Wins")
            sys.exit(0)
        elif yellow_test == 4:
            self.display_board()
            print("\n\nWinner: Yellow")
            sys.exit(0)
        #Board Full
        elif "   " not in self.board[0]:
            self.display_board()
            print("\n\nScratch Game: No one wins.")
            sys.exit(0)
    

    def check_win(self):
        """Handle checking wins on the game board."""

        #Horizontal Win
        for row in self.board:
            red_test = 0
            yellow_test = 0
            for column in row:
                if column == "   ":
                    red_test = 0
                    yellow_test = 0
                elif column == " X ":
                    red_test +=1
                    yellow_test = 0
                elif column == " O ":
                    yellow_test +=1
                    red_test = 0
                self.check_winner(red_test, yellow_test)

        #Vertical Win
        for c in range(7):
            red_test = 0
            yellow_test = 0
            for r in range(6):
                if self.board[r][c] == "   ":
                    red_test = 0
                    yellow_test = 0
                elif self.board[r][c] == " X ":
                    red_test += 1
                    yellow_test = 0
                elif self.board[r][c] == " O ":
                    yellow_test += 1
                    red_test = 0
                self.check_winner(red_test, yellow_test)

        #Diagonal Up Win /
        for ru in range((len(self.board) - 1), 2, -1):
            red_test = 0
            yellow_test = 0
            for du in range(4):
                if self.board[(ru-du)][du] == "   ":
                    red_test = 0
                    yellow_test = 0
                elif self.board[(ru-du)][du] == " X ":
                    red_test += 1
                    yellow_test = 0
                elif self.board[(ru-du)][du] == " O ":
                    yellow_test += 1
                    red_test = 0
                self.check_winner(red_test, yellow_test)

        #Diagonal Down Win \
        for rd in range(3):
            red_test = 0
            yellow_test = 0
            for dd in range(4):
                if self.board[(rd+dd)][dd] == "   ":
                    red_test = 0
                    yellow_test = 0
                elif self.board[(rd+dd)][dd] == " X ":
                    red_test += 1
                    yellow_test = 0
                elif self.board[(rd+dd)][dd] == " O ":
                    yellow_test += 1
                    red_test = 0
                self.check_winner(red_test, yellow_test)

        
    def next_turn(self):
        """Handles the next turn."""

        self.display_board()
        if self.turn == 0:
            print()
            self.player = "Red"
            print(f"{self.player} First")
        else:
            if (self.turn % 2) == 0:
                self.player = "\n\nRed"
                self.token = " X "
            else:
                self.player = "\n\nYellow"
                self.token = " O "
                
            print(f"\n{self.player}'s Turn {self.token[1]}")
            
        
        self.player_move()
        self.check_win()
        
        self.turn+=1
    


print("Welcome to Connect 4!\n\nRed Token: x\nYellow Token: o\n")
print("Instructions:\n- To win this game connect four of your tokens\n\n\n")
connect4_game = NewGame()

while True:
    connect4_game.next_turn()


###################################################################

#WHAT'S NEXT FOR MY PROJECT:
#Diagonal Down doesn't work 
#Maybe make a different design for the game board 
#Have the computer play as the second player (import random)
