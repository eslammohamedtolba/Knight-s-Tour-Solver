class ChessBoard:
    def __init__(self):
        # Ask user for board size
        while True:
            self.Boardsize = int(input("Enter board size: "))
            if self.Boardsize>0:
                break
        # Create an empty board
        self.Board = [[' ']*self.Boardsize for _ in range(self.Boardsize)]
    
    # List all valid moves for a given position on the board for the knight 
    def ValidMoves(self,CurrPosition):
        moves = []
        for distancex, distancey in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
            NewPosition = [CurrPosition[0] + distancex, CurrPosition[1] + distancey]
            if (0<NewPosition[0] and NewPosition[0]<=self.Boardsize) and (0<NewPosition[1] and NewPosition[1]<=self.Boardsize):
                if self.Board[NewPosition[0]-1][NewPosition[1]-1]==' ':
                    moves.append([NewPosition[0], NewPosition[1]])
        return moves

    def FillObstacles(self):
        # Ask user for number of cells to fill by obstacles
        while True:
            Numfilled = int(input("Enter Number of cells to fill by obstacles: "))
            if Numfilled>=0:
                break
        # Fill cells on the board with obstacles based on user input
        for numObstacle in range(Numfilled):
            while True:
                X = int(input(f"Enter X-axis of obstacles number {numObstacle+1}: "))
                Y = int(input(f"Enter Y-axis of obstacles number {numObstacle+1}: "))
                if (X in range(1,self.Boardsize+1)) and (Y in range(1,self.Boardsize+1)) and self.Board[X-1][Y-1]!='#':
                    self.Board[X-1][Y-1]='#'
                    # Print the current state of the board after filling each obstacle
                    self.PrintBoard()
                    break

    # Print the current state of the board
    def PrintBoard(self):
        print()
        print("--------"*self.Boardsize+"-"*(1+self.Boardsize))
        for i in range(self.Boardsize):
            print("| ",end="")
            for j in range(self.Boardsize):
                print(f"   {self.Board[i][j]}  " if self.Board[i][j]!=' ' else f"{i+1,j+1}",end = ' | ')
            print()
            print("--------"*self.Boardsize+"-"*(1+self.Boardsize))
        print()
    
    # Check if the Board totally filled then the Board solved 
    # by iterating over each row of the Board and check if it totally filled and doesn't contain any empty cell
    def SolvedBoard(self):
        for row in self.Board:
            if row.count(' ')>0:
                return False
        return True
