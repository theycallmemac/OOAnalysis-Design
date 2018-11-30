class Letter:
    LETTER_SCORES = {
        "E": 1,
        "A": 1,
        "I": 1,
        "O": 1,
        "N": 1,
        "R": 1,
        "T": 1,
        "L": 1,
        "S": 1,
        "U": 1,
        "D": 2,
        "G": 2,
        "B": 3,
        "C": 3,
        "M": 3,
        "P": 3,
        "F": 4,
        "H": 4,
        "V": 4,
        "W": 4,
        "Y": 4,
        "K": 5,
        "J": 8,
        "X": 8,
        "Q": 10,
        "Z": 10,
    }

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
