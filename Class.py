#All classes have a function called __init__(), which is always executed when the class is being initiated.

class myclass:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
p=myclass("sdghd",45)
print(p.name)
print(p.age)

class myclass:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    def __str__(self) -> str:
        return f"{self.name}"
p=myclass("sdghd",45)
print(p.name)
print(p.age)
print(p)

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()
