# 1. ABC (Abstract Base Class) must be imported to define an abstract class.
# 2. You must write at least one @abstractmethod in the abstract class to make it truly abstract.
# 3. Every abstract method must be overridden in the subclass.
# 4. Regular (non-abstract) methods in the abstract class are optional to override in the subclass.
# 5. You can only create an object of the abstract class if it has NO abstract method inside it.
#    If even one abstract method exists, you CANNOT instantiate (create object of) that class.
# 6. If an abstract method exists in the parent class, then:
#    - There must be a subclass.
#    - And the subclass must override that abstract method.

from abc import ABC,abstractmethod

class ploygone(ABC):
  @abstractmethod
  def areas(self):
    pass

class Rectangle(ploygone):
  def __init__(self,width,height):
    self.width = width
    self.height= height

  def areas(self):
    return f"the total area is {self.width * self.height}"

class Triangle(ploygone):
  def __init__(self,base,width):
    self.base = base
    self.width = width
  def areas(self):
    return f"the total area is {int(0.6*self.base*self.width)}"
  
rec = Rectangle(6,7)
tri = Triangle(8,9)
print(rec.areas())
print(tri.areas())  
      
    

    
      



