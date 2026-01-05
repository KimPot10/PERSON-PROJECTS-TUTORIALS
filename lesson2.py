#input format
#num = input("Enter number: ")


#lahat ng pini-print ni python ay automatic string
#para gawing ibang data type, ito ang syntax

""""
num2 = int(input("Enter Number: "))
#nasa labas ang data type
print(num2)
"""

#output formatting in python
#format() method

#basic usage

name = 'Jerson' 
print("I'm {}".format(name))

nickname = "Kim"
print("My nickname is: {}".format(nickname))

surname = 'Sagun'
print("My Surname is: {}".format(surname))

wholename = 'Jerson U. Sagun'
print("My whole name is {}".format(surname))

contact = "09602059511"
print("Contact Number: {}".format(contact))


#multiple Values. basta in order lang siya bes
""""
age = 21
city = "Caloocan"
wordCity = "City" 
print("I'm {}. Currently residing at {} {}".format(age, city, wordCity))
"""

#positional arguements. parang array lang ito 
""""
print("{0} {1} {2}".format("Jerson", "U.", "Sagun"))
print("{2} {0} {1}".format("Jerson", "U.", "Sagun"))
print("{0} {1} {2} {3} {4}".format("Jowanie", "Maria", "Kensei", "Avanceña", "Medrano"))
"""

#Named Arguements
"""
print("Name: {name}, Age: {age}, Address: {address}".format(name = "Kim", age = 21, address =  "Senate Village"))

print("{:^50}".format("Dito yung word?"))

print("{:>20}".format("Hello, World!"))
"""
#types of Naming variables

"""""
 3 MULTI WORDS VARIABLE NAMES
*  Camel Case: myVariableName = "John"
*  Pascal Case: MyVariableName = "John"
*  Snake Case: my_variable_name = "John"
CASE- Sensitive
 Variable names are case-sensitive.
Example
This will create two variables:
а = 4
A = 'Sally'
#A will not overwrite a

INDENTATION 
* In Python, Indentation is used to define blocks of code. It tells the Python interpreter that a group 
of statements belongs to a specific block. All statements with the same level of indentation are considered part of the same block. 
Indentation is achieved using whitespace (spaces or tabs) at the beginning of each line. The most common convention is to use 4 spaces or a 
tab, per level of indentation.
"""


#Variables 
"""
camelCaseVariable = "thisIsCamelCase"
PascalCaseVariable = "ThisIsPascalCase"
snake_case_variable = "this_is_snake_case"

print(camelCaseVariable)
"""