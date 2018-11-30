# Week 10 OO Analysys & Design Projects Minutes

__Week:__ 10 __Start Date:__ 2018/11/27 __Present:__ Connor, Jake, Martynas, James __Excused:__ Michael(3rd year project meeting) __Absent: Remote:__

- Connor chosen to take minutes.
- Goal of the day is to complete board class.
- Temporarily removed letter class for testing/ implementation purposes.
- Jake Connor and James working on board class (problem solving and improving search algorithm)
- Issue with search algorithm, successfully created word on first iteration but failed to do so on second iteration.
- Board now successfully updating when a valid word is placed.
- Group discussion on what the next step should be.
- Decided that implementing sockets with the board should take precedence for next meeting.

# Week 10 OO Analysys & Design Projects Minutes

__Week:__ 10 __Start Date:__ 2018/11/28 __Present:__ Connor, Michael, Jake, Martynas, James __Excused:__ __Absent: Remote:__

- Minutes : Connor
- Continued with yesterdays plan of getting the board class and sockets working.
- Connected html to flask server.
- No issues with this as it was pretty straight forward (message passing).
- "Make move" fully implemented.
- Starting "Pass".
- Very trivial since it was implemented as part of "Make move".
- Moving onto final action, "Swap Letters".
- Refactoring of Bag class required and added letter class back in again.
- Key issues with bag class were:
    - dictionary of tuples rather than lists
- Issue quickly resolved, updating values and having it persist throughout the game.
- Implemented sockets for swap letters, fully implemented.
- Checklist of features to date, Player can:
    - 2 players can connect and only then does the game commence.
    - Make a move, if a move is valid board updated else next players turn.
    - Pass, which lets the other player take their turn.
    - Swap Letter, completely updates players whole rack with letters in bag.
- Our next goal is to render it outside of the browsers console and onto the web page.

# Week 10 OO Analysys & Design Projects Minutes

__Week:__ 10 __Start Date:__ 2018/11/29 __Present:__ Connor, Michael, Jake, Martynas, James __Excused:__ __Absent: Remote:__

- Connor is doing the minutes today.
- We wrote out the goals of the day which were to render the template for the game and to get the end game sorted.
- We used flask render to a dynamic page that both players shared to an extent ie the board but not the wracks.
- We used a bit of bootstrap too just the make it look a bit nicer.
- We finally moved onto to sorting the end game state. This will happend on one of two events, either the bag is empty or one of the players reaches 100 points. This was a last minutes decision because we believed it added a bit of extra competition and excitement to the game.
- End game sorted!
- We now are rendering different templates for both winners and losers. (Ideas for losers: Rick Astley, Careless Whispers; Winners: A happy picture. Not important)
- Resolving issues with flask refusing to render new templates.
- Issue partially resolved, trying to avoid iframes since flask appears to not like them and may be settling for simple jpg's. 
- Currently working on calculating scores.
- Scores of valid words are now calculated.
- Bug found with horizontal placement!!
- Bug fixed, issue was row column were inverted...
- Pushed & merged
- Formatting files using PEP8.