# Chose a phase 1 2 or 3
#Can not take away 2 pecieses if 2 mills are formed!!! 
from board_rep import Board
from game_loop import game_loop
from mock_rule import mock_rule_check


game = game_loop()
board = Board()
rule_pass = False
opponent = {'W':'B','B':'W'}
while game.game_over == "False":
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
            print('Place pecie on a vaccen spot')
            move_row = input('Input which row variable = ')
            move_coloumn = input('Input which coloumn variable = ')
            rule_check = mock_rule_check(board,[move_row,move_coloumn],p,'place')
        
            if rule_check[0] != 'True':
                print(rule_check[1])
            else:
                rule_pass = True
        
        board.set_piece(move_row,move_coloumn,p)
        game.unplaced[p] -= 1
 
          
        
      
    
        
    else: #Phase 2 and 3 starts here
        while rule_pass == False:
            
            print("Pick pecie from borad to move\n")
            pick_row = input("Pick row ")
            pick_coloumn = input("Pick coloumn ")
            
            print('Move to adjecent pecie \n')
            move_row = input('Input which row variable = ')
            move_coloumn = input('Input which coloumn variable = ')
            rule_check = mock_rule_check(board,[pick_row,pick_coloumn,move_row,move_coloumn],p,'move')
            
            if rule_check[0] != 'True':
                print(rule_check[1])
            else: 
                rule_pass =  True
        game.board.set_piece(pick_row, pick_coloumn, '.')
        game.board.set_piece(move_row, move_coloumn, p)
        
    
    if game.inventory['B'] < 3 or game.inventory['W'] < 3:
        game.game_over = True
        if game.inventory['B'] < 3:
            game.winner = 'W'
        else:
            game.winner = 'B'

    if board.find_mill(move_row, move_coloumn, p):
        print(board)
        rule_pass = False
        
        print("Mill formed.")
        print("Pick piece from board to remove\n")

        while rule_pass == False:
            pick_row = int(input("Pick row "))
            pick_coloumn = int(input("Pick coloumn "))
            rule_check = mock_rule_check(board,[pick_row,pick_coloumn,move_row,move_coloumn],p,'remove')
            if rule_check[0] != 'True':
                print(rule_check[1])
            else:
                rule_pass =  True
                
        game.board.set_piece(pick_row, pick_coloumn, '.')
        game.inventory[opponent[p]] -= 1 
            
    game.nr_turns += 1
    rule_pass = False
    

print("The game is over. The winner is ", game.winner)

#For adjensent, use  input of pecie you want to move as input
#