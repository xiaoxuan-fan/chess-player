import chess
import random
from time import sleep


class RandomAI:
    def __init__(self):
        pass

    def choose_move(self, board):
        moves = list(board.legal_moves)
        move = random.choice(moves)
        sleep(1)   # I'm thinking so hard.
        print("Random AI recommending move " + str(move))
        return move


if __name__ == '__main__':
    board = chess.Board()
    print(board)
    ai = RandomAI()
    ai.choose_move(board)
