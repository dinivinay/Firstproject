class Bank():
    def __init__(self):
        self.closingBalance = 0
    def display(self):
        print("Enter your options: ")
        print("1 for deposit: \n 2 for withdraw: ")
        getOption = input()

        if getOption == "1":
            self.deposit()
        elif getOption == "2":
            self.withdraw()
        elif getOption != "1" or getOption !="2":
            print("You had entered invalid input \n Thanks")
            return
        print("Your closing balance is: ", self.closingBalance)
        print("Enter Y if you want to continue: ")

        a = input()
        if a== "Y" or a == "y":
            self.display()
        else:
            print("Thanks for visiting our bank")
    
    def deposit(self):
        depositAmount = int(input("Enter your deposit amount: "))
        self.closingBalance = self.closingBalance + depositAmount
        return self.closingBalance

    def withdraw(self):
        withdrawAmount = int(input("Enter your Withdrawl amount: "))
        if self.closingBalance >= withdrawAmount:
            self.closingBalance = self.closingBalance - withdrawAmount
            print("Your final balance amount is : ")
        else:
            print("insufficient balance")
            return self.closingBalance
        
bankobj = Bank()
bankobj.display()

            
    