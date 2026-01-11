x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")
if operator == '+':
    result = x + y
    print("Result:", result)
elif operator == '-':
    result = x - y
    print("Result:", result)
elif operator == '*':
    result = x * y
    print("Result:", result)
elif operator == '/':
    if y != 0:
        result = x / y
        print("Result:", result)
    else:
        print("Error: Division by zero")