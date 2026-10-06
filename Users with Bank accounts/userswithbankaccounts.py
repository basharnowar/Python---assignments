class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
       if self.balance >= amount:
          self.balance -= amount
       else:
           print("Insufficient funds: Charging a $5 fee")
           self.balance -= 5
       return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self


    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.01, balance=0)       

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self

guido = User("Guido", "Guido@gmail.com")
guido.make_deposit(100).make_deposit(100).make_withdraw(30)
guido.display_user_balance()

Emil = User("Emil", "Emil@gmail.com")
Emil.make_deposit(4000).make_deposit(2000).make_withdraw(1000)
Emil.display_user_balance()