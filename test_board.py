# Import the Board class from the board_rep.py file
from board_rep import Board
from mock_player import*
board_test = Board()
place = mock_player()
move = mock_player()
board_test.set_piece(move[0], move[1], 'X')
board_test.set_piece(0, 1, 'X')
board_test.set_piece(0, 2, 'X')
print(board_test)
print(board_test.find_mill(0, 0, 'X'))