class Letter:
    def __init__(self, char, score):
        self.char = char
        self.score = score
        """
        Initializes the letter
        
        @param letterId: letter id
        @param char: letter character
        @param score: letter score
        @return: none
        
        """
        
    def _setId(self, letterId):
        self.letterId = letterId 
        """
        
        Sets id to a letter object
        
        @param LetterId: id to be assigned to a letter object
        @return: void
        """
    
    def _setChar(self, char):
        self.char = char
        """
        
        Sets char to a letter object
        
        @param char: char to be assigned to a letter object
        @return: void
        """
    
    def _setScore(self, score):
        self.score = score
        """
        
        Sets score to a letter object
        
        @param score: int score to be assigned to a letter object
        @return: void
        """ 
    
    def getId(self):
        """
        Gets the letters id
        
        @param: None
        @return: letters id
        
        """
        return self.letterId

    def getChar(self):
        """
        Gets the letters Char
        
        @param: None
        @return: letters char
        
        """
        return self.char

    def getScore(self):
        """
        Gets the letters score
        
        @param: None
        @return: letter score
        
        """
        return self.score

