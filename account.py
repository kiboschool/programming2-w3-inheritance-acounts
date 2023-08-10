class Account():

    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def __str__(self):
        return f"This is the __str__ method of the Account class. We should not see this message. Define __str__ in the subclasses"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance or amount < 0:
            return False
        else:
            self.balance -= amount
            return True

    def transfer(self, amount, recipient):
        if self.withdraw(amount):
            recipient.deposit(amount)
            return True
        else:
            return False