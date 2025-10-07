# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways.
from random import randint

class train():
    trainNo = 0

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"succesfully Booked ticket in train {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train {self.trainNo} is running on time")

    def getfare(self, fro, to):
        print(f"Total fare of train {self.trainNo} from {fro} to {to} is {randint(255, 300)}")


ticket = train(1234)
ticket.book("Pune", "Pali,Rj")
ticket.getstatus()
ticket.getfare("Pune", "Pali,Rj")
