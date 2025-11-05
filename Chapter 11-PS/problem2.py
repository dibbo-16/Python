class Animals:
    pass
class Pets(Animals):
    pass 
class Dog(Pets):
    @staticmethod
    def bark(): #def bark(self):   if i don't use staticmethod
        print("Bow Bow!")
b=Dog()
b.bark()        