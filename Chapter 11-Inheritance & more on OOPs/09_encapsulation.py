# Encapsulation is the concept of binding data (variables) and methods (functions) into a single unit (class) and restricting direct access to some data to ensure controlled modification.
# In Python, this is often done using private/protected attributes (_var, __var).

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number   # private attribute
        self.__balance = balance                 # private attribute

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def deposit(self, amount):
        if(amount > 0):
            self.__balance += amount
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if(0 < amount <= self.__balance):
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount")
  
# Usage
acc = BankAccount("12345", 5000)
# print(acc.__balance) # it is a private variable.so direct access is not allowed.we have to access it through method in class.like here get_balance().method name can be anything
print(acc.get_balance())   # 5000
acc.deposit(2000)
print(acc.get_balance())   # 7000
acc.withdraw(3000)
print(acc.get_balance())   # 4000

#Here __balance and __account_number are encapsulated (hidden). We can only access them via methods.
# __rk(duble underscore diye variable start korle eta k private varibale bole)