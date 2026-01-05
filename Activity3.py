print("=====Activity 3=====")

#Input
a = int(input("Enter First Number: "))
if not a.isnumeric():
    print("Invalid input! Exiting program.")
    exit()

b = int(input("Enter Second Number: "))
if not b.isnumeric():
    print("Invalid input! Exiting program.")
    exit()
    
c = str(input("Enter Separator (special characters only): "))
if not c.isalnum() and c != "" and not c.isspace():
    pass
else:
    print("Invalid input! Exiting program.")
    exit()

print(str(a) * 6, str(b) * 4, sep=c)

