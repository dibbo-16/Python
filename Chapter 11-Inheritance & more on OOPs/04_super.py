class Employee: 
    def __init__(self):
        print("Constructor of Employee")
     
    a=6
class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
     
    b=3    

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
     
    c=7

# d= Employee() # eta sudhu comment out korle constructor of employee print hobe
# print(d.a)
# print(d.b) # will show error

# e=Programmer() # eta sudhu comment out korle constructor of programmer print hobe
# print(e.a)
# print(e.b)
# # print(e.c) # will show error

f=Manager()
# print(f.a)
# print(f.b)
# print(f.c)


   