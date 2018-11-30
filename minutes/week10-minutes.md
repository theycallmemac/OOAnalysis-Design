# Week 10 OO Analysys & Design Projects Minutes

__Week:__ 10 __Start Date:__ 2018/11/26 __Present:__ Connor, Michael, Jake, Martynas, James __Excused: Absent: Remote:__

- Connor volunteered to take minutes.
- Goals for the meeting is to get sockets and flask server working and flush out board class.
- Jake and James researched flask/socketio and quickly implemented it into our server class.
- Proceeded onto board class.
- Rather than everyone coding we decided to do joint programming (reduce syntax errors and ensure valid logic).
- Refactored board class.
- Implemented core functions.
- During implementation bugs arose but core logic is implemented.
- Discussed and whiteboarded potential fixes and approaches for next meeting.

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

__Week:__ 10 __Start Date:__ 2018/11/27 __Present:__ Connor, Michael, Jake, Martynas, James __Excused:__ __Absent: Remote:__

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
