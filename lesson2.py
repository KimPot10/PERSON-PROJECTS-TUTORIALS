#input format
#num = input("Enter number: ")


#lahat ng pini-print ni python ay automatic string
#para gawing ibang data type, ito ang syntax

""""
num2 = int(input("Enter Number: "))

print(num2)
"""

#output formatting in python
#format() method

#basic usage
"""""
name = 'Jerson' 
print("I'm {}".format(name))

surname = 'Sagun'
print("My Surname is: {}".format(surname))

wholename = 'Jerson U. Sagun'
print("My whole name is {}".format(surname))

contact = "09602059511"
print("Contact Number: {}".format(contact))
"""

#multiple Values. basta in order lang siya bes
""""
age = 21
city = "Caloocan"
wordCity = "City" 
print("I'm {}. Currently residing at {} {}".format(age, city, wordCity))
"""

#positional arguements. parang array lang ito 
print("{0} {1} {2}".format("Jerson", "U.", "Sagun"))
print("{2} {0} {1}".format("Jerson", "U.", "Sagun"))
print("{0} {1} {2} {3} {4}".format("Jowanie", "Maria", "Kensei", "Avanceña", "Medrano"))
