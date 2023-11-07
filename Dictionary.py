thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year":2012
}
print(thisdict)
print(len(thisdict))

#dict constructor
thisdict=dict(name="abc", country="india")
print(thisdict)

#access items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year":2012
}
print(thisdict["model"])
x=thisdict.keys()
print(x)
thisdict["color"]="white"
print(x)

y=thisdict.values()
print(y)
thisdict["color"]="red"
print(y)

z=thisdict.items()
print(z)
thisdict["year"]=2023
print(z)
thisdict["country"]="india"
print(z)

#change items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year":2016})
print(thisdict)
thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)
del thisdict


#copying dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
r=mydict.get("model")
print(r)

#nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child1"]["name"])