# Week 12 OO Analysys & Design Projects Minutes

__Week:__ 12 __Start Date:__ 2018/12/12 __Present:__ Connor, Jake, Martynas, James, Michael __Excused: Absent: Remote:__

- Connor has volunteered to take this meetings minutes.

- On todays agenda we have:
    - To add restrictions that were removed for demonstration/presentation purposes.
    - Possibly containerize the project so users won't have to affect their current system by downloading dependencies.

- The restrictions that were removed for the presentation purposes were the constraints by the rack i.e. having to play a letter that is on the rack. 
This was no issue at all as it was done on the clients end. 
    - One key rule that came from this implementation was that if the player made an invalid move such as using a letter they didn't have in their rack, their turn would be skipped. This added an extra layer of complexity and thinking for the players adding to the overall game.

- Secondly we decided to dockerize the project. This was primarily requested by James for the reasons stated previously. 
- The first challenge of this current meeting was to learn how to dockerize and flask app.
    - This issue was quickly resolved with the aid of some research.
- The second challenge we faced was CORS (Cross Origin Resource Sharing). This arose when we tried to host a game but the board wouldn't appear. We found that flask had an extension called flask-cors that could handle this. By using this extension we could easily allow resource sharing across origins and the game ran as intended.
![](https://i.imgur.com/ozYBXee.jpg)
