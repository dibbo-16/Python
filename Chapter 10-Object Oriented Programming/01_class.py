class Employee:
    
    language="Python" # this is a class attribute
    salary=130000
# here dibbo is a object and Employee is a class  
dibbo = Employee()
dibbo.name="Dibbo Jyoti" # this is an object attribute
print(dibbo.name, dibbo.language)   

rohan=Employee()
rohan.name="Rohan Sharma"
print(rohan.name,rohan.language,rohan.salary)

# Class is a blueprint to create object
# Here name is a instance/object attribute and language, salary are class attributes as they directly belong to the class
