from random import shuffle
from string import ascii_uppercase
from src.classes.letter import Letter
import random

class Bag:
    LETTERS = list(ascii_uppercase)					# for random search
    def __init__(self):
        self.length = 100
        self.letters = {							# "l" : (ammount, points)
                        " " : (2, 0),
                        "E" : (12, 1),
                        "A" : (9, 1),
                        "I" : (9, 1),
                        "O" : (8, 1),
                        "N" : (6, 1),
                        "R" : (6, 1),
                        "T" : (6, 1),
                        "L" : (4, 1),
                        "S" : (4, 1),
                        "U" : (4, 1),
                        "D" : (4, 2),
                        "G" : (3, 2),
                        "B" : (2, 3),
                        "C" : (2, 3),
                        "M" : (2, 3),
                        "P" : (2, 3),
                        "F" : (2, 4),
                        "H" : (2, 4),
                        "V" : (2, 4),
                        "W" : (2, 4),
                        "Y" : (2, 4),
                        "K" : (1, 5),
                        "J" : (1, 8),
                        "X" : (1, 8),
                        "Q" : (1, 10),
                        "Z" : (1, 10),
                        }

    def get(self):
        """ Get bag.
        @param self(Bag):.
        @return: Bag
        """
        return self.letters                         # return dictionary

    def _set(self):
        """ Updates bag.
            @param self(Bag):.
            @return: Void
        """
        self.letters = {                            # initial value
        " " : [2, 0],
        "E" : [12, 1],
        "A" : [9, 1],
        "I" : [9, 1],
        "O" : [8, 1],
        "N" : [6, 1],
        "R" : [6, 1],
        "T" : [6, 1],
        "L" : [4, 1],
        "S" : [4, 1],
        "U" : [4, 1],
        "D" : [4, 2],
        "G" : [3, 2],
        "B" : [2, 3],
        "C" : [2, 3],
        "M" : [2, 3],
        "P" : [2, 3],
        "F" : [2, 4],
        "H" : [2, 4],
        "V" : [2, 4],
        "W" : [2, 4],
        "Y" : [2, 4],
        "K" : [1, 5],
        "J" : [1, 8],
        "X" : [1, 8],
        "Q" : [1, 10],
        "Z" : [1, 10],
        }


    def _add(self, letters):							# input array of Letter obj
        """ Inherit letters from rack and add them to bag.
            @param letters (list): Length of list must be between 1 and 7.
            @return: Void
        """
        if 1 <= len(letters) and len(letters) <= 7:
            for letter in letters:
                self.letters[letter.char][0] += 1	# add letter back to bag

    def _remove(self):
        """ Removes a letter from the bag at random.
            @param:.
            @return: list
        """
        letter_obj = ""
        shuffle(Bag.LETTERS)                            # randomize letters
        true = True
        i = 0
        while true and i < len(Bag.LETTERS):
            char = Bag.LETTERS[i]                     # assign random letter
            meta = self.letters[char]
            if meta[0] > 0:           # if available letter

                score = meta[1]       # get score
                letter_obj = Letter(char, score)    # make new Letter

                meta = self.letters[char]
                self.letters[char] = [meta[0]-1, meta[1]]        # decrement availability
                self.length -= 1
                true = False                        # break loop
            else:
                i += 1                              # try again


        if letter_obj:
            return letter_obj
        self.length = 0
        return False

    def swap(letters):
        """ Implements both _add and _remove
        """
        a = []
        self._add(letters)                          # inputs array of letters
        for i in range(len(letters)):
            a.append(self._remove())
        return a                                    # array of letter objects

    def isEmpty(self):
        """ Checks if any letters remain in the bag.
            @param:.
            @return: Boolean
        """
        return self.length == 0