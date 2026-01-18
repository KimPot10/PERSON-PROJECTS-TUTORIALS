#printing stars in python using loop

# "i" is oftenly used because of its meaning iteration meaning to repeat. range is number of how many times it will be repeated
for i in range (1, 6):
    #since nasa loob siya ng indent mag start na rin ito ng iteration
    print('*' * i)
    # asterisk multiplied by the iteration. kada row ma-multiply siya

"""
For any pattern, ask yourself these questions:

How many rows? → Your outer loop... 5
For each row, what do I print? → Your inner calculations

How many spaces?
How many stars/symbols?
What's the pattern/formula?


Break it into parts:

Top half vs bottom half
Left side vs right side
"""
#without ai. paano mo siya gagawing pyramid?

rows = 5
for i in range(1, rows + 1):
    spaces = rows - i
    stars = (2 * i) - 1
    print(' ' * spaces + '*' * stars)

#a comment for a commit