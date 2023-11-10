class mynumber:
    def __init__(self,value):
        self.value=value
    
    def printvalue(self):
        print(self.value)
        
p=mynumber(2)
p.printvalue()

class car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    
    def show(self):
        print("Model is" +self.name)
        print("color is "+self.color)
        
s=car("defeefe","red")
s.show()
s1=car("audi","sedw")
s1.show()


#Single level Inheritance
class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def display(self):
        print("Name is {}" .format(self.name))
        print("Id is {}" .format(self.id))
        
class Employee(Person):
    def __init__(self, name, id,salary,post):
        self.salary=salary
        self.post=post
        
        Person.__init__(self,name, id)
        
        
    def display(self):
        print("Name is {}" .format(self.name))
        print("Id is {}" .format(self.id))
        print("Salary is {}" .format(self.salary))
        print("Post is {}" .format(self.post))
        
p=Employee("fdrdrf","wwwed",1233,"wae")
p=Employee("rftte",132,2333,234)
p.display()

#Multiple inheritance
class Base1:
    def __init__(self):
        print("hello")

class Base2:
    def __init__(self):
        print("hii")
        
class Base3(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        
    def display(self):
        print("displayed")    
ob=Base3()
ob.display()

#Encapsulation
#protected members
class Base:
    def __init__(self):
        self._a=3 #protected member
    
class Derived(Base):
    def __init__(self):
        
        Base.__init__(self)
        print("accessing " ,self._a)

obj1=Base()
obj2=Derived()
print(obj2._a)        
#Private members
class Base:
    def __init__(self):
        self._a=4
        self.__b=5 #private member
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("a is " , self._a)
        # print("b is " ,self.__b)
obj1=Derived()

#Data abstraction
class Sample:
    __hiddenvar=0
    
    def add(self,a):
        self.__hiddenvar+=a
        print(self.__hiddenvar)
        
res=Sample()
res.add(3)
# print(__hiddenvar)

# A Python program to demonstrate that hidden 
# members can be accessed outside a class 
class MyClass: 

	# Hidden member of MyClass 
	__hiddenVariable = 10

# Driver code 
myObject = MyClass()	 
print(myObject._MyClass__hiddenVariable) 

class Test: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

	def __repr__(self): 
		return "Test a:%s b:%s" % (self.a, self.b) 

	# def __str__(self): 
	# 	return "From str method of Test: a is %s," \ 
    #         "b is %s" % (self.a, self.b) 

# Driver Code		 
t = Test(1234, 5678) 
# print(t) # This calls __str__() 
print([t]) # This calls __repr__() 

#polymorphism
class Demo:
    def add(self,a,b):
        self.a=a
        self.b=b
        print(a+b)
        
res=Demo()
res.add(3,4)
res.add(6,7)

class Bird:
    def intro(self):
	    print("There are many types of birds.")
    #def flight(self):
	    #print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):
	    print("Sparrows can fly.")
	
class ostrich(Bird):
    def flight(self):
	    print("Ostriches cannot fly.")
	
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
# obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

