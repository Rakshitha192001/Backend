#Logical operators
x=16
y=6
if x>10 and y>10:
    print("and operation")
elif x>10 or y>10:
    print("or operation")
elif not(x>10 and y<10):
    print("not operation")

#Identity operators
x=["red","green","white"]
y=["red","green","white"]
z=x
print (x is z) # returns True because z is the same object as x
print (x is y) # returns False because x is not the same object as y, even if they have the same content
print (x is not y) #true
print (x is not z) #false

#Membership operators
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list
x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list 
