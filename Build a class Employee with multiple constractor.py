class Employee:
  def __init__(self,name,id = None,department= None):
    self.name= name 
    self.id = id
    self.department = department
  

  def employee_details(self):
    print("employee name :",self.name)
    if self.id:
      print("employee ID:",self.id)
    if self.department:
      print("employee department:",self.department)

emp = Employee("zobayer")
emp.employee_details()
emp1 = Employee("zobayer",23,"worker")
emp1.employee_details()