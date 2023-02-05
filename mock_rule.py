from board_rep import Board

def mock_rule_check(board, move, turn, type_of_move):
    if board.get_piece(move[0], move[1]) != '.' and type_of_move == 'place':
        return ['False', 'That space is already occupied.']
    elif type_of_move == 'move':
        if board.get_piece(move[0], move[1]) == '.':
            return ['False', 'That space is empty.']
        elif board.get_piece(move[0], move[1]) != turn:
            return ['False', 'You must move one of your pieces.']
        if board.get_piece(move[2], move[3]) != '.':
            return ['False', 'That space is already occupied.']
        elif board.get_piece(move[2], move[3]) == '.':
            return ['True', 'Valid move.']
    elif type_of_move == 'remove':
        if board.get_piece(move[0], move[1]) == '.':
            return ['False', 'That space is empty.']
        elif board.get_piece(move[0], move[1]) == turn:
            return ['False', 'You cannot remove one of your pieces.']
        elif board.get_piece(move[0], move[1]) != turn:
            return ['True', 'Valid move.']
    else:
        return ['True','Valid move.']