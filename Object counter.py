class Objectcounter:
  count =0
  def __init__(self):
    Objectcounter.count +=1

  @staticmethod
  def counter_method():
    return f"the total object is:{Objectcounter.count}"


obj = Objectcounter()
obj1 = Objectcounter()
print(Objectcounter.counter_method())