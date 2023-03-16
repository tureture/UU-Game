from copy import deepcopy as copy
from mock_rule import mock_rule_check
import random



##Fix game input in ,ill mock rule
#a = minimax_agent('B')


class Minimax_agent:

    def __init__(self, diff=2):
        self.difficulty = diff
        
        if self.difficulty == 1:   
            self.depth = 2
            self.toss = 0.3
        elif self.difficulty == 2:
            self.depth = 4
            self.toss = 0.5
        elif self.difficulty == 3:
            self.depth = 4
            self.toss = 0.9   
        elif self.difficulty == 4:
            self.depth = 6
            self.toss = 1   
        else:
            print("Error with wrong difficulty input")
            print(type(diff)) 

    def flip(self):
        return True if random.random() < self.toss else False
    
    def get_leagal_moves(self,board, unplaced, p, game): #p is the p of the player you want to find leagal moves for
        
        
        
        leagal_moves = [] #U_p = Unplaced piece, R_p = Remove piece
        if unplaced > 0:
            for i in range(0,9):
                for j in range(0,9):
                    if board.get_piece(i,j) == '.':
                        leagal_moves.append(['U_p','U_p',i,j]) #U_p = Unplaced piece
                        
        else:
            for i in range(0,9):
                for j in range(0,9):
                    if board.get_piece(i,j) == p:
                        for k in range(0,9):
                            for l in range(0,9):
                                if mock_rule_check(board,[i,j,k,l],p,'move',game)[0] == 'True':
                                    leagal_moves.append([i,j,k,l]) ## [i,j] is the piece to move, [k,l] is the destination
        return leagal_moves
                                    
                                    
        
    def get_leagal_mills(self,board, p):
        
        leagal_moves = []
        opponent = {'W':'B','B':'W'}
        free_pieces = [] # Pieces that are not in a mill
        pieces_in_mills = [] #Pieces that are in a mill

        for i in range(0,9): #Find all pieces that are not in a mill, for possible mill formation
            for j in range(0,9):
                if board.get_piece(i,j) == opponent[p] and board.find_mill(i, j, opponent[p]):
                    pieces_in_mills.append([i,j])
            
                elif board.get_piece(i,j) == opponent[p] and not board.find_mill(i, j, opponent[p]):
                    free_pieces.append([i,j]) #Pieces that are not in a mill   
                
        if len(free_pieces) > 0:
            for piece in free_pieces:
                leagal_moves.append([piece[0],piece[1]]) #R_p = Remove piece
        else:
            for piece in pieces_in_mills:
                leagal_moves.append([piece[0],piece[1]]) #R_p = Remove piece
        
        
        return leagal_moves


    def minimax(self, game, p, maximizingPlayer, alpha=float('-inf'), beta=float('inf')):
        if self.flip():
            return self._minimax(game, p, self.depth , maximizingPlayer, alpha, beta)
        else:
            moves = self.get_leagal_moves(game.board, game.unplaced[p] ,p, game)
            random_return = random.choice(moves)
            return [0, random_return]
                
        
            
    def _minimax(self, game, p, depth , maximizingPlayer, alpha=float('-inf'), beta=float('inf')): #With alpha beta
        opponent = {'W':'B','B':'W'}
        if depth <= 0 or game.inventory[p] <= 2: #Should only be called when input p is the p of the player to move
            #thus only even depths are possible (I think)
            return [self.evaluation_function(game, p), [0,0]]

        if maximizingPlayer == True:
            maxEval = -10000000 
            for move in self.get_leagal_moves(game.board, game.unplaced[p] ,p, game): ##All possible moves
                game_copy = copy(game) 
                game_copy.unplaced[p] -= 1
                board_copy = game_copy.board
                if move[0] == 'U_p': #If the move is to place a piece
                    board_copy.set_piece(move[2], move[3], p)
                else: #If the move is to move a piece
                    board_copy.set_piece(move[2], move[3], p)
                    board_copy.set_piece(move[0], move[1], '.') #Remove the piece from the old position    
                
                if board_copy.find_mill(move[2], move[3], p): #If a mill is formed
                    
                    eval = self._mill_minimax(game_copy, p, depth, True, alpha, beta)[0]
                      
                else:          
                    eval = self._minimax(game_copy, opponent[p], depth-1, False, alpha, beta)[0]
                if eval > maxEval:
                    best_move = [move[0], move[1], move[2], move[3]]
                    maxEval = eval
 
                alpha = max(alpha, maxEval)
                if beta <= alpha:
                    break
            return [maxEval  ,best_move]

        else:
            
                  
            minEval = 1000000
            for move in self.get_leagal_moves(game.board, game.unplaced[p] ,p, game):
                game_copy = copy(game)
                board_copy = game_copy.board #Copy the board, update the copy, and then pass the copy to the next level of recursion
                if move[0] == 'U_p': #If the move is to place a piece
                    board_copy.set_piece(move[2], move[3], p)
                else: #If the move is to move a piece
                    board_copy.set_piece(move[2], move[3], p)
                    board_copy.set_piece(move[0], move[1], '.') #Remove the piece from the old position   
                 
                if board_copy.find_mill(move[2], move[3], p): #If a mill is formed
                  
                    eval = self._mill_minimax(game_copy, p, depth, False, alpha, beta)[0] 
                else:    
                    eval = self._minimax(game_copy, opponent[p], depth-1, True, alpha, beta)[0]
                if eval < minEval:
                    best_move = [move[0], move[1], move[2], move[3]]
                    minEval = eval
                    
                beta = min(beta, minEval)
                if beta <= alpha:
                    break
            return [minEval, best_move]
        
        
    def mill_minimax(self, game ,p, maximizingPlayer, alpha=float('-inf'), beta=float('inf')): #With alpha beta
        if self.flip():
            return self._mill_minimax(game ,p, self.depth, maximizingPlayer, alpha, beta) #With alpha beta
        else:
            moves = self.get_leagal_mills(game.board,p)
            random_return = random.choice(moves)
            return [0, random_return]        
        
        

    def _mill_minimax(self, game ,p, depth, maximizingPlayer, alpha=float('-inf'), beta=float('inf')): #With alpha beta
        opponent = {'W':'B','B':'W'}
        if maximizingPlayer == True:
            maxEval = -10000000
            
            for move in self.get_leagal_mills(game.board, p):
                game_copy = copy(game)
                game_copy.inventory[opponent[p]] -= 1
                board_copy = game_copy.board
                board_copy.set_piece(move[0], move[1], '.') #Remove the piece from the board
                eval = self._minimax(game_copy, opponent[p], depth-1, False, alpha, beta)[0]
                if eval > maxEval:
                    maxEval = eval
                    best_move = [move[0], move[1]]
                    
                alpha = max(alpha, maxEval)
                if beta <= alpha:
                    break 
            return [maxEval, best_move]
        else:
            minEval = 10000000
            for move in self.get_leagal_mills(game.board, p):
                game_copy = copy(game)
                board_copy = game_copy.board
                game_copy.inventory[opponent[p]] -= 1
                board_copy.set_piece(move[0], move[1], '.')
                eval = self._minimax(game_copy, opponent[p], depth-1, True, alpha, beta)[0]
                if eval < minEval:
                    
                    minEval = eval
                    best_move = [move[0], move[1]]   
                beta = min(beta, minEval)
                if beta <= alpha:
                    break
            return [minEval, best_move]
                
            
        
        
    def evaluation_function(self, game, p):
        #return the evaluation of the board
        #Borad copy should be uppdated with the move to be evaluated
        #If a Mill is formed, the evaluation should be 1000
        #Forming a mill should be prioritized over blocking a mill
        #One should be able to form a mill and remove a piece in the same move
        opponent = {'W':'B','B':'W'}
        my_mills = 0
        op_mills = 0
        board = game.board
        #weights
        a = 2 #Increase to prioritize keeping pieces
        b = 1 #Increase to prioritize removing pieces
        c = 10 #Increase to prioritize forming mills
        d = 5 #Increase to prioritize blocking mills
        ##
        
        for i in range(0,9):
            for j in range(0,9):
                if board.get_piece(i,j) == p:
                    if board.find_mill(i,j,p): 
                        my_mills += 1 #Divide mills by 3 to get the number of mills
                elif board.get_piece(i,j) == opponent[p]:
                    if board.find_mill(i,j,opponent[p]):
                        op_mills += 1 #Divide mills by 3 to get the number of mills   
                        
                             
        my_pieces = game.inventory[p]
        op_pieces = game.inventory[opponent[p]]
        
        return a*my_pieces - b*op_pieces + (c*my_mills)/3 - (d*op_mills)/3 
        


