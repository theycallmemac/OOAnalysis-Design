class Rack:
    def __init__(self, id, letters):
        """
        Initialises Rack object

        @param id: id of Rack in the game
        @params letters: array of letters currently in the Racl
        @return: void
        """
        self.id = id
        self.letters = letters
    
    def getId(self):
        """
        Returns Id of Rack 

        @param: void
        @return: int
        """    
        return self.id

    def getLetters(self):
        """
        Returns Letters currently in the Rack

        @param: void
        @return: Letters[]
        """    
        return self.letters

    def _setId(self, id):
        """
        Sets Id of Rack 

        @param id: id of Rack in the game
        @return: void
        """    
        self.id = id

    def _setLetters(self, letters):
        """
        Sets Letters currently in the  Rack 

        @param letters: array of letters in the rack
        @return: void
        """    
        self.letters = letters

    def add(self, letter):
        """
        Adds a new letter from the bag to the rack

        @param letter: new letter that is added to the rack
        @return: void
        """
        self.letters.append(letter)

    def remove(self, letter):
        """
        Removes letter(s) from the rack 

        @param letter: Letter(s) to be removed from the rack
        @return: void
        """    
        self.letters.remove(letter)

    def isFull(self):
        """
        Checks to see if a Rack is currently full 

        @param: void
        @return: bool
        """    
        if len(self.letters) == 7:
            return True
        else:
            return False
        
    def swap(self, letters, bagId):
        """
        Swaps Letters from the Rack for Letters in the Bag

        @param letters: Letter(s) to be removed from the rack
        @param bagId: Id of bag to take letters from
        @return: void
        """
        # This section is probably wrong
        for letter in letters:
            Rack.remove(letter)
        
        new_letters = Bag.getLetters()
        i = 0
        while not Rack.isFull():
            Rack.add(new_letters[i])
