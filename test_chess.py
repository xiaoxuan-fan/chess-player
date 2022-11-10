# Author: Xiaoxuan
# Date: 10/31/2022
# Purpose: test various chess-playing programs
import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame
import random

random.seed(1)
player1 = MinimaxAI(4)
player2 = AlphaBetaAI(4)

game = ChessGame(player1, player2)
# game.board = chess.Board("3b1k1r/1b5q/3pp1K1/p7/2p2pp1/4n3/4r3/8 w - - 0 104")
game.board = chess.Board("1k2r2r/ppp2Q2/3p3b/2nP3p/2PN4/6PB/PP3R1P/1K6 b - - 0 1")

while not game.is_game_over():
    print(game)
    game.make_move()
print(game.board.outcome())

# print(hash(str(game.board)))
