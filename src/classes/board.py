from square import Square
from word import Word

class Board:
    def __init__(self):
        self.board = [[ "" for i in range (0,15) ] for j in range (0,15)]



    def isValid(self, coord):
        """
        Checks coord is valid coordinates (within range (0-14)), checks coord is empty.
        @param coord (x,y)
        @return: Boolean
        """
        x,y = coord
        if 0<=x and 15> x and 0<=y and 15>y:
            if self.board[y][x] == "":
                return True
        return False
    def update(self, x1,y1,x2,y2): # Need to append string to board
        """
        Update the board after a valid move is played.
        @param x (int): Represents boards x axis (0 <= x <= 15).
        @param y (int): Represents boards y axis (0 <= x <= 15).
        @return: Void
        """
        if self.isValid(x1, y1, x2, y2):
            
            return self.board

    def _set(self, x1, y1, x2, y2):
        """
        Updates board at end of players turn.

        @param self (Board): Overwrites board with updated board.
        @return: Void
        """
        self.board = update(x1, y1, x2, y2)


    def get(self):
	"""
        Get board.
        @param self (Board):.
        @return: Board
        """
        return self.board
