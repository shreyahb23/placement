class Bankaccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    @classmethod
    def set_rate(cls, rate):
        cls.interest_rate = rate
        
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

account1 = Bankaccount("Alice", 1000)
account1.deposit(500)
Bankaccount.set_rate(0.05)
print(Bankaccount.is_valid_amount(-100))