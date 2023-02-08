class EndGame:
    def init(self, board):
        self.board = board

    def check_win(self):
        # Check if a player has only 2 pieces left
        white_count = self.board.count_pieces("W")
        black_count = self.board.count_pieces("B")
        if white_count <= 2:
            return "Black wins"
        if black_count <= 2:
            return "White wins"

        # Check if a player cannot move
        white_moves = self.get_moves("W")
        black_moves = self.get_moves("B")
        if not white_moves:
            return "Black wins"
        if not black_moves:
            return "White wins"

        return "Game is still ongoing"

    def get_moves(self, piece):
        pieces = self.board.get_pieces(piece)
        moves = []
        for row, col in pieces:
            empty_spaces = self.board.get_adjacent_empty_spaces(row, col)
            moves.extend(empty_spaces)
        return moves
