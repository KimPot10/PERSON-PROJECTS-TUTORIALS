print("=====Activity 2=====")

#Input
#Input
word = input("Enter a Word: ")
if not word.isalpha():
    print("Invalid input! Exiting program.")
    exit()

num = input("Enter a Number: ")
if not num.isnumeric():
    print("Invalid input! Exiting program.")
    exit()

num = int(num)

print(word*num, end="\n")

