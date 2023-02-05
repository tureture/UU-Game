import random
def mock_player():
    row = 3
    column = random.randint(0, 5)
    index = random.randint(0, 2)
    type_move = ['place','move','remove'][index]
    return [row, column, type_move]

