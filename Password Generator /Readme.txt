---

# Python Password Generator with Error Handling

## Description

This is an enhanced Python script for generating a random password. The generated password will contain at least one lowercase letter, one uppercase letter, one digit, and one special character. The user can specify the length of the password. Error handling is implemented for invalid or out-of-range inputs.

## Requirements

- Python 3.x
- Standard Python libraries (`string`, `secrets`)

## How to Run

1. Clone the repository or download the Python script.
2. Open a terminal and navigate to the folder where the script is located.
3. Run the script by executing `python <script_name>.py`.

## User Input

The script will ask the user to input the desired length of the password, which should be between 8 and 12 characters. 

- If the user enters an invalid input (e.g., text), the script will default to an 8-character password.
- If the user enters a length that is outside the range of 8-12 characters, the script will also default to an 8-character password.

## Code Explanation

- The `secrets` module is used for generating cryptographically secure random characters.
- The `string` module is used to get sets of all lowercase and uppercase ASCII characters, digits, and punctuation marks.
- The password is initialized with one character from each set (lowercase, uppercase, digit, punctuation) to ensure diversity in character types.
- Additional characters are added to the password until it reaches the user-specified length, or defaults to 8 characters in case of invalid or out-of-range inputs.
- Error handling is implemented using Python's `try` and `except` blocks.

## Example Output

```
Enter the no. of chars in password (8-12): abc
Invalid input. Taking default value of 8.
xR9?dj2!
```

```
Enter the no. of chars in password (8-12): 15
Value out of range. Taking default value of 8.
hS3@pq8x
```
