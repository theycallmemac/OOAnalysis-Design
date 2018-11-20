from square import Square

class Board:
    def __init__(self):
        self.board = [[Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square],
                      [Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square],
                      [Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square],             # matrix of Squares
                      [Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square],
                      [Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square],
                      [Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square],
                      [Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square],
                      [Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square],
                      [Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square],
                      [Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square],
                      [Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square],
                      [Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square],
                      [Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square],
                      [Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square],
                      [Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square,Square]
                      ]



    def isValid(self, x1,y1, x2,y2):
        """
        Checks x, y is valid coordinate.
        @param x (int): Represents boards x axis (0 <= x <= 15).
        @param y (int): Represents boards y axis (0 <= x <= 15).
        @return: Boolean
        """
        s = []
        if self.onBoard(x1,y1):
            return False
        elif self.onBoard(x2,y2):
            return False
        if self.goVert(x1, x2):
            #Interate down along the the Y since x is the same
            #Start from the (x1,y1) down to (x2,y2)
            for i,val in enumerate(self.board):
                if i > x1 and val.getLetter() != "":
                    #Build an array from the contents
                    s.append(val.getLetter())
                
            #Compare contents to dic.txt
            l2str = ''.join(s):
            if l2str in dictionary.txt:
                return True
            else:
                return False
            #ifTrue
            return True
        
        elif self.goHori(y1, y2):
            #Interate down along the the Y since x is the same
            #Start from the (x1,y1) down to (x2,y2)
            for i in self.board:
                for i,val in enumerate(self.board):
                    if i > y1 and val.getLetter() != "":
                        #Build an array from the contents
                        s.append(val.getLetter())
            #Build an array from the contents
            #Compare contents to dic.txt
            l2str = ''.join(s):
            if l2str in dictionary.txt:
                return True
            else:
                return False
            #ifTrue
            return True
        return True

    def goVert(self, x1, x2):
        if x1 == x2:
            return True
        return False
    
    def goHori(self, y1, y2):
        if y1 == y2:
            return True
        return False

    def onBoard(self, x, y):
        if 15 < x or x < 0 or 15 < y or y < 0:
            return False
        return True

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
