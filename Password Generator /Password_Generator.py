import secrets
import string

alpha = string.ascii_lowercase
Alpha = string.ascii_uppercase
digits = string.digits
spl = string.punctuation
chars = alpha + Alpha + digits + spl
pas = secrets.choice(alpha) + secrets.choice(Alpha) + secrets.choice(digits) + secrets.choice(spl)

try:
    a = int(input("Enter the no. of chars in password (8-12): "))
    if a < 8 or a > 12:
        print("Value out of range. Taking default value of 8.")
        a = 8
except ValueError:
    print("Invalid input. Taking default value of 8.")
    a = 8

for x in range(a - 4):  # Subtract 4 because the password is initialized with 4 characters
    pas = pas + secrets.choice(chars)
    
print(pas)
