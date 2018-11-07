class Player:
    def __init__(self, id, score, isTurn):
        """
        Initializes the Player

        @param id: player id
        @param score: player score
        @param isTurn: player turn state
        @return: none
        """
        pass

    def placeLetter(self, letter):
        """
        Places letter on the board

        @param letter: the letter to place
        @return: none
        """
        pass


    def updateScore(self, score):
        """
        Updates the players score.

        @param: none
        @return: users new score
        """
        pass


    def passTurn(self):
        """
        Passes turn to next player

        @param: none
        @return: void
        """
        pass


    def swapLetters(self, letters):
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
        pass


    def getScore(self):
        """
        Gets the player score

        @param: none
        @return: player score
        """
        pass


    def getIsTurn(self):
        """
        Gets the isTurn variable

        @param: none
        @return: player turn state
        """
        pass


    def _setId(self, playerId):
        """
        Sets the player id.

        @param playerId: the id to be assigned to the player instance
        @return: void
        """
        pass


    def _setScore(self, score):
        """
        Sets the player score.

        @param score: the players score
        @return: void
        """
        pass


    def _setIsTurn(self, isTurn):
        """
        Sets if is players turn.

        @param isTurn: state of player turn
        @return: void
        """
        pass