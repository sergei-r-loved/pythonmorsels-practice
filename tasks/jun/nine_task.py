# Your bank account should accept an optional balance argument (defaulting to 0), have a balance attribute, and have deposit, withdraw, and transfer methods:

class BankAccount():

    accounts = []
    numbers = {}

    def __init__(self, balance = 0) -> None:
        if balance < 0:
            raise ValueError(f"Cannot open account with {balance} balance")
        self._balance = balance
        
        for number in range(1, 1001):
            if number not in self.numbers.values():  
               BankAccount.accounts.append(self)
               BankAccount.numbers[self] = number
               break
            continue

    @property
    def balance(self):
        return self._balance
    
    @property
    def number(self):
        return self.numbers[self]
    
    def deposit(self, money):
        if money < 0:
            raise ValueError(f"Cannot deposit {money}")
        self._balance = self.balance + money
    
    def withdraw(self, money):
        if money < 0:
            raise ValueError(f"Can't withdraw {money}")
        elif money > self._balance:
            raise ValueError(f" Can't withdraw {money} with {self._balance} balance")
        self._balance = self.balance - money

    def transfer(self, account_number, money):
        if money < 0:
            raise ValueError(f"Can't transfer {money}")
        if money > self._balance:
            raise ValueError(f"Can't withdraw {money} with {self._balance} balance")
        self._balance = self.balance - money
        account_number.deposit(money)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(balance={self._balance})"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(balance={self._balance})"

# a1 = BankAccount()
# print(a1.balance)

# a1.deposit(10)
# print(a1.balance)

# a2 = BankAccount(balance=20)
# a2.withdraw(15)
# print(a2.balance)

# a1.transfer(a2, 3)

# print(a1)
# print(a2)

# a3 = BankAccount(balance=-10)
print(BankAccount.accounts)
a1 = BankAccount(100)
a2 = BankAccount()
print(a1.accounts)
print(a2.number)
a3 = BankAccount(50)
print(a3.accounts)
print(a3.number)