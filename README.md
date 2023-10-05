# Knight's Tour Game
This is a simple implementation of the Knight’s Tour game in Python. 
The goal of the game is to move a knight around an empty chessboard and visit each square exactly once.


## ChessBoard Class
The ChessBoard class represents the chessboard on which the game is played.
It has four methods:

### __init__(): Initializes an empty chessboard with user-defined size.
### ValidMoves(CurrPosition): Returns all valid moves based on the current position on the board.
### FillObstacles(): Fills cells on the board with obstacles based on user input.
### PrintBoard(): Prints the current state of the board.



## TourSolver Class
The TourSolver class solves the Knight’s Tour problem using backtracking. 
It has three methods:

### __init__(): Initializes an empty list to store all tour solutions.
### Solver(ChessBoard,CurrPosition,counter): Recursively finds all valid moves for a given position on the board and appends a deep copy of the board to the list of solutions if it is solved.
### FindSolutions(ChessBoard,Start): Sets the starting position to 1 and calls Solver() with starting position and counter set to 2.
### PrintSolutions(): Prints each solution in the list of solutions.
