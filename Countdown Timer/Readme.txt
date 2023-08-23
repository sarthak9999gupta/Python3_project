---

## Countdown Timer in Python

### Description
This is a simple Python script that lets the user input a number of seconds and then counts down to zero, displaying the remaining time in a `MM:SS` format.

### Author
Sarthak Gupta

### Date of Creation
24th August 2023

### Requirements:
- Python 3.x

### How to Run:
1. Ensure you have Python 3 installed on your machine.
2. Save the code in a file, say `countdown_timer.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the file.
5. Run the command:
   ```
   python3 countdown_timer.py
   ```
6. You will be prompted to enter the time in seconds. Input the desired time and press Enter.
7. The program will then display the countdown and print "times up" once the timer reaches zero.

### Code Structure:
- The function `countdown(t)` takes in a time `t` in seconds and manages the countdown logic.
- The `divmod` function is used to compute the minutes and seconds from the total seconds input.
- The time is then formatted to `MM:SS` format using the `format` method.
- `time.sleep(1)` ensures that the countdown decrements by one second.
- Once the countdown completes, "times up" is printed.

### Potential Enhancements:
- Integrate with a GUI for a more visual experience.
- Add sound notifications or alerts for when the time is up.
- Allow input in `MM:SS` format in addition to just seconds.

---
