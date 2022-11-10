# Author: Xiaoxuan
# Date: 10/27/2022
# Purpose: Iterative Deepening under time limit
from AlphaBetaAI import AlphaBetaAI
import chess
import time


class IterativeDeepeningAI:
    def __init__(self, search_method, time_limit):
        self.search_method = search_method
        self.time_limit = time_limit

    def choose_move(self, chess_board):
        start_time = time.time()
        move = None

        for curr_depth in range(1000):
            search_method = self.search_method(curr_depth)
            move = search_method.choose_move(chess_board)
            current_time = time.time()
            spent_time = current_time - start_time
            if (self.time_limit - spent_time) < spent_time:
                print(curr_depth)
                break

        print("IterativeDeepening AI recommending move " + str(move))
        return move


if __name__ == '__main__':
    board = chess.Board()
    print(board)
    ai = IterativeDeepeningAI(AlphaBetaAI, 30)
    ai.choose_move(board)
