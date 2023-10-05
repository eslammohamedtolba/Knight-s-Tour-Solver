'''
Knight’s Tour is a puzzle game where the player must move a knight on a chessboard so that it visits every square exactly once
'''
from ChessBoard import *
from SolverKnightTour import *

# Creating a new chess board and Printing the initial state of it and then Filling obstacles on the board based on user input
chess = ChessBoard()
chess.PrintBoard()
chess.FillObstacles()
chess.PrintBoard()


# Creating a new solver object
tourSolver = TourSolver()
# Setting the starting position for the knight's tour
Start=[1,1]
# Finding all possible solutions for the knight's tour and printing them
tourSolver.FindSolutions(chess,Start)
tourSolver.PrintSolutions()