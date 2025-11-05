class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e=Employee()
e.a=45
e.show() 
# ekhane instance attribute 45 jehetu.call korar por 45 print howar kotha.but classmethod use kora hoise dekhe ekhane class attribute 1 print hobe