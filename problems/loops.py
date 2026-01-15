#for is used of loops

#mayroon din while
"""
for i in range(10):
    print(i)  # Prints 0 to 4
"""
#Commit kasi baka masira streak
import random

dice = random.randint(1,6)
print(dice)
count = 1

while dice != 6:
  dice = random.randint(1,6)
  print(dice)
  count += 1
print('You got 6!')
print('You rolled',count,'times')

