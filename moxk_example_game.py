# Chose a phase 1 2 or 3
#Can not take away 2 pieceses if 2 mills are formed!
from board_rep import Board
from game_loop import game_loop
from mock_rule import mock_rule_check
from input_player import to_coords


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
            move = to_coords([move_row, move_coloumn],board, p, 'place', game)
            print(' ')
            
            if move != None:
                rule_pass = True
                move_row = move[0]
                move_coloumn = move[1]
        board.set_piece(move[0],move[1],p)
        game.unplaced[p] -= 1
 
          
      
    
        
    else: #Phase 2 and 3 starts here
        
        if board.count_pieces(p) <= 3: #Phase 3 starts    
            if  game.game_phase == 2:
                game.game_phase = 3 
                game.rule_print()
            elif game.game_phase == 1:
                game.game_phase = 2 
                game.rule_print()
                game.game_phase = 3 
                game.rule_print()    
        
        if game.game_phase == 1: #Phase 3 could have been initizalised before, so only print rules
            #If phase 1 is over.
            game.game_phase = 2 #If phase 1 is over. start phase 2.
            game.rule_print() #Phase 3 starts in mock_rule
            


        while rule_pass == False:
            
            print("Pick piece from board to move")
            pick_row = input("Pick row ")
            pick_coloumn = input("Pick coloumn ")
            
            if game.game_phase == 2:
                print('Move to adjecent piece \n')
            elif game.game_phase == 3:
                print('Move to any piece \n')
            move_row = input('Input which row variable = ')
            move_coloumn = input('Input which coloumn variable = ')

            moves = to_coords([pick_row, pick_coloumn, move_row, move_coloumn], board, p, 'move', game)
            
            print(' ')
            
            if moves != None:
                rule_pass = True
                pick_row = moves[0]
                pick_coloumn = moves[1]

                move_row = moves[2]
                move_coloumn = moves[3]
                
        game.board.set_piece(moves[0], moves[1], '.')
        game.board.set_piece(moves[2], moves[3], p)
        
    


    if board.find_mill(move_row, move_coloumn, p): 
        #itterate over all positions in the board to find what if the peice is 'B' or 'W' and not in a mill
        #Set to 0 Before every itteration to avoid memories
        
        free_pieces = [] # Pieces that are not in a mill
        pieces_in_mills = [] #Pieces that are in a milly

        for i in range(0,9):
            for j in range(0,9):
                if board.get_piece(i,j) == opponent[p] and board.find_mill(i, j, opponent[p]):
                    pieces_in_mills.append([i,j])
               
                elif board.get_piece(i,j) == opponent[p] and not board.find_mill(i, j, opponent[p]):
                    free_pieces.append([i,j]) #Pieces that are not in a mill   
                

        print(f"free pieces = {free_pieces}")
        print(f"pieces in mills = {pieces_in_mills}")

        print(board)
        rule_pass = False
        
        print(f"Mill formed by {p}")
        print(f"Pick piece from {opponent[p]}'s to remove")

        while rule_pass == False:
            pick_row = (input("Pick row = "))
            pick_coloumn = input("Pick coloumn = ")
            pick_move = to_coords([pick_row, pick_coloumn], board, p, 'remove', game)
            

            if pick_move != None:
                rule_pass =  True
                pick_row = pick_move[0]
                pick_coloumn = pick_move[1]              
                if free_pieces != []: #If there are free pieces, you can only remove free pieces
                    if [int(pick_row),int(pick_coloumn)] in pieces_in_mills:
                        print("You can only remove free pieces, not formed mills")
                        rule_pass =  False 
                        print(board)
                        continue 
                   
            
            print(' ')


             
        game.board.set_piece(pick_move[0], pick_move[1], '.')
        game.inventory[opponent[p]] -= 1
        
        
    #Wining conditions
    
    if game.nr_turns >= 300: #If 300 turns have passed, the game is over
        if game.inventory['B'] > game.inventory['W']:
            game.winner = 'B'
        else:
            game.winner = 'W'
            
            
    if game.inventory['B'] < 3 or game.inventory['W'] < 3: #If one player has less than 3 pieces, the game is over
        game.game_phase = 'End'  
        game.game_over = True
        if game.inventory['B'] < 3:
            game.winner = 'W'
        else:
            game.winner = 'B'
        game.rule_print()    
        break #Breaks the while loop  

    # Check if opponent has legal moves, if no, game is over
    if game.inventory[opponent[p]] >3 and game.unplaced[opponent[p]] == 0: 
        # Check if opponent has free adjecent pieces
        placed_pieces = board.get_pieces(opponent[p])
        free = []
        print(placed_pieces)
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