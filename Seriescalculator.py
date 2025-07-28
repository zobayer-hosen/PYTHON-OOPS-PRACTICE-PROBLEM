class SeriesCalculator:
  def calculator_sum(self,n,a=1,d=2):
    return n*(2*a+(n-1)*d)//2
  
sc = SeriesCalculator()
a = int(input("Enter the your series number:"))
print("sum fo series :",sc.calculator_sum(a))  