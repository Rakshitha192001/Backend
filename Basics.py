#while loop
i = 1
while i < 6:
  print(i)
  i += 1

i=2
while i<6:
  print(i)
  if i==4:
    break
  i=i+1

#for loops
mylist=[1,2,3,4]
for x in mylist:
  print(x)

#Functions 

def myfunc():
  print("hello")
myfunc()

#passinf arguments
def myfunc(name):
  print(name)
myfunc("abcs")

#args
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
#kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

#Lambda functions-it is a small anonymous function, it can take any number of arguments but can have only one expression
#Syntax: lambda arguments:expression

x=lambda a:a+7
print(x(4))
y=lambda a,b,c:a*b*c
print(y(1,2,3))

#with ifelse
x=lambda a,b: "hi" if(a>b) else "hello"
print(x(2,4))

#second largest
List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
sortList = lambda x: (sorted(i) for i in x)
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)
print(res)

#filter,map,reduce
from functools import reduce
li=[1,3,4,5,6,7,9,3,4]
x=list(filter (lambda x:(x%2==0) ,li ))
print(x)
y=list(filter(lambda x:(x%2!=0),li))
print(y)
z=list(map(lambda x:x*2,li))
print(z)
sum=reduce(lambda x,y:x+y,li)
print(sum)

username=input("enter username")
print("Username is" +username )