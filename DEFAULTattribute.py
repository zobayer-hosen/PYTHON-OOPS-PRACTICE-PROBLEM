class Rectangle:
  def __init__(self,length=1,width=1):
    self.length = length 
    self.width = width 
  
  def sef_dimension(self,length,width):
    self.length = length
    self.width = width

  def area(self):
    return f"{self.length*self.width}"
rec = Rectangle()
print("Default area is:",rec.area())
rec.sef_dimension(5,6)
print("Update area:",rec.area())  

    