# Import the Board class from the board_rep.py file
from board_rep import Board
board_test = Board()
board_test.set_piece(0, 0, 'X')
board_test.set_piece(0, 1, 'X')
board_test.set_piece(0, 2, 'X')
print(board_test)
print(board_test.find_mill(0, 0, 'X'))