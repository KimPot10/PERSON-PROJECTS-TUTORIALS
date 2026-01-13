#Logical operators

# AND - both conditions must be true
# OR - at least one is true
# NOT - used to reverse the the result of conditional statements

#Use an if statement to print "YES" if either a or b is equal to c.

"""

MALIIIII
a = 2
b = 50
c = 2
if a or b == c:
  print("YES")
"""

#the correct logic should be 

a = 2
b = 50 
c = 2
#the logic is more complete rather than "a or b == c"
if a == c or b == c:
    print("YES")
else:
    print("no")