import os
class Word:
    DICTIONARY = set()
    def __init__(self, word):
        """
        Initialises Word object

        @param id:  id of the word 
        @param letters: array of letters
        @param score: score int
        @return: void
        """
        self.word = word
        
        if Word.DICTIONARY != "":
            fileDir = os.path.dirname(os.path.realpath('__file__'))
            filename = os.path.join(fileDir, './british-english.txt')
            f = open(filename, 'r')
            Word.DICTIONARY = set()
            x = f.readlines()
            for l in x:
                Word.DICTIONARY.add(l.strip())
            f.close()
        
    def _setScore(self, score):
        """
        @param score : int score to be assigned to word object
        @return: void
        """
        pass

    def getScore(self):
        """
        @params: none
        @return: score int
        """
        pass
    
    def calcScore(self):
        """
        @params: none
        @return: word score int
        """
        pass

    def _setLetters(self, letters):
        """
        @param letters: array of letters
        @return: void
        """
        pass
    
    def getLetters(self):
        """
        @params: none
        @return: array of letters
        """
        pass
    
    def _setScore(self, score):
        """
        @param score: int score to be assigned to word
        @return: void
        """
        pass
    
    def getScore(self):
        """
        @params: none
        @return: score int
        """
        pass

    def isValid(self):
        """
        @param dictionary: dictionary of words which will be used to check if the word is valid
        """
        if self.word in Word.DICTIONARY:
            return True
        return False
           
