class Employee: 
    a=6
class Programmer(Employee):
    b=3    

class Manager(Programmer):
    c=7

d= Employee()
print(d.a)
# print(d.b) # will show error

e=Programmer()
print(e.a)
print(e.b)
# print(e.c) # will show error

f=Manager()
print(f.a)
print(f.b)
print(f.c)


   