thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

#accessing tuple
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple[3])
print(thistuple[-1])
print(thistuple[1:3])
print(thistuple[-4:-1])
print(thistuple[:4])

#changing
x=("red","green","yellow")
y=list(x)
y[1]="orange"
x=tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
del thistuple


#unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#looping through a tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#joining tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3=tuple1+tuple2
print(tuple3) 
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

#Tuple methods
mytuple=(1,2,4,5,6,7,4,3,6,7)
print(mytuple.count(6))
print(mytuple.index(2))