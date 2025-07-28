class Bank_account:
  def __init__(self,balance):
    self.__balance = balance
  def deposite(self,amount):
     self.__balance += amount
     print(f'the total balance is {self.__balance}')
  def Withdraw(self,amount):
    
    if amount>self.__balance:
      print(f"the amount not sufficient ")
    else:
      self.__balance -= amount
      print(f"your withdraw amount is {amount} remaning amount is {self.__balance}")
b = Bank_account(500)
b.deposite(200)      
b.Withdraw(300)
b.Withdraw(100)
