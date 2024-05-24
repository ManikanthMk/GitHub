class account:
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    print(f"Deposited ${amount} into {self.name}'s account. New balance: ${self.balance}")

  def withdraw(self, amount):
    if amount > self.balance:
      print(f"Insufficient funds in {self.name}'s account.")
    else:
      self.balance -= amount
      print(f"Withdrew ${amount} from {self.name}'s account. New balance: ${self.balance}")

  def check_balance(self):
    print(f"{self.name}'s account balance: ${self.balance}")
s1 = account("John", 1000)
print(s1.name)
print(s1.balance)
s1.deposit(500)