# Next players move

| __Use Case 4__ || Next players move |
|:-----------------------------:|:-:|:-----------------------------------------:|
| __Goal in Context__          || For the next player to make a move |
| __Scope & Level__             || Global, System |
| __Preconditions__             || Must make a valid move and must be players move |
| __Success End Condition__     || Player has placed valid tiles, has passed their turned or swapped 1-7 letters from their rack  |
| __Failed End Condition__      || Player fails to make a valid move |  
| __Primary, Secondary Actors__ || __Primary:__ Player, Word. __Secondary:__ Rack, board, Tile, Letter |
| __Trigger__                   || Player move is flagged to "True" 
|
| __DESCRIPTION__               | __Step__ | __Action__ |
|| 1 | Player is presented with options |
|| 2 | Player can attempt to place a valid word | 
|| 3 | Word is checked to be valid |
|| 4 | Word is placed on the board, and move is terminated |
|| 5 | Player swaps letters from their rack and the bag |
|| 6 | Move is terminated |
|| 7 | Player passes their turn, move is terminated ||
|
| __EXTENSIONS__  | __Step__ | __Branching Action__  |
|| 3a | Move is not valid |
|| 3a |Turn is still open |
|| 5a | Player tries to swap an incorrect amount of letters |
|| 5a | Move is still open |
|
| __VARIATIONS__ | __Step__ | __Branching Action__ |
|| 2b | Player may pass their turn to the next player |
|| 2b | Player may swap letters between their rack and the bag |
