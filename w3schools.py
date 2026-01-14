'''
Docstring for w3schools
#   Many values to multiple threads

x, y, z = "banana", "mango", "milktea"
# para siyang array in a way. pero list siya... array nga? haha

print(x)
print(y)
print(z)


input("enter something: ")
#git cant focus part 2
'''

#Assigning Multiple Values
#unpack a collection.
#basically para siyang array pero as alist? haha
''''
fruits = ["pineanpple", "strawberry", "banana"]
a, b, c = fruits
'''
'''
print(a)
print(b)
print(c)
'''
#other method ay pwede rin isang line

''' print(a, b, c) '''

#ooooo tangina isang line lang din sila mapiprint
#aaaaa kasi potangina yung isang print ng python automatic na new line na haha bwisit amp


#global variables

#Variables that are created outside of a function (as in all of the examples in the previous pages)
#  are known as global variables. may tawag dito eh... basta global variables nga
#Global variables can be used by everyone, both inside of functions and outside.
'''
globalVariables = "awesome"

def globalVpractice():
    print("Python is " + globalVariables)

globalVpractice()


x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()

print("Python is " + x) 

'''

#pwede siya gawing global if ginawa siya locally
#locally meaning yung variable ginawa inside only ng isang function



def example_of_local_going_global():
    global x 
    x = "fantastic"
    print("Python is " + x)
example_of_local_going_global()

print("Python is " + x) 


#Data types in python
'''
x = "Hello World"	str	
x = 20	            int	
x = 20.5	        float	
x = 1j	            complex	
x = ["apple", "banana", "cherry"]	list	lists are mutable, meaning their elements can be changed, added, or removed after creation
x = ("apple", "banana", "cherry")	tuple	tuples are immutable, meaning their contents cannot be modified once defined
x = range(6)	                    range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	                                    bool	
x = b"Hello"	                                bytes	
x = bytearray(5)	                            bytearray	
x = memoryview(bytes(5))	                    memoryview	
x = None	                                    NoneType
'''

#learning loops
