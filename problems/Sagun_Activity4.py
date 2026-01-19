"""Write a Python program to get a string made of the first 2 and last 2
characters of a given string. If the string length is less than 2, return the emptys string instead.
"""

input_string = input("Enter a string with more than 2 letters: ")

#if less than 2 ang input
if len(input_string) < 2:
    result = ""

# slicing indeces [0:2] and [-2:]
else:
    first_two = input_string[0:2]
    last_two = input_string[-2:]
    result = first_two + last_two
print("Output:", result)


