# Scenarios

- __User John logs on__
    - __Current System State:__ There is no game in play at this time.

    - __Informal Scenario:__ Game is created by either John when he joins the server. The game can only be played when both John and Mary have connected to the server. When both John and Mary have connected to the server, the rules of the game are printed on the screen in front of them. These rules include the number of points each letter is worth, as well as the coloured tile bonuses which exist on the board.

    - __Next Scenario:__ The game commences and the order in which players move is determined by the server. John was selected at random by the server to play first.


- __The server starts the game__
    - __Current System State:__ The players have received 7 tiles at random each. The game board is currently empty.

    - __Informal Scenario:__ When the board is empty, the first move should be John placing a word on the board which runs through the star square. Anything else is flagged as an illegal move by the server.

    - __Next Scenario:__ John can pass his turn to Mary or alternatively, if he cannot create a valid word from the seven letters in his rack, he has two other options. He may pass his turn to Mary or swap 1 - 7 of the tiles in his rack for an equal amount of lettered tiles from the bag.


- __John makes a move__
    - __Current System State:__ John has swapped his 7 tiles for 7 new tiles from the bag. His previous tiles have been put back into the bag.

    - __Informal Scenario:__ John places five tiles to form a valid word. This word runs through the star tile, making this a valid first move.

    - __Next Scenario:__ It is now Mary’s turn to place her tiles on the board. She must append these tiles to the tiles John has placed to form another word.

- __Mary makes a move__
    - __Current System State:__ A single, valid word exists on the board, and this word runs through the star tile. It is now Mary’s turn.

    - __Informal Scenario:__ Mary now follows the same process that John had the move before. She may pass her turn to John, or she may swap out letters for her own. Her turn, and all subsequent turns come with the key difference of having to try append tiles with a word on the board since the star is no longer available.

    - __Next Scenario:__ John repeats his previous step and once his turn is over Mary then repeats that step, until no possible words can be played, the board is full, or no tiles remain.


- __A winner is decided__
    - __Current System State:__ The process of making moves has continued until no tiles remain to place on the board

    - __Informal Scenario:__ A score is now calculated by the server and a winner is declared by having a greater number of points.

    - __Next Scenario:__ The game is closed by the server.



