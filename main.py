from account import Account

class CheckingAccount(Account):
    def __str__(self):
        return f"{self.owner}'s Checking Account. Balance = {self.balance}"
    # Your code for Step 1 goes here

class SavingsAccount(Account):
    def __init__(self, owner, interest_rate):
        self.interest_rate = interest_rate
        super().__init__(owner)

    def __str__(self):
        return f"{self.owner}'s Savings Account. Balance = {self.balance}."
    # Your code for Step 2 goes here

    def accrue_interest(self):
        self.balance *= (1+ self.interest_rate/100)

    def withdraw(self, balance):
        return super().withdraw(balance + 5)

class LockedAccount(SavingsAccount):
    def __str__(self):
        return f"{self.owner}'s Locked Account. Balance = {self.balance}"

    def withdraw(self, balance):
        return False

    def transfer(self, balance, recipient):
        return False

if __name__ == '__main__':
    print("You can manually test your code here")
