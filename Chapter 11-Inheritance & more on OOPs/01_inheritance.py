class Employee: # base or parent class
    company="ITC"
    name="Default name"
    language="Python"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")


class Programmer(Employee): # derived or child class
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a=Employee()
b=Programmer()

print(a.company, b.company)        
