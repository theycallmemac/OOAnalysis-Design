from copy import deepcopy


def placeLetters(b, input):
    """
    Places users letters and checks if a valid word exists
    @param tuple (letter,[x,y])
    @return: set of valid words
    """
    words = set()
    valids = []
    boardC = deepcopy(b)

    for t in input:
        boardC[t[1][1]][t[1][0]] = t[0]
    for t in input:
        w = tryMake(boardC, t[1])
        if w != []:
            for wordt in w:
                words.add(wordt)
    return boardC


def tryMake(b, coord):
    x = coord[0]
    y = coord[1]

    words = []
    i = x
    while b[y][i] != "" and i >= 0:
        i -= 1
    i += 1
    j = i
    while b[y][j] != "" and j < 15:
        j += 1
    j -= 1
    word = ""
    while i < j:
        word += b[y][i]
        i += 1
    word += b[y][i]
    words.append(word)

    word = ""
    i = y
    while b[i][x] != "" and i >= 0:
        i -= 1
    i += 1
    j = i
    while b[j][x] != "" and j < 15:
        j += 1
    j -= 1
    word = ""
    while i < j:
        word += b[i][x]
        i += 1
    word += b[i][x]
    words.append(word)
    return words


b = [["", "", "", "", ""],
     ["", "", "", "", ""],
     ["", "", "a", "", ""],
     ["", "", "t", "", ""],
     ["", "", "", "", ""]]

print(b)
print(placeLetters(b, [("b", [2, 1])]))
print(b)
