class Number:
    def __init__(self,n): #constructor
        self.n= n

    def __add__(self,num): # operator overloading
         return self.n + num.n
    
a = Number(1)    
b = Number(3) 
print(a + b)
