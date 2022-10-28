# Author: Xiaoxuan
# Date: 10/26/2022
# Purpose: Minimax AI with Alpha-Beta Pruning playing chess
import chess
from math import inf
import random


class AlphaBetaAI:
    def __init__(self, depth_limit, memoize=False):
        self.depth_limit = depth_limit
        self.pieces_value = {chess.PAWN: 1, chess.KNIGHT: 4, chess.BISHOP: 5, chess.ROOK: 6, chess.QUEEN: 10,
                             chess.KING: 500}
        self.call_count = 0
        self.memoize = memoize
        self.transposition_table = {}

    def alphabeta(self, chess_board, curr_depth, is_white, alpha=-inf, beta=inf):
        self.call_count += 1
        moves = list(chess_board.legal_moves)
        best_move = None

        if self.cutoff_test(chess_board, curr_depth):
            return self.eval_func(chess_board), best_move

        # shuffle the legal moves to avoid infinite loop
        random.shuffle(moves)

        # if the board position was seen before
        if self.memoize:
            if str(chess_board) in self.transposition_table:
                return self.transposition_table[str(chess_board)]

        if is_white:
            # maximize
            best_value = -inf
            for move in moves:
                chess_board.push(move)
                v = self.alphabeta(chess_board, curr_depth+1, not is_white, alpha, beta)[0]
                if v > best_value:
                    best_value = v
                    alpha = v
                    best_move = move
                chess_board.pop()
                if beta < alpha:
                    break
        else:
            # minimize
            best_value = inf
            for move in moves:
                chess_board.push(move)
                v = self.alphabeta(chess_board, curr_depth+1, not is_white, alpha, beta)[0]
                if v < best_value:
                    best_value = v
                    beta = v
                    best_move = move
                chess_board.pop()
                if beta < alpha:
                    break

        if self.memoize:
            self.transposition_table[str(chess_board)] = (best_value, best_move)

        return best_value, best_move


    # cut off the search if depth limit is reached or if the game is over
    def cutoff_test(self, chess_board, curr_depth):
        if chess_board.is_game_over() or curr_depth >= self.depth_limit:
            return True
        return False

    # heuristic to calculate the desirability of each state:
    # value of pieces * number of pieces
    def eval_func(self, chess_board):
        value = 0
        # if it is checkmate, value is infinity
        if chess_board.is_checkmate():
            if chess_board.outcome().winner:
                value = inf
            else:
                value = -inf
        else:
            for piece_type, piece_value in self.pieces_value.items():
                value += len(chess_board.pieces(piece_type, chess.WHITE)) * piece_value
                value -= len(chess_board.pieces(piece_type, chess.BLACK)) * piece_value
        return value

    def choose_move(self, chess_board):
        self.call_count = 0
        self.transposition_table = {}
        value, move = self.alphabeta(chess_board, 0, chess_board.turn)
        if move is None:
            move = list(chess_board.legal_moves)[0]
        print("AlphaBeta AI recommending move " + str(move))
        print(str(self.call_count) + 'calls to alphabeta')
        return move


if __name__ == "__main__":
    board = chess.Board()
    print(board)
    ai = AlphaBetaAI(3, True)
    ai.choose_move(board)
