from mock_rule import mock_rule_check

def input_player(game, p, type_of_move):
    if type_of_move == 'place':
        print('Place piece on a vacant spot')
        move_row = input('Input which row variable = ')
        move_coloumn = input('Input which coloumn variable = ')
        return to_coords([move_row, move_coloumn],game.board, p, 'place')
        
    elif type_of_move == 'move':
        print("Pick piece from board to move")
        pick_row = input("Pick row ")
        pick_coloumn = input("Pick coloumn ")
        
        if game.game_phase == 2:
            print('Move to adjecent piece \n')
        elif game.game_phase == 3:
            print('Move to any piece \n')
        move_row = input('Input which row variable = ')
        move_coloumn = input('Input which coloumn variable = ')
        return to_coords([pick_row, pick_coloumn, move_row, move_coloumn], game.board, p, 'move')
    
    elif type_of_move == 'remove':
        pick_row = input("Pick row = ")
        pick_coloumn = input("Pick coloumn = ")
        return to_coords([pick_row, pick_coloumn], game.board, p, 'remove')


def input_coord(moves):
    #moves = [int , str]
    [row, column] = moves
    move = None

    if [row, column] == [7, 'a']: 
        move = [0, 0]
    if [row, column] == [7, 'd']: 
        move = [0, 1]
    if [row, column] == [7, 'g']:
        move = [0, 2]
    if [row, column] == [6, 'b']: 
        move = [1, 0]
    if [row, column] == [6, 'd']:
        move = [1, 1]
    if [row, column] == [6, 'f']: 
        move = [1, 2]
    if [row, column] == [5, 'c']: 
        move = [2, 0]
    if [row, column] == [5, 'd']: 
        move = [2, 1]
    if [row, column] == [5, 'e']: 
        move = [2, 2]
    if [row, column] == [4, 'a']:
        move = [3, 0]
    if [row, column] == [4, 'b']: 
        move = [3, 1]
    if [row, column] == [4, 'c']: 
        move = [3, 2]
    if [row, column] == [4, 'e']: 
        move = [3, 3]
    if [row, column] == [4, 'f']: 
        move = [3, 4]
    if [row, column] == [4, 'g']: 
        move = [3, 5]
    if [row, column] == [3, 'c']: 
        move = [4, 0]
    if [row, column] == [3, 'd']: 
        move = [4, 1]
    if [row, column] == [3, 'e']: 
        move = [4, 2]
    if [row, column] == [2, 'b']: 
        move = [5, 0]
    if [row, column] == [2, 'd']: 
        move = [5, 1]
    if [row, column] == [2, 'f']: 
        move = [5, 2]
    if [row, column] == [1, 'a']: 
        move = [6, 0] 
    if [row, column] == [1, 'd']: 
        move = [6, 1]
    if [row, column] == [1, 'g']: 
        move = [6, 2]
    if move == None:
        print("Invalid coordinate")
    return move



def to_coords(fst, board, p, type_of_move):
    move = None
    
    if isntValid(fst):
        if move == None:
            rule_check = mock_rule_check(board, fst, p, type_of_move)
        
            if rule_check[0] != 'True':
                print(rule_check[1])
                print(board)
                move = None
            return move
        
    fst[0] = int(fst[0])
    fst[1] = fst[1]

    if fst[0] > 7 or fst[1] > 'g':
        rule_check = mock_rule_check(board, [100,100], p, type_of_move)
        if rule_check[0] != 'True':
                print(rule_check[1])
                print(board)
                move = None
        
    if type_of_move == 'place' or type_of_move == 'remove':
        move = input_coord(fst)
        if move != None:
            rule_check = mock_rule_check(board, move, p, type_of_move)

            if rule_check[0] != 'True':
                print(rule_check[1])
                print(board)
                move = None
        return move

    if type_of_move == 'move':
        fst[2] = int(fst[2])
        fst[3] = fst[3]
        move_from = input_coord([fst[0],fst[1]])
        move_to = input_coord([fst[2], fst[3]])
        
        if move_from != None and move_to!= None: 
            move = move_from + move_to
            print(move)
            rule_check = mock_rule_check(board, move, p, type_of_move)

            if rule_check[0] != 'True':
                print(rule_check[1])

                print(board)
                move = None
        return move


def isnt_int(s):
    try:
        int(s)
        return False
    except ValueError:
        return True

def isnt_str(s):
    try:
        str(s)
        return False
    except ValueError:
        return True
    
def isntValid(s):
    # Valid [int, str] or [int, str, int, str]
    if len(s) == 2:
        if isnt_int(s[0]) or isnt_str(s[1]):
            return True
    if len(s) == 4:
        if isnt_int(s[0]) or isnt_str(s[1]) or isnt_int(s[2]) or isnt_str(s[3]):
            return True
    return False

