print("Hello")
print('Hello')
#Strings are arrays
a = "Hello, World!"
print(a[1])
#looping
for x in "banana":
    print(x)

#Functions
x="Hello world!"
print(len(x))
print("world" in x)
print("hello" not in x)
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[4:])
print(b[-6:-3]) #negative indexing
print(b.upper())
print(b.lower())
s="  Hello   "
print(s.strip())
print(s.replace("H","L"))
print(b.split(","))

#String methods

r="Python is easy!"
print(r.capitalize())
print(r.casefold())
print(r.center(100))
print(r.count("Python"))
print(r.endswith("!"))
print(r.find("is"))
txt = "My name is Ståle"
x = txt.encode()
print(x)

txt1="For only {price:.2f}"
print(txt1.format(price=50))

list=["red","green","blue"]
x="!".join(list)
print(x)
#When using a dictionary as an iterable, the returned values are the keys, not the values.

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

