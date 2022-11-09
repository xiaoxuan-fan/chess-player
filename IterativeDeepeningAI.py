# Author: Xiaoxuan
# Date: 10/27/2022
# Purpose: Iterative Deepening
from AlphaBetaAI import AlphaBetaAI
import chess
import time
# changed branch

class IterativeDeepeningAI:
    def __init__(self, depth_limit, search_method, provided_time):
        self.depth_limit = depth_limit
        self.search_method = search_method
        self.provided_time = provided_time

    def choose_move(self, chess_board):
        start_time = time.time()
        move = None

        for curr_depth in range(self.depth_limit):
            ai = self.search_method(curr_depth)
            move = ai.choose_move(chess_board)
            current_time = time.time()
            spent_time = current_time - start_time
            if (self.provided_time - spent_time) < spent_time:
                break

        print("IterativeDeepening AI recommending move " + str(move))
        return move


if __name__ == '__main__':
    board = chess.Board()
    print(board)
    ai = IterativeDeepeningAI(3, AlphaBetaAI, 3000)
    ai.choose_move(board)
