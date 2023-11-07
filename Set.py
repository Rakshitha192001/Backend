myset={"green","blue","orange"}
print(myset)

myset1={"green","blue","orange",True,1}
print(myset1)
print(len(myset1))

#accessing
myset={"green","blue","orange"}
for x in myset:
    print(x)
print("blue" in myset)

#add items
myset.add("red")
print(myset)
myset.update(myset1)
print(myset)

#remove items
thisset = {"apple", "banana", "cherry","mango","watermelon"}
thisset.remove("banana")
print(thisset)
thisset.discard("apple")
print(thisset)
thisset.pop() #removes random item
print(thisset)
thisset.clear()
del thisset

#loops
thisset = {"apple", "banana", "cherry","mango","watermelon"}
for x in thisset:
    print(x)

#Join sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
x.intersection(y)
print(x)
x.symmetric_difference_update(y)
print(x)
x.symmetric_difference(y)
print(x)

#Methods
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
s=x.difference(y)
print(s)
s=x.isdisjoint(y)
print(s)

