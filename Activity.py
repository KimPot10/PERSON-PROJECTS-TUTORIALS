#Activity 1

print("=====Activity 1=====")

#Input with validations
a = str(input("Enter First Word: "))
if a.isnumeric():
    print("Invalid input! Exiting program.")
    exit()

#second word with validation
b = str(input("Enter Second Word: "))
if b.isnumeric():
    print("Invalid input! Exiting program.")
    exit()

#separator special character
c = str(input("Enter Separator (special characters only): "))
if not c.isalnum() and c != "" and not c.isspace():
    pass
else:
    print("Invalid input! Exiting program.")
    exit()

#With Space
print(a, b, end="\n")

#Without newline   
print(a, b, end="")

#With Separator
print(a, b, sep=c)

#Without space
print(a, b, end="\n" , sep="")







