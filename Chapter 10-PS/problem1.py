class Programmer:
    company="Microsoft"
    def __init__(self,name, salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=Programmer("Dibbo", 13000000,23443)
print(p.name,p.salary,p.pin,p.company)
r=Programmer("Rohan", 11000000,23445)
print(r.name,r.salary,r.pin,r.company)

        
