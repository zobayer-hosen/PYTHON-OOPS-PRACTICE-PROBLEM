class Bank:
  def __init__(self):
    self.customer ={}

  def create_account(self,account_number,initial_balance=0):
    if account_number in self.customer:
      print("Account number already exits")
    else:
      self.customer[account_number] = initial_balance
      print("Account created successfully")
  def make_deposite(self,account_number,amount):
    if account_number in self.customer:
      self.customer[account_number] += amount
      print("Deposit successful")
    else:
      print("Account number does not exits")


  def make_withdrawal(self,account_number, amount):
    if account_number in self.customer:
      if self.customer[account_number] >= amount:
        self.customer[account_number] -= amount
        print("Withdrawal successful")
      else:
        print("Insufficient funds")

    else:
      print("Account numbers does not exits")  


  def check_balance(self,account_number):
    if account_number in self.customer:
      balance = self.customer[account_number]
      print(f"Account balance is: {balance}")
    else:
      print("Account number does not exist")

bank = Bank()

acno1 = "sb-123"
damt1 = 10000

print("New a/c No :",acno1,"Deposit amount:",damt1)
bank.create_account(acno1,damt1)

wamt1 = 600
bank.make_deposite(acno1,wamt1)

bank.make_withdrawal(acno1,300)
bank.check_balance(acno1)



      
    