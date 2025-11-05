class Employee:
    
    language="Python" 
    salary=130000

    def __init__(self, name, salary, language): # dunder method(starting and ending ah always double underscore sign thake) which is automatically called by object and here it is a constructor example
        self.name=name # self.name hocche class er bhitor variable. r equal er pore j name eta user er through teh j value newa hobe shetar parameter
        self.salary=salary
        self.language= language
        print("I am creating an object")
       

    def getInfo(self):
        print(f"This language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet(sel):
        print("Good morning")

dibbo = Employee("Dibbo", 1400000, "C++")
# dibbo.name="Dibbo"
print(dibbo.name,dibbo.language,dibbo.salary) 
rohan=Employee("Rohan", 1500000, "C#") 
print(rohan.name,rohan.language,rohan.salary) 
dibbo.getInfo()
