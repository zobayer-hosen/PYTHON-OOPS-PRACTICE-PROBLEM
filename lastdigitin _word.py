class NumberWord:
  def finding_number(self,numbers):
    reminder = numbers%10
    world= ["gero","One","two","three","four","Five","six","seven","eight","nine"]
    return world[reminder]

num = NumberWord()
print(num.finding_number(123))
