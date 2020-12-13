import math
import random

class Player:
    def __init__ (self, letter):
        # letter x or o
        self.letter = letter
    # we want all players to get their move given a game 
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        #Get random valid spot for our next move
        square = random.choice(game.avaiable_moves())
        return square

class HumanPlayer(Player):
    def _init__(self, letter):
        super().__init__(letter)
    
    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input (self.letter + '\'s turn. Input move (0 - 8):')
            # We are going to check that this is a valid value by trying to cast it to an interger 
            # and if it's not, then we say it is invalid. If that spot is not available on the board, we say invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then well done
            except ValueError:
                print ('Invalid square. Try again')
        return val
