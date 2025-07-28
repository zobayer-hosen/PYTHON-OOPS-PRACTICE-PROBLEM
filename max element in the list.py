class MaxFinder:
  def __init__(self,num):
    self.num = num
  
  def max_number(self):
    if not self.num:
      return "List is empty"
    return max(self.num)
numbers = MaxFinder([2,9,1,6,2,0])
print(numbers.max_number())
numbers1 = MaxFinder([])
print(numbers1.max_number())  
  