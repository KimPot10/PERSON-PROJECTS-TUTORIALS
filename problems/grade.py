"""

MALI

grade = int(input("Enter your grade: "))

if grade == 91 < 100:
    print("Your grade is A")
elif grade < 90:
    print("Your grade is B")
elif grade < 80:
    print("Your grade is C")
elif grade <= 70:
    print("Your grade is D")
elif grade > 101:
    print("Invalid")
else: 
    print("Your grade is F")

"""

grade = int(input("Enter your grade: "))
# This states that grades  more than zero OR grades more than 100 is incorrect
if grade < 0 or grade > 100:
    print("Invalid Grade")
# this states grade 90 to 100 are A
elif grade >= 90:
    print("Your grade is A")
# this states 
elif grade >= 80:
    print("Your grade is B")
elif grade >= 70:
    print("Your grade is C")
elif grade >= 60:
    print("Your grade is F")
