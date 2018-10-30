# Receive Letters

| __Use Case 2__ || Receive Letters |
|:-----------------------------:|:-:|:-----------------------------------------:|
| __Goal in Context__          || Player receives new Letters from Bag |
| __Scope & Level__             || System, Core |
| __Preconditions__             || Players turn, rack is not full. |
| __Success End Condition__     || Rack is full of new Letters. |
| __Failed End Condition__      || Rack is not filled or has same letters. |
| __Primary, Secondary Actors__ || __Primary:__ Rack. __Secondary:__ Player, Bag. |
| __Trigger__                   || Rack is not full at end of turn. Player requests to swap Letters.

| __DESCRIPTION__ | __Step__ | __Action__ |
|
|| 1 | Player selects Letters at start of turn. |
|| 2 | Word is formed and placed on Board. |
|| 3 | System checks validity of Word is checked. |
|| 4 | Player receives appropriate amount of points. |
|| 5 | System requests correct number of Letters from Bag to Rack. |
|| 6 | System updates Rack. |
|| 7 | System ends current Player’s turn. | 
||
| __EXTENSIONS__  | __Step__ | __Branching Action__  |
|| 3a | Word is not valid therefore all Letters placed will be returned to players Rack. |
|| 1a | Player may decide to discard any number of Letters on their Rack and receive new Letters at random then proceed with their turn. (Once per turn) |
|| 1b | Bag is empty so Letters cannot be swapped. |
|| 1c | Bag is empty so Letters cannot be replaced. |

| __VARIATIONS__ | __Step__ | __Branching Action__ |
