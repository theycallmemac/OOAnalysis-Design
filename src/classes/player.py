from src.classes.bag import Bag 
from src.classes.rack import Rack 
from src.classes.board import Board 

class Player:
    def __init__(self, id, isTurn, rack):
        self.id = id
        self.score = 0
        self.isTurn = isTurn
        self.rack = rack
        """
        Initializes the Player

        @param id: player id
        @param score: player score
        @param isTurn: player turn state
        @return: none
        """


    def placeLetter(self, letters, x, y):

        """
        Places letter on the board

        @param letter: the letter to place
        @return: none
        """
        pass


    def updateScore(self, score):
        self.score = self.score + score
        """
        Updates the players score.

        @param: none
        @return: users new score
        """
        return self.score


    def passTurn(self):
        self.isTurn = False
        #need to add interaction with the server 
        """
        Passes turn to next player

        @param: none
        @return: void
        """
        pass


    def swapLetters(self, letters, bag):
        bag.swap(rack, letters, bag)
        
        """
        Swaps letters on the rack for letters in the bag

        @param letters: array of letters the player wants to swap
        @return: array of letters from the bag
        """
        pass


    def getId(self):
        """
        Gets the players id.

        @param: none
        @return: player id
        """
        return self.getId


    def getScore(self):
        """
        Gets the player score

        @param: none
        @return: player score
        """
        return self.score


    def getIsTurn(self):
        """
        Gets the isTurn variable

        @param: none
        @return: player turn state
        """
        return self.isTurn


    def _setId(self, playerId):
        self.id = playerId
        """
        Sets the player id.

        @param playerId: the id to be assigned to the player instance
        @return: void
        """


    def _setScore(self, score):
        """
        Sets the player score.

        @param score: the players score
        @return: void
        """
        self.score = score


    def _setIsTurn(self, isTurn):
        """
        Sets if is players turn.

        @param isTurn: state of player turn
        @return: void
        """
        self.isTurn = isTurn