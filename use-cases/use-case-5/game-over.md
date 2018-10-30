# Game Over

| __Use Case 5__ || Game Over |
|:-----------------------------:|:-:|:-----------------------------------------:|
| __Goal in Context__          || The Game is closed by the server |
| __Scope & Level__             || System, Core |
| __Preconditions__             || The process of making moves has continued until no tiles remain to place on the board. |
| __Success End Condition__     || A score is now calculated by the server and a winner is declared by having a greater number of points. |
| __Failed End Condition__      || None |
| __Primary, Secondary Actors__ || __Primary:__ Board. __Secondary:__ Rack, Bag, |
| __Trigger__                   || No possible words can be played, the board is full, or no tiles remain in the bag.
|
| __DESCRIPTION__               | __Step__ | __Action__ |
|
|| 1 | No possible words can be played, the board is full, or no tiles remain in the bag. |
|| 2 | The system closes the board from the players. |
|| 3 | The system calculates the overall score of both players. |
|| 4 | Player with the highest score is declared the winner |
|| 5 | The system closes the game. |
||
| __EXTENSIONS__  | __Step__ | __Branching Action__  |

| __VARIATIONS__ | __Step__ | __Branching Action__ |
