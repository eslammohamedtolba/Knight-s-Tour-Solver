from copy import deepcopy

class TourSolver:
    def __init__(self):
        # Initialize an empty list to store all tour solutions.
        self.TourSolutions = []
    def Solver(self,ChessBoard,CurrPosition,counter):
        # If the board was solved, append a deep copy of the board to the list of solutions
        if ChessBoard.SolvedBoard():
            self.TourSolutions.append(deepcopy(ChessBoard))
            return
        # Get all valid moves for the current position
        # Recursively call Solver() for each valid move
        for Move in ChessBoard.ValidMoves(CurrPosition):
            ChessBoard.Board[Move[0]-1][Move[1]-1]=counter
            self.Solver(ChessBoard,Move,counter+1)
            ChessBoard.Board[Move[0]-1][Move[1]-1]=' '

    def FindSolutions(self,ChessBoard,Start):
        ChessBoard.Board[Start[0]-1][Start[1]-1]=1
        # Call Solver() with starting position and counter set to 2
        self.Solver(ChessBoard,Start,2)

    # Print each solution in the list of solutions
    def PrintSolutions(self):
        for solution in self.TourSolutions:
            solution.PrintBoard()
