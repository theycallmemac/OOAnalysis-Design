class Word:

    def __init__(self, id, letters, score):
        """
        Initialises Word object

        @param id:  id of the word 
        @param letters: array of letters
        @param score: score int
        @return: void
        """
        self.id = id
        self.letters = letters
        self.score = score
    
    def _setId(self, id):
        """
        @param id : int word id
        @return: void
        """
        self.id = id

    def getId(self):
        """
        @param: None
        @return: id int
        """
        return self.id

    def _setScore(self, score):
        """
        @param score : int score to be assigned to word object
        @return: void
        """
        self.score = score

    def getScore(self):
        """
        @params: none
        @return: score int
        """
        return self.score
    
    def calcScore(self):
        """
        @params: none
        @return: word score int
        """
        score = 0
        for letter in self.letters:
            score += Word.LETTER_SCORES[letter]
        self.score = score

    def _setLetters(self, letters):
        """
        @param letters: array of letters
        @return: void
        """
        for letter in letters:
            self.letters.append(letter)
    
    def getLetters(self):
        """
        @params: none
        @return: array of letters
        """
        return self.letters

    def isValid(self, dictionary):
        """
        @param dictionary: dictionary of words which will be used to check if the word is valid
        """
        word = "".join(self.letters)
        if word in dictionary:
            return True
        return False