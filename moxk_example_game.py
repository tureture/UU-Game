# Chose a phase 1 2 or 3
#Can not take away 2 pieceses if 2 mills are formed!
from board_rep import Board
from game_loop import game_loop
from mock_rule import mock_rule_check


game = game_loop()
board = Board()
rule_pass = False
opponent = {'W':'B','B':'W'}
game.rule_print()
start_game = input('Start game? y/n ')
while game.game_over == "False" and start_game == 'y':
    ###Print rules by calling print rule funciton first itteration if game.turn==1
    board = game.board
    
    if game.nr_turns%2 == 1: #game.nr:turns%2 = player
        p = 'B'
        print("Player", p, "turn", game.nr_turns)
        print(board)
        print("Inventory: ", game.inventory)
        print(f"Unplaced pieces player {p}: ", game.unplaced[p])
    else: 
        p = 'W'
        print("Player", p, "turn", game.nr_turns)
        print(board)
        print("Inventory: ", game.inventory)
        print(f"Unplaced pieces player {p}: ", game.unplaced[p])
        
    if game.unplaced[p] > 0:
        while rule_pass == False:
            print('Place piece on a vacant spot')
            move_row = input('Input which row variable = ')
            move_coloumn = input('Input which coloumn variable = ')
            print(' ')
            rule_check = mock_rule_check(board,[move_row,move_coloumn],p,'place',game)
        
            if rule_check[0] != 'True':
                print(rule_check[1])
                print(board)
            else:
                rule_pass = True
        
        board.set_piece(move_row,move_coloumn,p)
        game.unplaced[p] -= 1
 
          
        
      
    
        
    else: #Phase 2 and 3 starts here
        
        if game.game_phase == 1: #Phase 3 could have been initizalised before, so only print rules
            #If phase 1 is over.
            game.game_phase = 2 #If phase 1 is over. start phase 2.
            game.rule_print() #Phase 3 starts in mock_rule
            
        
        
        while rule_pass == False:
            
            print("Pick piece from board to move")
            pick_row = input("Pick row ")
            pick_coloumn = input("Pick coloumn ")
            
            print('Move to adjecent piece \n')
            move_row = input('Input which row variable = ')
            move_coloumn = input('Input which coloumn variable = ')
            print(' ')
            rule_check = mock_rule_check(board,[pick_row,pick_coloumn,move_row,move_coloumn],p,'move',game)
            
            if rule_check[0] != 'True':
                print(rule_check[1])
                print(board)
            else: 
                rule_pass =  True
        game.board.set_piece(pick_row, pick_coloumn, '.')
        game.board.set_piece(move_row, move_coloumn, p)
        
    
    if game.inventory['B'] < 3 or game.inventory['W'] < 3:
        game.game_phase = 'End'  
        game.game_over = True
        if game.inventory['B'] < 3:
            game.winner = 'W'
        else:
            game.winner = 'B'
        game.rule_print()    
        break #Breaks the while loop  

    if board.find_mill(move_row, move_coloumn, p):
        print(board)
        rule_pass = False
        
        print(f"Mill formed by {p}")
        print(f"Pick piece from {opponent[p]}'s to remove")

        while rule_pass == False:
            pick_row = int(input("Pick row = "))
            pick_coloumn = int(input("Pick coloumn = "))
            print(' ')
            rule_check = mock_rule_check(board,[pick_row,pick_coloumn,move_row,move_coloumn],p,'remove',game)
            if rule_check[0] != 'True':
                print(rule_check[1])
                print(board)
            else:
                rule_pass =  True
                
        game.board.set_piece(pick_row, pick_coloumn, '.')
        game.inventory[opponent[p]] -= 1

    # Check if opponent has legal moves
    if game.inventory[opponent[p]] >3 and game.unplaced[opponent[p]] == 0:
        # Check if opponent has free adjecent pieces
        placed_pieces = board.get_pieces(opponent[p])
        free = []
        for piece in placed_pieces:
            free.append(board.get_adjacent_empty_spaces(piece[0],piece[1]))
        if all([len(f) == 0 for f in free]):
            game.game_phase = 'End' 
            game.game_over = True
            game.winner = p
            game.rule_print()
            break #Breaks the while loop

    game.nr_turns += 1
    rule_pass = False
    
if start_game == 'n':
    print("Game not started")
elif start_game != 'y' and start_game != 'n':
    print("Invalid input, restart")
else:    
    print("Goodbye!")

#For adjensent, use  input of piece you want to move as input
####