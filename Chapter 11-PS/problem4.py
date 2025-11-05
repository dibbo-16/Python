class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,c2):
        return Complex(self.r+ c2.r, self.i+ c2.i) 
    
    def __mul__(self, c2):   
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)

    def __str__(self): # from complex object to make it readable as a string and complex number. without it, value will be print as a complex object
        return f"{self.r} + {self.i}i"   
c1= Complex(1,3)
c3= Complex(4,5)   
print(c1+c3) 
print(c1*c3)