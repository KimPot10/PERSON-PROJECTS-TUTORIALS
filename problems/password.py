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
"""

password = input("Enter Password: ")

while password  