from src.classes.bag import Bag
from src.classes.letter import Letter

class Rack:
    def __init__(self, letters):
        """
        Initialises Rack object

        @params letters: array of letters currently in the Racl
        @return: void
        """
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

    def toArray(self):
        lst = []
        for letter in self.letters:
            print(letter)
            if letter != False:
                lst.append(letter.char)
        return lst

    def add(self, letter):
        """
        Adds a new letter from the bag to the rack

        @param letter: new letter that is added to the rack
        @return: void
        """
        self.letters.append(letter)

    def removeLetter(self, char):
        """
        Removes letter(s) from the rack 

        @param char: Letter to be removed from the rack
        @return: void
        """  
        for i, letter in enumerate(self.letters):
            if letter.char == char:
                break
        self.letters.pop(i)
            

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
        
    def swap(self, letters, bag):
        """
        Swaps Letters from the Rack for Letters in the Bag

        @param letters: Letter(s) to be removed from the rack
        @param bagId: Id of bag to take letters from
        @return: void
        """
        # This section is probably wrong
        new_rack = []
        for x in range(len(letters)):
            if not bag.isEmpty():
                new_rack.append(bag._remove())
        self.letters = new_rack
