# Author: Xiaoxuan
# Date: 10/20/2022
# Purpose: Minimax AI playing chess
import chess
from math import inf


class MinimaxAI:
    def __init__(self, depth_limit):
        self.depth_limit = depth_limit
        self.pieces_value = {chess.PAWN: 1, chess.KNIGHT: 4, chess.BISHOP: 5, chess.ROOK: 6, chess.QUEEN: 10,
                             chess.KING: 500}
        self.call_count = 0

    def minimax(self, chess_board, curr_depth, is_white):
        self.call_count += 1
        moves = chess_board.legal_moves
        best_move = None

        if self.cutoff_test(chess_board, curr_depth):
            return self.eval_func(chess_board), best_move

        if is_white:
            # maximize
            best_value = -inf
            for move in moves:
                chess_board.push(move)
                v = self.minimax(chess_board, curr_depth+1, not is_white)[0]
                if v > best_value:
                    best_value = v
                    best_move = move
                chess_board.pop()
        else:
            # minimize
            best_value = inf
            for move in moves:
                chess_board.push(move)
                v = self.minimax(chess_board, curr_depth+1, not is_white)[0]
                if v < best_value:
                    best_value = v
                    best_move = move
                chess_board.pop()

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
        value, move = self.minimax(chess_board, 0, chess_board.turn)
        if move is None:
            move = list(chess_board.legal_moves)[0]
        print("Minimax AI recommending move " + str(move))
        print(str(self.call_count) + 'calls to minimax')
        return move


if __name__ == "__main__":
    board = chess.Board()
    print(board)
    ai = MinimaxAI(3)
    ai.choose_move(board)
