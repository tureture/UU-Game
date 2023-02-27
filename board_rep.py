# Class for representation of a board state in the game


class Board:
    def __init__(self):
        self.board = [['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.','.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.']]

    def __str__(self):
        
        print('7 ', self.board[0][0], '-' * 12, self.board[0][1], '-' * 12, self.board[0][2])
        print( '  ','|', ' ' * 12, '|', ' ' * 12, '|')
        print('6 ','| ', self.board[1][0], '-' * 9, self.board[1][1], '-' * 9, self.board[1][2], ' |')
        print('  ','|   ' * 2, ' ' * 5, '|', ' ' * 5, '   |' * 2)
        print('5 ','|   ' * 2, self.board[2][0], '-' * 3, self.board[2][1], '-' * 3, self.board[2][2], '   |' * 2)
        print('  ','|   ' * 3, ' ' * 5, '   |' * 3)
        print('4 ',self.board[3][0], '-', self.board[3][1], '-', self.board[3][2], ' ' * 11, self.board[3][3], '-', self.board[3][4], '-', self.board[3][5])
        print('  ','|   ' * 3, ' ' * 5, '   |' * 3)
        print('3 ','|   ' * 2, self.board[4][0], '-' * 3, self.board[4][1], '-' * 3, self.board[4][2], '   |' * 2)
        print('  ','|   ' * 2, ' ' * 5, '|', ' ' * 5, '   |' * 2)
        print('2 ','| ', self.board[5][0], '-' * 9, self.board[5][1], '-' * 9, self.board[5][2], ' |')
        print('  ','|', ' ' * 12, '|', ' ' * 12, '|')
        print('1 ',self.board[6][0], '-' * 12, self.board[6][1], '-' * 12, self.board[6][2])
        print('  ', 'a ',' b ', '  c  ', '  d  ', '  e  ', ' f ', ' g')
        return 'Board current state \n'
        
    def get_board(self):
        return self.board

    def set_board(self, board):
        self.board = board

    def get_piece(self, row, col):
        row = int(row)
        col = int(col)
        if self.inside_board(row, col) == False:
            return None
        else:
            return self.board[row][col]

    def set_piece(self, row, col, piece):
        self.board[row][col] = piece

    def count_pieces(self, piece):
        count = 0
        for row in self.board:
            for col in row:
                if col == piece:
                    count += 1
        return count
    
    def inside_board(self, row, col):
        row = int(row)
        col = int(col)
        if row >= 0 and row < len(self.board):
            if col >= 0 and col < len(self.board[row]):
                return True
        return False
    
    def get_empty_spaces(self):
        empty_spaces = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == '.':
                    empty_spaces.append((row, col))
        return empty_spaces

    def get_pieces(self, piece):
        pieces = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == piece:
                    pieces.append((row, col))
        return pieces

    # def get_adjacent_spaces(self, row, col):
    #     row = int(row)
    #     col = int(col)
    #     adjacent_spaces = []
    #     if row - 1 >= 0:
    #         adjacent_spaces.append((row - 1, col))
    #     if row + 1 < len(self.board):
    #         adjacent_spaces.append((row + 1, col))
    #     if col - 1 >= 0:
    #         adjacent_spaces.append((row, col - 1))
    #     if col + 1 < len(self.board[row]):
    #         adjacent_spaces.append((row, col + 1))
    #     return adjacent_spaces
    
    def get_adjacent_spaces(self, row, col):
        row = int(row)
        col = int(col)
        #ajacent_spaces = []
        #Can you turn all tuples into lists? For the whole function
        if([row, col] == [0, 0]):           #[7, a]
            return [[0, 1], [3, 0]]
        if([row, col] == [0, 1]):           #[7, d]
            return [[0, 0], [0, 2], [1, 1]]
        if([row, col] == [0, 2]):           #[7, g]
            return [[0, 1], [3, 5]]
        if([row, col] == [1, 0]):           #[6, b]
            return [[1, 1], [3, 1]]
        if([row, col] == [1, 1]):           #[6, d]
            return [[1, 0], [1, 2], [2, 1], [0, 1]]
        if([row, col] == [1, 2]):           #[6, f]
            return [[1, 1], [3, 4]]
        if([row, col] == [2, 0]):           #[5, c]
            return [[2, 1], [3, 2]]
        if([row, col] == [2, 1]):           #[5, d]
            return [[2, 0], [2, 2], [1, 1]]
        if([row, col] == [2, 2]):           #[5, e]
            return [[2, 1], [3, 3]]         
        if([row, col] == [3, 0]):           #[4, a]
            return [[0, 0], [3, 1], [6, 0]]
        if([row, col] == [3, 1]):           #[4, b]
            return [[3, 0], [3, 2], [1, 0], [5, 0]]
        if([row, col] == [3, 2]):           #[4, c]
            return [[3, 1], [2, 0], [4, 0]]
        if([row, col] == [3, 3]):           #[4, e]
            return [[2, 2], [4, 2], [3, 4]]
        if([row, col] == [3, 4]):           #[4, f]
            return [[3, 3], [1, 2], [5, 2], [3, 5]]
        if([row, col] == [3, 5]):           #[4, g]
            return [[0, 2], [3, 4], [6, 2]]
        if([row, col] == [4, 0]):           #[3, c]
            return [[4, 1], [3, 2]]
        if([row, col] == [4, 1]):           #[3, d]
            return [[4, 0], [4, 2], [5, 1]]
        if([row, col] == [4, 2]):           #[3, e]
            return [[4, 1], [3, 3]]
        if([row, col] == [5, 0]):           #[2, b]
            return [[5, 1], [3, 1]]
        if([row, col] == [5, 1]):           #[2, d]
            return [[5, 0], [5, 2], [4, 1], [6, 1]]
        if([row, col] == [5, 2]):           #[2, f]
            return [[5, 1], [3, 4]]
        if( [row, col] == [6, 0]):          #[1, a]
            return [[3, 0], [6, 1]]
        if([row, col] == [6, 1]):           #[1, d]
            return [[6, 0], [6, 2], [5, 1]]
        if([row, col] == [6, 2]):           #[1, g]
            return [[6, 1], [3, 5]]
        

    def get_adjacent_pieces(self, row, col, piece):
        row = int(row)
        col = int(col)
        adjacent_spaces = self.get_adjacent_spaces(row, col)
        adjacent_pieces = []
        for space in adjacent_spaces:
            if self.board[space[0]][space[1]] == piece:
                adjacent_pieces.append(space)
        return adjacent_pieces

    def get_adjacent_empty_spaces(self, row, col):
        row = int(row)
        col = int(col)
        adjacent_spaces = self.get_adjacent_spaces(row, col)
        #print ("adjacent spaces: ", adjacent_spaces)
        
        adjacent_empty_spaces = []
        for space in adjacent_spaces:
            if self.board[space[0]][space[1]] == '.':
                adjacent_empty_spaces.append(space)
        return adjacent_empty_spaces

    def find_mill(self, row, col, turn): 
        #Three pieces of the same type in a line
        # Horizontal
        piece = turn
        row = int(row)
        col = int(col)
        
        if self.board[row][0] == piece and self.board[row][1] == piece and self.board[row][2] == piece:
            if [row,col] == [row,0] or [row,col] == [row,1] or [row,col] == [row,2]:
                return True
        if row == 3 and self.board[row][3] == piece and self.board[row][4] == piece and self.board[row][5] == piece:
            if [row,col] == [row,3] or [row,col] == [row,4] or [row,col] == [row,5]:
                return True

        # Potential vertical mill coordinates
        pot_mills = [[[0,0],[3,0],[6,0]],[[0,2],[3,5],[6,2]],[[1,0],[3,1],[5,0]],[[1,2],[3,4],[5,2]],[[0,1],[1,1],[2,1]],[[4,1],[5,1],[6,1]],[[2,0],[3,2],[4,0]],[[2,2],[3,3],[4,2]]]
        for mill in pot_mills:
            if self.board[mill[0][0]][mill[0][1]] == piece and self.board[mill[1][0]][mill[1][1]] == piece and self.board[mill[2][0]][mill[2][1]] == piece:
                if [row,col] == [mill[0][0],mill[0][1]] or [row,col] == [mill[1][0],mill[1][1]] or [row,col] == [mill[2][0],mill[2][1]]:
                    return True
                