# Pong Game
This is a basic implementation of the classic Pong game using Python and the Turtle graphics library. The game features two paddles, one for each player, and a ball. The objective is to bounce the ball back and forth using the paddles and prevent it from reaching the edges of the screen. Each time the ball passes a player's paddle and reaches the edge of the screen, the opposing player scores a point. The game continues indefinitely until you decide to exit.

## How to Play
- Player A controls their paddle using the "W" key to move up and the "S" key to move down.
- Player B controls their paddle using the "Up" arrow key to move up and the "Down" arrow key to move down.
- The game keeps track of the score for both players at the top of the screen.
- The ball will bounce off the paddles and the top and bottom edges of the screen.
- The game features a bouncing sound effect when the ball hits the paddles or the top and bottom edges.

## Dependencies
This game requires the Python Turtle graphics library, which is included in Python's standard library, so there's no need for additional installations.

## Installation
Simply clone or download this repository to your local machine and run the Python script using Python 3.

```bash
python3 pong_game.py
```

## Controls
- Player A: "W" (up) and "S" (down) keys
- Player B: "Up" (up) and "Down" (down) arrow keys
- Exit the game by closing the window or pressing Ctrl+C in the terminal.

## Acknowledgments
- This game was created by Sarthak Gupta.
- Sound effects are played using the "afplay" command, which works on macOS. You may need to modify the sound playing code if you're using a different operating system.

Enjoy the game!
