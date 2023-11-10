from bs4 import BeautifulSoup


#opening dict.xml in read mode
with open("dict.xml","r") as file:
    data=file.read()
#     print(data)

#passing the data in beautifulsoup parser and storing it    
bs_data=BeautifulSoup(data,"xml")
print(bs_data)

#Finding all instances of a tag unique
b_unique=bs_data.find_all('unique')
print(b_unique)

#Finding first instance of a tag
b_find=bs_data.find('child',{"name":'Texas'})
print(b_find)

#Extracting the data stored in a particular tag
value=b_find.get("test")
print(value)

for tag in bs_data.find_all('child',{"name":"Frank"}):
    tag['child']="WHAT"
    
print(bs_data.prettify())