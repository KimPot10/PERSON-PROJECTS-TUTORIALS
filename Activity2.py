print("=====Activity 2=====")

#Input
#Input
word = str(input("Enter a Word: "))
if not word.isalpha():
    print("Exit")
    exit()

num = str(input("Enter a Number: "))
if not num.isnumeric():
    print("Exit.")
    exit()

num = int(num)
print(word*num, end="\n")

