# Week 3 OO Analaysis & Design Project Minutes
---

__Week:__ 3
__Start Date:__ 2018/10/11
__Present:__ James, Jake, Michael, Martynas and Connor
__Excused:__
__Absent:__
__Remote:__

---

## Minutes:
- The first thing we need to do today is define our classes.
- Jake was tasked with this last week. We discussed his results and ended up with the following class list:
    - Player
        - Attr:
            - ID
            - Rack (made of Letters)
            - Score
        - Methods:
            - getters/setters
            - placeLetter()
            - swapLetters()
            - pass()
            - updateScore()
    - Board
        - Attr:
            - Matrix of Square Types
        - Methods:
            - Setters/Getters
            - update()
            - isValidMove()
    - Rack
        - Attr:
            - ID
            - Array of Letter Types
        - Methods:
            - canTake()
            - isFull()
            - add()
            - remove()
            - swap()
            - getters/setters
    - Letter
        - Attr:
            - ID
            - Character
            - Score
        - Methods:
            - Setters/Getters
    - Word
        - Attr:
            - ID
            - Array of Letters
            - Score
        - Methods:
            - isWord()
            - calcScore()
            - Setters/Getters
    - Bag
        - Attr:
            - Array of Letter Types: 
        - Methods:
            - add()
            - remove()
            - isEmpty()
            - getters/setters
    - Square
        - Attr:
            - Letter: int
            - X co-ordinate: int
            - Y co-ordainte: int
            - isStar: Bool
        - Methods:
            - Getters/setters

- Leave out multipliers for now. Perhaps added once we pass the requirements.
- Python & Flask is the way to go - we think.
- We are also considering using the built-in Python socket library.
- Due to time constraints, we have agreed to split up the CRC's for the week among the team.
---

## Action Items
- Split CRC's for the weekend as follows:

#### Connor
- Board
    - square[Square][Square]
    ========
    - set()
    - get()
    - update()
    - isValidMove()
- Bag
    - letters[Letter]
    - =======
    - add()
    - remove()
    - isEmpty()
    - setBag()
    - getBag()

#### James
- Rack
    - id: int
    - letters[Letters]
    ========
    - getId()
    - getLetters()
    - setId()
    - setLetters()
    - canTake()
    - remove()
    - isFull()
    - add()
    - swap()

- Square
    - x: int
    - y: int
    //- multiplier: int//
    - letter: Letter
    - score: int
    - isMiddle: Bool
    - =======
    - get()
    - set()

#### Mike
- Word
    - id: int
    - score: int
    - letters[Letters]
    ========
    - isValid()
    - calcScore()
    - getScore()
    - setScore()

### Martynas
- Letter
    - id: int
    - character: char
    - score: int
    - ======
    - set()
    - get()

### Jake
- Player
    - id: Integer
    - score: Integer
    - isTurn: Boolean
    - =======
    - placeLetter()
    - get()
    - set()
    - updateScore()
    - pass()
    - swapLetter()

---
