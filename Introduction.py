print("hello")

#Python indentation
x=7
if x>5:
    print("x is greater than 5")

#Multi line comments
"""
This is a comment
written in
more than just one line
"""

#Variables- containers for storing values
x=5
y="hello"
#We can also specify the data type-casting
x=int(5)
y=str("hello")
z = float(3) 
print(type(x)) #get the type by using type() function

#Unpacking a collection
fruits=["apple", "mango","papaya"]
a,b,c=fruits
print(a)
print(b)
print(c)

#print function
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#global variables
x=5
def myfunc():
    print(x)

myfunc()

#global keyword-to create global variables inside a function
def myfunc1():
    global z
    z=8
myfunc1()
print(z)

#Python datatypes
x="HELLO" #str
x=5 #int
x=5.6 #float
x=True #bool
x=[1,2,3,4] #list
x=(1,4,5,6,7) #tuple
x={1,5,6} #set
x={"num1":1,"num2":2} #dict
x = range(6) #ouput-range(0, 6)

#Type conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)
"""You cannot convert complex numbers into another number type."""

#Random
import random
print(random.randrange(1,10))