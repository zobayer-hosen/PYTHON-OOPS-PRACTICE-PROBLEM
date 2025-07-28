class Animal:
  def speeks(self):
    pass
class Dog(Animal):
  def speeks(self):
    print("the Dog sound ")
class Cat(Animal):
  def speeks(self):
    print("the cat sound")

dog = Dog()
dog.speeks()
cat = Cat()
cat.speeks()
