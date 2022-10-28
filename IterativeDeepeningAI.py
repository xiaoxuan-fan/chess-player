# Author: Xiaoxuan
# Date: 10/27/2022
# Purpose: Iterative Deepening
from AlphaBetaAI import AlphaBetaAI
from math import inf
import chess


class IterativeDeepeningAI:
    def __init__(self, depth_limit):
        self.depth_limit = depth_limit
        self.ai = AlphaBetaAI(depth_limit)

    def choose_move(self, chess_board):
        best_move = None
        best_value = -inf
        for curr_depth in range(self.depth_limit):
            value, move = self.ai.alphabeta(chess_board, curr_depth, chess_board.turn)
            if value > best_value:
                best_value = value
                best_move = move
        print("IterativeDeepening AI recommending move " + str(best_move))
        return best_move


if __name__ == '__main__':
    board = chess.Board()
    print(board)
    ai = IterativeDeepeningAI(3)
    ai.choose_move(board)
