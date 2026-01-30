"""
Problem: Password Validator
Write a program that checks if a password is strong enough.
The program should:

Ask the user to enter a password
Check if the password meets ALL these requirements:

At least 8 characters long
Contains at least one number (0-9)
Contains at least one uppercase letter (A-Z)
Contains at least one lowercase letter (a-z)


If the password is valid, print "Password is strong!"
If not, tell the user which requirements are missing
Keep asking until they enter a valid password

Get the password from the user
Check all requirements (length, has number, has uppercase, has lowercase)
If it fails, show what's wrong and ask again
If it passes, say it's strong and stop

You want to keep looping UNTIL the password is valid
So think: while password is NOT valid:
You'll need to check if ALL requirements are met

For checking if password contains at least one number:

You can't use .isnumeric() because that checks if ALL characters are numbers
Instead, loop through each character and check if ANY character is a digit:
"""

"""
references
while time <= 0:
    time = int(input("Enter Time in Years: "))
    if time <= 0:
        print("Time is counted in years")
"""


# input

password = input("Enter password: ")

# validators variables

has_number = False
has_upper = False
has_lower = False
is_long_enough = False

# check the length

if len(password) == 8:
    is_long_enoug = True

# loop

for char in password:
    if char.isdigit():
        has_number = True
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    password = input("Enter password: ")
    
# Step 5: Check if ALL requirements are met
if has_number and has_upper and has_lower and is_long_enough:
    print("Password is strong!")
else:
    print("Password is weak")
    # Print what's missing