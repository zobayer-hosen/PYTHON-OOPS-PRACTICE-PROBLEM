#__str__() object representation return 

class Person:
  def __init__(self,first_name,last_name):
    self.first_name = first_name
    self.last_name = last_name

  def __str__(self):
    return f"the first name is:{self.first_name}, and the last name is: {self.last_name}"
s1 = Person("zobayer","Hosen")
print(s1)  
  