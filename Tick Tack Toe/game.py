import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # We will use a single list to rep 3 x 3 board
        self.current_winner = None # Keep track of winner!

    def print_board (self):
        for row in [self.board[i*3: (i + 1)*3] for i in range(3)]:
            print ('| ' + ' | ' .join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us which number corresponds to which box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range (3)]

        for row in number_board:
            print('| ' + ' | ' .join(row) + ' |')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' '] # the entire bottom code can be summarized using line 19. 
        #moves = []
        #for (i,spot) in enumerate(self.board):
            # ['x', 'x' , 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #    if spot == ' ':
        #        moves.append (i)
        #return (moves)
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares (self):
        return len(self.available_moves()) # or can use self.board.count(' ')

    def make_move (self, square, letter):
        # if valid move, then make the move (assign a square to letter)
        # then return true. if Invalid, then return false.
        if self.board[square] == ' ':    
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner (self,square,letter):
        # Winner if 3 in a row anywhere. check all the possibilities
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind+ 1 )* 3]
        if all ([spot == letter for spot in row]):
            return True

        # Check Column
        col_ind = square % 3
        Column = [self.board[col_ind + i*3] for i in range (3) ]
        if all ([spot == letter for spot in Column]):
            return True
        
        # Check Diagonals
        # But only if the square is an even number (0,2,4,6,8)
        # These are the only moves avaiable to win using diagonals

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all ([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all ([spot == letter for spot in diagonal2]):
                return True 




def play(game, x_player, o_player, print_game = True):
    # returns the winner of the game! Or None for a tie 
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # starting letter move
    # iterate while the game still has empty squares
    # (we dont have to worry about winner because we'll just return that which breaks the loop)
    while game.empty_squares():
        # get the moves from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

    # Now define a function to make a move
        if game.make_move ( square, letter, ):
            if print_game:
                print (letter + f' make a move to square {square}')
                game.print_board()
                print ('') # just empty line

            if game.current_winner:
                if print_game:
                    print (letter + ' wins ! ')

                return letter

        # After we make a move, have to alternate letters
        
        letter = 'O' if letter == 'X' else 'X' # A summarized version of the bottom line (Switches player)
        #if letter == 'X':
        #    letter = 'O'
        #else:
        #    letter = 'X'   

    if print_game:
        print ('It is a tie! ')

        # But what if won?

if __name__ == '__main__':
    x_player = HumanPlayer('X') 
    o_player = RandomComputerPlayer ('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)