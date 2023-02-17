# Lunk Game Spec Sheet
## version 1.0

## Table of contents
- [Objective](#objective)
- [Player Movement](#player-movement)
- [Enemy Movement](#enemy-movement)
- [Enemy Interaction](#enemy-interaction)
    - [Attack Enemy Options](#attack-enemy-options)
    - [Enemy Attack Pretty Lady](#enemy-attack-pretty-lady)
- [Pretty Lady Movement](#pretty-lady-movement)
- [Score System](#score-system)
    - [Health Bar](#health-bar)
    - [High Score](#high-score)
    - [Bored Bar](#bored-bar)


## Objective
The main objective of Lunk, the player character, is to do what he wants and do it when he wants.
The secondary objective is for Lunk to not do what he does not want to do.

Lunk positive interactions:
* Lunk wants to crush his enemies.
* Lunk wants to save the pretty ladies.


Lunk negative interactions:
* fall off the map, reappear somewhere random
* crush pretty ladies
* ingest non-tasty things


## Player Movement
Lunk always goes forward, but he can choose to turn to the left or the right.

This means movement is rotational in nature. Lunk's heading will be adjusted but not suddenly altered. The purpose of this movement system is to give Lunk the feeling of an unwieldy character who is hard to control directly. The player can steer Lunk, but not command him. The same thought process was used when creating Lunks abilities and enemy interactions.

If Lunk falls off the map, he jumps back up so high that the landing spot is a random area within a 10 by 10 area near the fall point

## Enemy Movement
Enemies will wander the map after being spawned.

* if a pretty lady is within 10 squares, enemies will walk generally toward the pretty lady
* if a pretty lady is within 4 squares, enemies will run directly towards the pretty lady
* if Lunk is greater than 5 squares enemies will walk generally away from Lunk
* if Lunk is less than 5 squares and a pretty lady is within 10 squares, enemies will run directly towards Lunk to stop him from saving the pretty lady
* if enemy is blocked (on a wall or other object), walk towards Lunk

## Enemy Interaction
When the hit box interacts, rotate through the 3 abilities described [here](#attack-enemy-options).

### Attack Enemy Options
Options will rotate through every enemy interaction in a loop. The options to attack an enemy are:
* Crush

  The simplest enemy interaction. Any enemy is simply crushed beneath Lunk's feet with no chance of survival.
* Throw

  Lunk chooses to remove his enemy from sight by tossing it out like the trash. Enemies will fly forward 2 or 3 spaces before dying in the embrace of the ground.
If a pretty lady is crushed by Lunk's flying enemy, Lunk losses his points from his [health bar](#health-bar).
* Eat

  Lunk gets hungry, he eats his enemy. Eating can be positive or negative depending on what is eaten.

### Enemy Attack Pretty Lady
Enemies will try to kill or kidnap pretty ladies if they see any.

The mechanics of this are to be decided.

## Pretty Lady Movement
Pretty ladies will wander the map when spawned.

* if an enemy if within 6 squares of a pretty lady, they will walk in the opposite direction
    * this is ignored if Lunk is nearby in favor of Lunk related logic
* if Lunk is within 12 squares of a pretty lady, they will walk towards Lunk
* if Lunk is within 5 sqaures of a pretty lady, they will stand still and make heart emojis at Lunk 

## Score System
### Health Bar
Lunk can only do so many things he doesn't like doing before deciding to sleep and ignore everything.
The health bar is a countdown to Lunk sleeping out of anger. When it reaches 0, the game is over.

### High Score
Lunk gains points for doing things he likes to do.
Each favorable action adds to the total high score for an amount specific to each action

### Bored Bar
Each level has a set timer that counts down to the moment Lunk goes to sleep from boredom.