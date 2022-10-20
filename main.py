import mariadb
import random
    
conn =  mariadb.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="atm"
)
print(conn)
cur = conn.cursor()

def generateCardNumber():
    cardNumber = "5674"    
    for i in range(13):
        cardNumber += str((random.randrange(0,9)))
    return str(cardNumber)

def registerToDB(FirstName, LastName, CardNumber, Pin):
    try:
       cur.execute("INSERT INTO accounts (`FirstName`, `LastName`, `CardNumber`, `pinNumber`) VALUES (?, ?, ?, ?)", (FirstName, LastName, CardNumber, Pin))
    except mariadb.Error as e: 
        print(f"Error: {e}")
    conn.commit()

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

registerMain()
