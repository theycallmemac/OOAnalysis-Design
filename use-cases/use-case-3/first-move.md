# First Move

| __Use Case 3__ || First Move |
|:-----------------------------:|:-:|:-----------------------------------------:|
| __Goal in Context__          || For the first player to make their move |
| __Scope & Level__             || Global, System |
| __Preconditions__             || Must be able to play valid move, and must be the player’s move |
| __Success End Condition__     || Player has placed valid tiles, has passed their turn, or swaped 1-7 tiles |
| __Failed End Condition__      || Player fails to make a valid move |
| __Primary, Secondary Actors__ || __Primary:__ Player, Word. __Secondary:__ Rack, Board, Tile, Letter. |
| __Trigger__                   || Player move is flagged to `True` 

| __DESCRIPTION__               | __Step__ | __Action__ |
|
|| 1 | Player is presented with options |
|| 2 | Player can attempt to place valid word |
|| 3 | Word is checked to be valid |
|| 4 | Word is placed on the board, and move terminated |
|| 5 | Player swaps letters from their rack |
|| 6 | Move is terminated |
|| 7 | Player passes their turn, move is terminated |
||
| __EXTENSIONS__  | __Step__ | __Branching Action__  |
|| 3a | Move is not valid | 
|| 3a | Turn is still open |
|| 5a | Player tries to swap an incorrect amount of letters |
|| 5a | Move is still open | 
| __VARIATIONS__ | __Step__ | __Branching Action__ |
|| 2b | Player may pass their turn to the next player | 
|| 2b | Player may swap letters from their rack with bag | 
