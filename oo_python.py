class ATM:
    def __init__(self, name, pin, balance, name2= None, pin2 = None):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.name2 = name2
        self.pin2 = pin2
    def printBalance(self):
        while (self.name != self.name2):
            self.name2 = input("Enter your name: ")
            if self.name != self.name2:
                print("Incorrect Name!")
        while (self.pin != self.pin2):
            self.pin2 = int(input("Enter your pin: "))
            if self.pin != self.pin2:
                print("Incorrect pin!")
        print(self.balance)
        
dic = {
    "name": "Greg",
    "pin": 1234,
    "balance": 1000
}       
atm = ATM(dic["name"], dic["pin"], dic["balance"])
atm.printBalance()