import sys
import mariadb
import random


class UserHandler:
    def __init__(self, FirstName, LastName, CardNumber):
        self.FirstName = FirstName
        self.Lastname = LastName
        self.CardNumber = CardNumber


try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="localhost",
        port=3306,
        database="atm"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
print(conn)

cur = conn.cursor()


def generateCardNumber():
    cardNum = "5674"
    for i in range(13):
        cardNum += str((random.randrange(0,9)))

    return str(cardNum)


def registerToDB(FirstName, LastName, CardNumber, Pin):
    try:
       cur.execute("INSERT INTO accounts (`FirstName`, `LastName`, `CardNumber`, `pinNumber`) VALUES (?, ?, ?, ?)", (FirstName, LastName, CardNumber, Pin))
    except mariadb.Error as e: 
        print(f"Error: {e}")
    conn.commit()
    print(f"{FirstName, LastName, CardNumber, Pin} succesfully insterted into DB")

def pin():
    pinNum = ""
    correct = False
    while not correct:
        pinNum = input("PIN(4 characters): ")
        if len(pinNum) == 4:
            correct = True
        elif len(pinNum) > 4:
            print("PIN cannot be more than 4 characters!")
        else:
            print("PIN number cannot be less than 4 characters!")
    return pinNum

def registerMain():
    FName = str(input("Your first name: "))
    LName = str(input("Your last name: "))
    pinNum = pin()
    cardNumber = generateCardNumber()
    print(FName, LName, cardNumber, pinNum)
    registerToDB(FName, LName, cardNumber, pinNum)

def loginMain():

    login = UserHandler()
    

registerMain()
