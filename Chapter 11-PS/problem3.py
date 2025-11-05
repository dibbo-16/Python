class Employee:
    salary= 2400
    increment= 250

    @property # eta likhle jekono kichu return kora possible 
    def salaryAfterIncrement(self):
        return (self.salary + self.salary*(self.increment/100))
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment=((salary/self.salary)-1)*100 #salary= new salary and self.salary= old salary

e= Employee() 
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement=8400

print(e.increment)