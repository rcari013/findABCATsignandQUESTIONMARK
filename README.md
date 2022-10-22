# CSE210 Find A B C @ and ?
Find A, B, C, @ and ? game from BYU CSE210

Find A, B, C, @ and ? (including it's small letter counterpart) is a game in which the player seeks to find the characters mentioned on the title.

Rules:

1. The player starts with 500 points. Each character that collides with the robot that are not within the characters mentioned causes the player to lose 20 points.

2. Each time a question mark lands at the nearest bottom will cause 5 points deduction.

3. Colliding with question mark (?) will also either give you 20 points or deduct you 5 points.

4. Colliding with at sign (@) is the riskiest to collide with as it eithers gives you 50 chance to either lose points for 80 or get points for 100.

5. The player must find the characters mentioned to keep the points above 0 or the game will be over which causes all characters to turn into white and game will move slowly.

Based from the game greed, however, the mechanics is different.

---
## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 jumper
or
py jumper
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- findABC-ATsignandQUESTIONMARK              (source code for game)
  +-- game              (specific classes)
  +-- __main__.py       (program entry point)
  +-- constants.py       (some variables to use)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.8.0

## Authors
* Romelito Carino