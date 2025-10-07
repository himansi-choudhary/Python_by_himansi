# change the self-parameter inside a class to something else (say “harry”). 
# Try changing self to “slf” or “harry” and see the effects.
# ANSWER :- NO EFFECT (but not a good practice to write anything ekse insted of self)
# Code :- with Q5 solution


# see at self positions
from random import randint

class train():
    trainNo = 0

    def __init__(slf, trainNo):  # write slf
        slf.trainNo = trainNo

    def book(harry, fro, to):  # write harry
        print(f"succesfully Booked ticket in train {harry.trainNo} from {fro} to {to}")

    def getstatus(himansi):  # write himansi
        print(f"Train {himansi.trainNo} is running on time")

    def getfare(etc, fro, to):   # Write etc
        print(f"Total fare of train {etc.trainNo} from {fro} to {to} is {randint(255, 300)}")


ticket = train(1234)
ticket.book("Pune", "Pali,Rj")
ticket.getstatus()
ticket.getfare("Pune", "Pali,Rj")

