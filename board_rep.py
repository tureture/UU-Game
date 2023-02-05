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
        return  str(self.board[0]) + '\n' + str(self.board[1]) + '\n' + str(self.board[2]) + '\n' + str(self.board[3]) + '\n' + str(self.board[4]) + '\n' + str(self.board[5]) + '\n' + str(self.board[6])

    def get_board(self):
        return self.board

    def set_board(self, board):
        self.board = board

    def get_piece(self, row, col):
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

    def get_adjacent_spaces(self, row, col):
        adjacent_spaces = []
        if row - 1 >= 0:
            adjacent_spaces.append((row - 1, col))
        if row + 1 < len(self.board):
            adjacent_spaces.append((row + 1, col))
        if col - 1 >= 0:
            adjacent_spaces.append((row, col - 1))
        if col + 1 < len(self.board[row]):
            adjacent_spaces.append((row, col + 1))
        return adjacent_spaces

    def get_adjacent_pieces(self, row, col, piece):

        adjacent_spaces = self.get_adjacent_spaces(row, col)
        adjacent_pieces = []
        for space in adjacent_spaces:
            if self.board[space[0]][space[1]] == piece:
                adjacent_pieces.append(space)
        return adjacent_pieces

    def get_adjacent_empty_spaces(self, row, col):
        adjacent_spaces = self.get_adjacent_spaces(row, col)
        adjacent_empty_spaces = []
        for space in adjacent_spaces:
            if self.board[space[0]][space[1]] == '.':
                adjacent_empty_spaces.append(space)
        return adjacent_empty_spaces

    def find_mill(self, row, col, piece):
        # Three pieces of the same type in a line
        # Horizontal
        if row == 0 or row == 3 or row == 6:
            if self.board[row][0] == piece and self.board[row][1] == piece and self.board[row][2] == piece:
                return True
        # Vertical
        if col == 0 or col == 3 or col == 6:
            if self.board[0][col] == piece and self.board[1][col] == piece and self.board[2][col] == piece:
                return True
        return False

    