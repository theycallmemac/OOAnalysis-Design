class Square:
    def __init__(self, x, y, letter, score, isMiddle):
        self.x = x
        self.y = y
        self.letter = letter
        self.score = score
        self.isMiddle = isMiddle

    def getX(self):
        """
        Gets x co-ordinate of square
        @param: void
        @return: int
        """
        return self.x

    def _setX(x):
        """
        Sets x co-ordinate of square
        @param x: x co-ordinate to be set
        @return: void
        """
        self.x = x 

    def getY():
        """
        Gets y co-ordinate of square
        
        @param: void
        @return: int
        """
        return self.y 

    def _setY(y):
        """
        Sets y co-ordinate of square
        
        @param y: y co-ordinate to be set
        @return: void
        """
        self.y = y

    def getLetter(self):
        """
        Gets letter value (if any) of a square
        
        @param: void
        @return: Letter
        """
        return self.letter

    def _setLetter(self, letter):
        """
        Sets letter value of a square
        
        @param letter: letter value to be set on current square
        @return: void
        """
        self.letter = letter

    def getScore(self):
        """
        Gets score value (if any) of a square
        
        @param: void
        @return: int
        """
        return self.score

    def _setScore(self, score):
        """
        Sets score value of a square
        
        @param score: score value to be set on current square
        @return: void
        """
        self.score = score

    def getMiddle(self):
        """
        Checks to see if square is in the centre of the board
        
        @param: void
        @return: bool
        """
        return self.isMiddle

    def _setMiddle(self, square):
        """
        Sets the centre of the board
        
        @param sqaure: sqaure to be set as centre
        @return: void
        """
        self.isMiddle = square.isMiddle # potentially incorrect 
