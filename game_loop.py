from board_rep import Board

# Mocks
from mock_player import*
from mock_endgame import*

class game_loop:
    def __init__(self):
        self.board = Board()    # Create a board object
        self.turn = 'B'           # Keep track of whose turn it is
        self.nr_turns = 1         # Keep track of the number of turns
        self.game_over = 'False'    # Keep track of whether the game is over
        self.winner = None        # Keep track of who the winner is
        self.inventory = {'B': 9, 'W': 9} # Keep track of the number of pieces each player has
        self.unplaced = {'B': 9, 'W': 9}  # Keep track of the number of pieces each player has yet to place
        self.inputsources = {'B': mock_player(), 'W': mock_player()} # Keep track of the input source for each player

    def input(self):
        return self.inputsources[self.turn]

    def set_inputsource(self, player, source):
        self.inputsources[player] = source
    
    def next_turn(self):
        # Update the turn
        # Update the number of turns
        pass

    def game_loop(self):
        while self.game_over == 'False':
            move = self.input()
            
            self.game_over = mock_end(self.board, self.nr_turns)
            self.next_turn()
        self.print_winner()
            
#Share