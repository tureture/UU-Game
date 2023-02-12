from board_rep import Board
from game_loop import game_loop

def mock_rule_check(board, move, turn, type_of_move, game):
    if isnt_int(move[0]) or isnt_int(move[1]):
        return ['False', 'Input was not a number']
    
    elif board.inside_board(move[0],move[1])==False:
        return ['False', 'Move is outside of board']
    
    elif board.get_piece(move[0], move[1]) != '.' and type_of_move == 'place':
        return ['False', 'That space is already occupied.']

    elif type_of_move == 'move':
        if isnt_int(move[2]) or isnt_int(move[3]):
            return ['False', 'Input was not a number']
            
        elif board.inside_board(move[2],move[3])==False:
            return ['False', 'Move is outside of board']

        if board.count_pieces(turn) > 3: #Phase 3 starts
            if  game.game_phase == 2 or game.game_phase == 1:
                game.game_phase = 3 
                game.rule_print()
            if move[2:] in board.get_adjacent_spaces(move[0],move[1]):
                if board.get_piece(move[2], move[3]) != '.':
                    return ['False', 'That space is already occupied.']
            else:   
                return ['False', 'Non-adjacent']
        
        if board.get_piece(move[0], move[1]) == '.':
            return ['False', 'That space is empty.']
        elif board.get_piece(move[0], move[1]) != turn:
            return ['False', 'You must move one of your pieces.']
        if board.get_piece(move[2], move[3]) != '.':
            return ['False', 'That space is already occupied.']
        elif board.get_piece(move[2], move[3]) == '.':
            return ['True', 'Valid move.']             

    elif type_of_move == 'remove':
        opponent = {'B':'W','W':'B'}
        turn = opponent[turn] #Remove opponents pecie
        if board.get_piece(move[0], move[1]) == '.':
            return ['False', 'That space is empty.']
        elif board.get_piece(move[0], move[1]) != turn:
            return ['False', 'You cannot remove one of your own pieces.']
        elif board.get_piece(move[0], move[1]) == turn:
            return ['True', 'Valid move.']
    

        

    else:
        return ['True','Valid move.']
    
def isnt_int(s):
    try:
        int(s)
        return False
    except ValueError:
        return True
    
    ##