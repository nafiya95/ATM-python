class INDIAN_ATM:
    def __init__(self, account_no, account_holder):
        self.account_no = account_no
        self.account_holder = account_holder
        self.balance = 1000

    def display(self):
        print(f"account_no: {self.account_no}")
        print(f"account_holder: {self.account_holder}")
        print(f"current balance: {self.balance}")

    def balance_enquiry(self):
        print(f"your current balance is: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"deposit amount: {amount}")
        print(f"current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"withdrawal amount: {amount}")
            print(f"current balance: {self.balance}")
        else:
            print("insufficient balance")

    def exit(self):
        print("thank you for using the ATM!")

obj1 = INDIAN_ATM("1234xxxxxxxx", "anu")

choice = int(input("1.display\n2.balance_enquiry\n3.withdraw\n4.exit\nEnter choice: "))
print(choice)

if choice == 1:
    obj1.display()
    print("-----------------")
elif choice == 2:
    obj1.balance_enquiry()
    print("")
elif choice == 3:
    amt = float(input("enter the amount to withdraw: "))
    obj1.withdraw(amt)
    print("")
elif choice == 4:
    obj1.exit()
    print("")
    print("bye")
