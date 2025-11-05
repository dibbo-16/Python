from random import randint
class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
    def book(self,fro,to):
        print(f"Ticket is booked in trainNo {self.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"Train no {self.trainNo} is running on time")
    def getFare(self,fro,to): # from is a reserved keyword in python like def.so we can not use from.that's why we use fro
        print(f"Ticket fare in trainNo {self.trainNo} from {fro} to {to} is {randint(222,5555)}")
t=Train(12543)
t.book("Dhaka","Rajshahi")
t.getStatus()
t.getFare("Dhaka","Rajshahi")


