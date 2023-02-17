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
        self.game_phase = 1 #Game phase starts at 1, 2 and 3 are the other phases, phase 4 is the endgame phase.
        self.pieces_in_mills = {'B':[],'W':[]} #Keeps track of the pieces that are free to move, i.e. not in a mill formation
        self.free_pieces = {'B':[],'W':[]} #Keeps track of the pieces that are free to move, i.e. not in a mill formation

        

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
            
    def rule_print(self): #Function that prints rules of the game, called with base rules in p1, as well as rule changes in p2 and p3 respectively
        if self.game_phase == 1:
            print('Welcome to VegaSoft latest game installment \n')
            print('The rules of the game are as follows: \n')
            print("The objective of the game is to form rows of three by placing or moving your pieces into rows of three's, called mills\n")
            print('Forming a mill allows you to remove a piece from your opponent.\n')
            print('If your opponent has a mill formed and has other pieces left, you may not take a piece from that mill formation \n')
            print('The game continues with each player alternating placing pieces, forming mills and removing opponent pieces until all starting pieces have either been placed or removed from the game \n')
            print('Once this is done, the first phase of the game (the "placing" phase) ends and the "moving" phase begins:\n')
            print('In the "moving" phase, each player alternates moving pieces to adjacent positions, trying to break and reform mills to continously remove the opponents pieces from the game \n')
            print('This carries on until one player is reduced to 3 pieces left, initiating the flying phase of the game for that player \n')
            print('In the "flying" phase, the player with only 3 pieces left is now allowed to move their pieces to any unoccupied position on the board, instead of just adjacent positions.\n')
            print('Good luck! Have fun! \n')
        elif self.game_phase == 2:
            print('All pieces placed, entering "moving" phase. Now give a piece position followed by an adjacent position you would like to move it to on your turn: \n')

        elif self.game_phase == 3: #Should probably only be the player with 3 pieces left that enters the phase
            p3_player = 'Black' #placeholder
            print(f'Player reduced to three pieces left, entering "flying" phase. {p3_player} is now allowed to move pieces from any position to anywhere on the board \n')

        elif self.game_phase == 'End':
            print(f'Game over! {self.winner} wins! \n') #{check_win()} check_win would need the turn limit case for this to work, othertwise could just make an if statement for this case