# DEVLOG - Will be better formatted later

## Day 1 - Thursday 29th April

- Today the project was started!
- The basic idea I came up with was a turn based rogue like fantasy battler game based in the CLI
- I began by creating a python project with UV and creating a basic welcome screen
- The skeletons for a player class and an enemy class were created along with placeholder stats for attack, etc
- I wanted it to be in the CLI but wanted it to be formatted niceley so I googled for some libraries to help and came across "Rich"
- Rich seemed cool and wanted to test it so i implemented a very basic print round function to use Rich to print the stats of both combatents and it looked nice
- So probably going to stick with that

## Day 2 - Friday 1st May

- Basic combat now works, you can defeat enemies with attacks (ones that have been defined, not all of them so far), block attacks and an evasion system
- Added an action list for player actions
- Actions take up resources
- QoL:
  - Renamed to turns, turns will be moves in a battle, rounds will be a single battle
  - Clear the terminal before printing the round to make it clearer
  - Prints out action list including cost and descriptions
- Still need to do random rolling for enemies before rounds and round rewards
- Things are taking shape nicely though!

## Day 3 - Saturday 2nd May

- Today I want to try and finish the main gameplay loop! I want to get this project done today or tomorrow so I can continue the course!
- Ive added a second enemy type (hydra) and created a generate enemy function in main that will pick an enemy at the start of a round (so we dont get all goblins)
- Decided the game will be 20 rounds long, 10 and 20 will be boss rounds
- Enemies now award gold and their actions now have resource cost (they will only use an action they can afford)

## Day 4 - Tuesday 5th May

- Today I worked on the shop implementation! Items can now be bought for bonuses to the player!
- I also added boss rounds, 10 and 20 (final) and enemies now drop gol

## Day 5 - Wednesday 6th May

- Added a helper function to add to log
- Added a pheonix boss
