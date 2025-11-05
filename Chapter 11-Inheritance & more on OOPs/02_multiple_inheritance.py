class Employee: # base or parent class
    company="ITC"
    name="Default name"
    def show(self): # parent 1
        print(f"The name of the employee is {self.name} and the company is {self.company}")

    
class Coder: # parent 2
    language="Python"
    name="R"
    def printLanguages(self):
        print(f"Out of all the languages, here is your language {self.language}") 

        

class Programmer(Employee,Coder): # derived or child class
    company="ITC Infotech"
   
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
a=Employee()
b=Programmer()
b.show()
b.printLanguages()
b.showLanguage()
 