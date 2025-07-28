class Student:
  def __init__(self,name ,marks):
    self.name = name
    self.marks = marks\

  def Total_marks(self):
    return sum(self.marks)
  def average_marlk(self):
    average = self.Total_marks()/len(self.marks)
    return average

  def Student_markshit(self):
    print(f"the student name is :{self.name}")
    print(f"the total number is each subject: {self.Total_marks()}")
    print(f"the average mark is each subject :{self.average_marlk()}") 

st1= Student("zobayer",[80,90,78,67])
st1.Student_markshit()