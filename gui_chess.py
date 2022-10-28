import random
import sys
import chess
import chess.svg
from PyQt5 import QtSvg
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame
from MinimaxAI import MinimaxAI


class ChessGui:
    def __init__(self, player1, player2):
        self.timer = None
        self.player1 = player1
        self.player2 = player2
        self.game = ChessGame(player1, player2)
        self.app = QApplication(sys.argv)
        self.svgWidget = QtSvg.QSvgWidget()
        self.svgWidget.setGeometry(50, 50, 400, 400)
        self.svgWidget.show()

    def start(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.make_move)
        self.timer.start(10)
        self.display_board()

    def display_board(self):
        svgboard = chess.svg.board(self.game.board)
        svgbytes = QByteArray()
        svgbytes.append(svgboard)
        self.svgWidget.load(svgbytes)

    def make_move(self):
        print("making move, white turn " + str(self.game.board.turn))
        self.game.make_move()
        self.display_board()


if __name__ == "__main__":
    random.seed(1)

    # player_ronda = RandomAI()

    # to do: gui does not work well with HumanPlayer, due to input() use on stdin conflict
    #   with event loop.

    player1 = AlphaBetaAI(4)
    player2 = MinimaxAI(4)

    game = ChessGame(player1, player2)
    gui = ChessGui(player1, player2)

    gui.start()

    sys.exit(gui.app.exec_())
