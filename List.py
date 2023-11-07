thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
print(type(thislist))

#list constructor
thislist=list(["apple","orange"])
print(thislist)

#accessing the list
print(thislist[1])
print(thislist[-1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#changing the list
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#add items
thislist.insert(2,"orange")
print(thislist)
thislist.append("kiwi")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove items
thislist1=["red","green","blue","white"]
thislist1.remove("red")
print(thislist1)
thislist1.pop(0)
print(thislist1)
del thislist1[1]
print(thislist1)
thislist1.clear()
print(thislist1)

#Looping through a list
thislist1=["red","green","blue","white"]
for x in thislist1:
    print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

#sort
fruits = ["apple", "banana", "mango","cherry", "kiwi"]
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
fruits.reverse()
print(fruits)

#copy
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
mylist1=list(mylist)
print(mylist1)

#join
alpha=["a","b","c"]
num=[1,2,3]
print(alpha+num)
for x in num:
    alpha.append(x)
print(alpha)
alpha.extend(num)
print(alpha)

#List methods
