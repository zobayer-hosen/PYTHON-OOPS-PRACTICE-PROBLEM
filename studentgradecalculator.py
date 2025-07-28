class Student:
  def __init__(self,name,Marks):
    self.name = name
    self.Marks = Marks

  def average(self):
    return sum(self.Marks)/len(self.Marks)
  #this method is for grade
  def __str__(self):
    average = self.average()

    if average >= 90:
      return 'A+'
    elif average >=80:
      return 'A'
    elif average >=70:
      return 'B'
    else:
      return 'F'
student = Student("zobayer",[80,90,70])
print(student.name,f" your grade is {student}")   