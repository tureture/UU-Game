from board_rep import Board
from mock_rule import mock_rule_check
from input_player import to_coords

# Mocks
from mock_player import*
from mock_endgame import*

class game:
    def __init__(self,p1='Blackplayer',p2='Whiteplayer'):
        self.board = Board()    # Create a board object
        self.turn = 'B'           # Keep track of whose turn it is
        self.nr_turns = 1         # Keep track of the number of turns
        self.game_over = 'False'    # Keep track of whether the game is over
        self.winner = None        # Keep track of who the winner is
        self.inventory = {'B': 9, 'W': 9} # Keep track of the number of pieces each player has
        self.unplaced = {'B': 9, 'W': 9}  # Keep track of the number of pieces each player has yet to place
        self.inputsources = {'B': mock_player(), 'W': mock_player()} # Keep track of the input source for each player
        self.game_phase = 1 #Game phase starts at 1, 2 and 3 are the other phases, phase 4 is the endgame phase.
        self.player = {'B':p1,'W':p2}


    def start(self):
        rule_pass = False
        opponent = {'W':'B','B':'W'}
        self.rule_print()
        start_game = input('Start game? y/n ')
        while self.game_over == "False" and start_game == 'y':
            ###Print rules by calling print rule funciton first itteration if game.turn==1
            
            if self.nr_turns%2 == 1: #game.nr:turns%2 = player
                p = 'B'
                print("Player", p, "turn", self.nr_turns)
                print(self.board)
                print("Inventory: ", self.inventory)
                print(f"Unplaced pieces player {p}: ", self.unplaced[p])
            else: 
                p = 'W'
                print("Player", p, "turn", self.nr_turns)
                print(self.board)
                print("Inventory: ", self.inventory)
                print(f"Unplaced pieces player {p}: ", self.unplaced[p])
                
            if self.unplaced[p] > 0:
                while rule_pass == False:
                    print('Place piece on a vacant spot')
                    move_row = input('Input which row variable = ')
                    move_coloumn = input('Input which coloumn variable = ')
                    move = to_coords([move_row, move_coloumn], p, 'place', self)
                    print(' ')
            
                    if move != None:
                        rule_pass = True
                        move_row = move[0]
                        move_coloumn = move[1]
                
                self.board.set_piece(move_row,move_coloumn,p)
                self.unplaced[p] -= 1
        
                
                
            
            
                
            else: #Phase 2 and 3 starts here
                
                if self.board.count_pieces(p) <= 3: #Phase 3 starts    
                    if  self.game_phase == 2:
                        self.game_phase = 3 
                        self.rule_print()
                    elif self.game_phase == 1:
                        self.game_phase = 2 
                        self.rule_print()
                        self.game_phase = 3 
                        self.rule_print()    
            
                    if self.game_phase == 1: #Phase 3 could have been initizalised before, so only print rules
                        #If phase 1 is over.
                        self.game_phase = 2 #If phase 1 is over. start phase 2.
                        self.rule_print() #Phase 3 starts in mock_rule.py                                               
                    
                
                
                while rule_pass == False:
                    
                    print("Pick piece from board to move")
                    pick_row = input("Pick row ")
                    pick_coloumn = input("Pick coloumn ")
                    
                    if self.game_phase == 2:
                        print('Move to adjecent piece \n')
                    elif self.game_phase == 3:
                        print('Move to any piece \n')
                    move_row = input('Input which row variable = ')
                    move_coloumn = input('Input which coloumn variable = ')
                    
                    moves = to_coords([pick_row, pick_coloumn, move_row, move_coloumn], p, 'move', self)
            
                    print(' ')
            
                    if moves != None:
                        rule_pass = True
                        pick_row = moves[0]
                        pick_coloumn = moves[1]

                        move_row = moves[2]
                        move_coloumn = moves[3]

                self.board.set_piece(moves[0], moves[1], '.')
                self.board.set_piece(moves[2], moves[3], p)
                

            if self.board.find_mill(move_row, move_coloumn, p): 
                
                #itterate over all positions in the board to find what if the peice is 'B' or 'W' and not in a mill
                #Set to 0 Before every itteration to avoid memories
                
                
                free_pieces = [] # Pieces that are not in a mill
                pieces_in_mills = [] #Pieces that are in a milly

                for i in range(0,9):
                    for j in range(0,9):
                        if self.board.get_piece(i,j) == opponent[p] and self.board.find_mill(i, j, opponent[p]):
                            pieces_in_mills.append([i,j])
                    
                        elif self.board.get_piece(i,j) == opponent[p] and not self.board.find_mill(i, j, opponent[p]):
                            free_pieces.append([i,j]) #Pieces that are not in a mill   
                

                print(f"free pieces = {free_pieces}")
                print(f"pieces in mills = {pieces_in_mills}")


                print(self.board)
                rule_pass = False
                
                print(f"Mill formed by {p}")
                print(f"Pick piece from {opponent[p]}'s to remove")

                while rule_pass == False:
                    pick_row = input("Pick row = ")
                    pick_coloumn = input("Pick coloumn = ")
                    pick_move = to_coords([pick_row, pick_coloumn], p, 'remove', self)


                    if pick_move != None:
                        rule_pass =  True
                        pick_row = pick_move[0]
                        pick_coloumn = pick_move[1]              
                        if free_pieces != []: #If there are free pieces, you can only remove free pieces
                            if [int(pick_row),int(pick_coloumn)] in pieces_in_mills:
                                print("You can only remove free pieces, not formed mills")
                                rule_pass =  False 
                                print(self.board)
                                continue 
                    
                    print(' ')
                    
                        
                self.board.set_piece(pick_move[0], pick_move[1], '.')
                self.inventory[opponent[p]] -= 1

            # Check if player has less than 3 pieces left    
            if self.inventory['B'] < 3 or self.inventory['W'] < 3:
                self.game_phase = 'End'  
                self.game_over = True
                if self.inventory['B'] < 3:
                    self.winner = self.player['W']
                else:
                    self.winner = self.player['B']
                self.rule_print()    
                break #Breaks the while loop

            if self.nr_turns >= 300: #If 300 turns have passed, the game is over
                if self.inventory['B'] > self.inventory['W']:
                    self.winner = 'B'
                else:
                    self.winner = 'W' 

            if self.inventory['B'] < 3 or self.inventory['W'] < 3: #If one player has less than 3 pieces, the game is over
                self.game_phase = 'End'  
                self.game_over = True
                if self.inventory['B'] < 3:
                    self.winner = 'W'
                else:
                    self.winner = 'B'
                self.rule_print()    
                break #Breaks the while loop 

            # Check if opponent has legal moves
            if self.inventory[opponent[p]] >3 and self.unplaced[opponent[p]] == 0:
                # Check if opponent has free adjecent pieces
                placed_pieces = self.board.get_pieces(opponent[p])
                free = []
                for piece in placed_pieces:
                    free.append(self.board.get_adjacent_empty_spaces(piece[0],piece[1]))
                if all([len(f) == 0 for f in free]):
                    self.game_phase = 'End' 
                    self.game_over = True
                    self.winner = self.player[p]
                    self.rule_print()
                    break #Breaks the while loop

            self.nr_turns += 1
            rule_pass = False
            
        if start_game == 'n':
            print("Game not started")
            return None
        elif start_game != 'y' and start_game != 'n':
            print("Invalid input, restart")
            return None
        else:
            print(self.board)    
            print("Goodbye!")

            
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