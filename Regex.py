import re
txt = "The rain in Spain"
x=re.findall("in",txt) # function returns a list containing all matches
print(x)

x=re.search("\s",txt) #searches the string for a match
print(x.start())

x=re.split("\s",txt) #returns a list where the string has been split at each match
print(x)

x=re.search("\AThe",txt)
print(x)

txt1="sdfejk345453"
y=re.findall("\d",txt1)
print(y)