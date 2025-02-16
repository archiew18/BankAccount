class BankAccount:
  def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self,amount):
    self.balance = self.balance + amount
    return self.balance

  def withdraw(self,amount):
    self.balance = self.balance - amount
    return self.balance

  def display_balance(self):
    print(self.balance)

example = BankAccount('bob','smith',123,'debit',0000,100)

example.deposit(100)
example.display_balance()
example.withdraw(150)
example.display_balance()
