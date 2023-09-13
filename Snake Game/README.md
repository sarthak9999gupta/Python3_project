# Snake Game
This README file provides an overview of a simple Snake Game implemented in Python using the Turtle graphics library. The game features a snake that moves around the screen, eating food to grow longer while avoiding collisions with the border or itself.

## Table of Contents
1. [Game Overview](#game-overview)
2. [Setup](#setup)
3. [Game Controls](#game-controls)
4. [Scoring](#scoring)
5. [Game Over](#game-over)
6. [Customization](#customization)

## 1. Game Overview
The Snake Game is a classic arcade-style game where you control a snake. The objective is to eat the red food items that appear on the screen to score points and grow longer. As the snake consumes food, it increases in size, making the game progressively challenging. The game continues until the snake collides with the screen's border or itself.

## 2. Setup
- Ensure you have Python installed on your computer.
- The game utilizes the Turtle graphics library, which is a standard library in Python, so no additional installations are required.
- Copy and paste the provided code into a Python environment or script.
- Run the code to start the game.

## 3. Game Controls
- Use the following keyboard controls to navigate the snake:
  - **W**: Move the snake up
  - **S**: Move the snake down
  - **A**: Move the snake left
  - **D**: Move the snake right

## 4. Scoring
- Your score is displayed at the top of the game window.
- You earn 10 points each time the snake consumes a red food item.
- The high score achieved during a game session is also displayed.

## 5. Game Over
The game can end in two ways:
1. **Collision with the Border**: If the snake collides with the screen's border, the game will pause briefly, and then you can restart the game by pressing any key.
2. **Collision with Itself**: If the snake collides with its own body, the game will pause briefly, and then you can restart the game by pressing any key.

## 6. Customization
You can customize the game by modifying the code. Here are some possible customizations:
- **Game Speed**: Adjust the `delay` variable to change the speed of the snake.
- **Game Window Size**: Modify the `width` and `height` parameters when setting up the screen (e.g., `wn.setup(width=800, height=800)`).
- **Snake Appearance**: You can change the snake's shape, color, and size by modifying the `head` and `segments` attributes.
- **Food Appearance**: Customize the food's shape, color, and size by modifying the `food` attributes.

Feel free to explore and enhance the game to make it your own!

Have fun playing the Snake Game!
  
