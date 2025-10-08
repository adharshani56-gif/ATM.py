class ATM:
    def __init__(self):
        self.balance=1000

    def check_balance(self):
        print(f"your current balance is: ${self.balance}")

    def deposit(self):
        amount=float(input("Enter the amount to deposit:$"))  
        if amount > 0:
            self.balance += amount
            print(f"Deposit successfully your new balance is:${self.balance}")
        else:
            print("invalid amount please enter a positive value") 

    def withdraw(self):
        amount=float(input("Enter the amount to withdraw:$"))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"withdrawal successful. your new balance is:${self.balance}")
        elif amount <=0:
            print("invalid amount .please enter a positive value")
        else:
            print("insufficient funds")

atm = ATM()  
def result():
        while True:
            print("\n ATM Simulator Menu")
            print("1.check balance")
            print("2.deposit funds")
            print("3.withdraw funds")
            print("4.Exit")
            choice=input("Enter your choice(1/2/3/4):")
            if choice=="1":
                print(atm.check_balance())  
            elif choice=="2":
                print(atm.deposit())
            elif choice=="3":
                print(atm.withdraw())
            elif choice=="4":
                print("Exiting the ATM simulator.Thank you!")
                break
            else:
                print("Invalid choice.please choose a valid option.")

if __name__ == "__main__":
    result()                              
