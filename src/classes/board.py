from src.classes.square import Square
from src.classes.word import Word
import copy 

class Board:
    def __init__(self):
        self.board = [[ " " for i in range (0,15) ] for j in range (0,15)]
        self.board[2][3] = "C"
        self.board[5][3] = "T"


    def isValid(self, coord):
        """
        Checks coord is valid coordinates (within range (0-14)), checks coord is empty.
        @param coord (x,y)
        @return: Boolean
        """
        x,y = coord
        if 0<=x and 15> x and 0<=y and 15>y:
            if self.board[y][x] == "":
                return True
        return False

    def tryMake(self, b, coord):
        row = coord[0]
        col = coord[1]
        print(b)
        words = []
        i = row
        while b[row][i] != " " and i >= 0:
            i -= 1
        i+=1
        j=i
        while b[row][j] != " " and j<15:
            j+=1
        j-=1
        word = ""
        while i<j:
            word +=b[row][i]
            i+=1
        word += b[col][i]
        if len(word) >= 2:
            words.append(Word(word))

        word = ""
        i=row
        while b[i][col] != " " and i >=0: 
            i-=1
        i+=1
        j=i
        while b[j][col] != " " and j < 15:
            j+=1
        j-=1
        word=""
        while i <j:
            word += b[i][col]
            i+=1
        word +=b[i][col]
        if len(word) >= 2:
            words.append(Word(word))
        return words

    def placeLetters(self, input):
        """
        Places users letters and checks if a valid word exists
        @param tuple (letter,[x,y])
        @return: set of valid words
        """
        words = set()
        valids= []
        boardC = copy.deepcopy(self.board) 
        for t in input:
            boardC[t[1][0]][t[1][1]] = t[0]
        for t in input:
            w = self.tryMake(boardC,t[1])
            if w != ["",""]:
                for wordt in w:
                    if wordt.isValid():
                        words.add(wordt)
                        valids.append(t)
        validlist = []
        for i in range(len(valids)):
            v = valids.pop()
            if v not in validlist:
                validlist.append(v)
        if len(words) and len(validlist) == len(input):
            for valid in validlist:
                self.update(valid)
            return words
        else:
            print(words)
            return False

    def update(self, t):
        """
        Update the board after a valid move is played.
        @param tuples [(letter,[x,y])].
        @return: Void
        """
        x = t[1][0]
        y = t[1][1]
        self.board[x][y] = t[0]
    
    # def _set(self, x1, y1, x2, y2):
    #     """
    #     Updates board at end of players turn.

    #     @param self (Board): Overwrites board with updated board.
    #     @return: Void
    #     """
    #     self.board = update(x1, y1, x2, y2)


    def get(self):
        return self.board

