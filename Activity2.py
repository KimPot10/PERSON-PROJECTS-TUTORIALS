print("=====Activity 2=====")

#Input
#Input
word = str(input("Enter a Word: "))
if not word.isalpha():
    print("Invalid input! Exiting program.")
    exit()

num = str(input("Enter a Number: "))
if not num.isnumeric():
    print("Invalid input! Exiting program.")
    exit()

num = int(num)
print(word*num, end="\n")

