class TwoDVactor:
    def __init__(self,i,j):
        self.i= i
        self.j= j

    def show(self):
        print(f" The TwoDVactor is {self.i}i + {self.j}j")  

          
class ThreeDVactor(TwoDVactor):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def show(self):
        print(f" The ThreeDVactor is {self.i}i + {self.j}j + {self.k}k")

a=TwoDVactor(1,3)
a.show()
b=ThreeDVactor(1,5,7)
b.show()