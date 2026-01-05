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
sepa = str(input("Enter Separator (special characters only): "))
if not sepa.isalnum() and sepa != "" and not sepa.isspace():
    pass
else:
    print("Invalid input! Exiting program.")
    exit()

#With Space
print(a, b, end="\n")

#Without newline    
print(a, b, end="")

#With Separator
print(a, sepa, b, sep="")

#Without space
print(a, b, end="\n" , sep="")







