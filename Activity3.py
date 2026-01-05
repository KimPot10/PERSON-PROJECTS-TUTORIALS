print("=====Activity 3=====")

#Input
firstNum = input("Enter First Number: ")
if not firstNum.isnumeric():
    print("Exit.")
    exit()

secondNum = input("Enter Second Number: ")
if not secondNum.isnumeric():
    print("Exit.")
    exit()
    
sepa = str(input("Enter Separator (special characters only): "))
if not sepa.isalnum() and sepa != "" and not sepa.isspace():
    pass
else:
    print("Invalid input! Exiting program.")
    exit()

print((firstNum) * 6, int(secondNum) * 4, sep="&")
