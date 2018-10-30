class Rack:
    def __init__():
        self.id = 1         # placeholder
        self.letters = []   # type Letter[]
        self.length = len(self.letters)

    def getId():
        return self.id

    def getLetters():
        return self.letters

    def setId(id):
        self.id = id        # placeholder func

    def setLetters():
        pass                # get letters from bag

    def canTake():
        pass                # check if can take from bag

    def take():             # add func
        pass                # take letter from bag

    def remove(n):
        pass                # removes n letters from self

    def isFull():
        return self.length == 7

    def swap(a):
        for n in a:
            self.remove(n)
            self.take()
