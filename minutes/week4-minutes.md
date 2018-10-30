# Week 4 OO Analysis & Design Project Minutes

---

__Week__: 4
__Start Date__: 2018/10/18
__Present__: Jake, Connor, Michael, Martynas
__Excused__: James (Interview)
__Absent:__
__Remote:__

---

## Minutes:
- Jake was selected to write the minutes
- Connor was selected to draw the class diagram on a white board
- We decided on the following:
  - A Board has many squares
  - A Board has many Words
  - A Word has many Letters
  - A Letter belongs to many words
  - A Rack can have 0  to many Letters
  - A Letter belongs to 0 to 2 Racks
  - A Bag contains many Letters
  - A Rack interfaces with a Bag and Players
  - A Rack has many Letters
  - A Player interfaces with the Board
- We found a flaw in our design and have now decided that as a player is making their move, we build up an array of Squares that will be encapsulated within a word object. When a player is satisfied with their move isValidWord() is called, if it is valid, the letters are placed on the board.
- We completed the class diagram and are satisfied with the design. 
- We have divided up and handed out the use case descriptions for everyone to work on until the next meeting
---

## Action Items:
- Use Case Descriptions delegated as follows:
    - Jake: Game Created
    - Michael: First Move
    - Martynas: Next Move
    - Connor: Receive new letters
    - James: Game Over
