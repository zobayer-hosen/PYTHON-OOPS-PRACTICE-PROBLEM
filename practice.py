#Develop a class calculator
class Calculator:
  def add(self,a,b):
    return a+b
  def subtract(self,a,b):
    return a-b
  
calc = Calculator()
print("sum",calc.add(5,3))
print("Different:",calc.subtract(5,3)) 

#another way
class Cla:
  def __init__(self,a,b):
    self.a = a
    self.b = b

  def sub(self):
    return f"sub:{self.a-self.b}"
  def add(self):
    return f"add:{self.a+self.b}"

cl= Cla(8,3)
print(cl.sub())
print(cl.add())    
  