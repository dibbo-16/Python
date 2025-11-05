class Employee:
    
    language="Python" # this is a class attribute
    salary=130000
    
    def getInfo(self):
        print(f"This language is {self.language}. The salary is {self.salary}")

    @staticmethod # by add this method, we don't need to add self. and we are not going to access any instance attribute
    def greet():
        print("Good morning")

dibbo = Employee()
dibbo.language="C++" # this is an object attribute
print(dibbo.language) 

dibbo.getInfo() # same
Employee.getInfo(dibbo) # same
dibbo.greet()