#try-except
a=[1,2,3]
try:
    print(a[0])
    print(a[3])
except:
    print("an error occurred")

#try else
def myfunc(a,b):
    try:
        
        print(a+b)
    except:
        print("error")
    else:
        print("no error")

myfunc(1,4)


#custom exception
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)
    
    