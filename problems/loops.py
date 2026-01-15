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

# Without a loop (tedious!)
print("Welcome student 1")
print("Welcome student 2")
print("Welcome student 3")

# With a loop (efficient!)
for i in range(1, 5):
    print(f"Welcome student {i}")       

#while loop when you don't know how many times it should run. meaning, as long as it's true itutuloy niya lang.

#for loop is best used when you know how many times it should run

#for-each loop parang for loop pero may array

#array is a collection of values
"""
myArray = [values]

myFruits = [banana, strawberry, apple, etc]
"""
