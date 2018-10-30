# Game Creation

| __Use Case 1__ || Game Creation |
|:-----------------------------:|:-:|:-----------------------------------------:|
| __Goal in Context__          || Scrabble game created |
| __Scope & Level__             || System, Core |
| __Preconditions__             || None |
| __Success End Condition__     || Game created |
| __Failed End Condition__      || Game not created, users haven’t connected |
| __Primary, Secondary Actors__ || __Primary:__ Players. __Secondary:__ None |
| __Trigger__                   || Users connect to server
|
| __DESCRIPTION__               | __Step__ | __Action__ |
|
|| 1 | Player 1 connects server |
|| 2 | Game instance created |
|| 3 | Player 2 connects to player 1’s game instance |
|| 4 | Rules are printed out to the screen |
|| 5 | Board, Racks and bag are initialized |
||
| __EXTENSIONS__  | __Step__ | __Branching Action__  |
|| 2a | Game fails to create |
|| 3a | Player 2 never joins |
|| 5a | Board, racks or bag are not initialized |
|
| __VARIATIONS__ | __Step__ | __Branching Action__ |
