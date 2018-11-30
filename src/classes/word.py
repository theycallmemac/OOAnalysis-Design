import os
from src.classes.letter import Letter
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
        self.score = self.getScore()
        
        if Word.DICTIONARY != "":
            fileDir = os.path.dirname(os.path.realpath('__file__'))
            filename = os.path.join(fileDir, './british-english.txt')
            f = open(filename, 'r')
            Word.DICTIONARY = set()
            x = f.readlines()
            for l in x:
                Word.DICTIONARY.add(l.strip())
            f.close()
        
        # self.id = id
        # self.letters = letters
        # self.score = score
    
    # def _setId(self, id):
    #     """
    #     @param id : int word id
    #     @return: void
    #     """
    #     self.id = id

    # def getId(self):
    #     """
    #     @param: None
    #     @return: id int
    #     """
    #     return self.id

    # def _setScore(self, score):
    #     """
    #     @param score : int score to be assigned to word object
    #     @return: void
    #     """
    #     self.score = score

    def getScore(self):
        """
        @params: none
        @return: score int
        """
        score = 0
        for letter in self.word:
            print("Letter", letter)
            if letter != "_":
                score += Letter.LETTER_SCORES[letter]
        return score
        
    
    # def calcScore(self):
    #     """
    #     @params: none
    #     @return: word score int
    #     """
    #     score = 0
    #     for letter in self.letters:
    #         score += Word.LETTER_SCORES[letter]
    #     self.score = score

    # def _setLetters(self, letters):
    #     """
    #     @param letters: array of letters
    #     @return: void
    #     """
    #     for letter in letters:
    #         self.letters.append(letter)
    
    # def getLetters(self):
    #     """
    #     @params: none
    #     @return: array of letters
    #     """
    #     return self.letters

    def isValid(self):
        """
        @param dictionary: dictionary of words which will be used to check if the word is valid
        """
        if self.word in Word.DICTIONARY:
            return True
        return False
