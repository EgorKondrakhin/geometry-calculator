import math 
class Circle:
  def_init_(self,radius: float):
    if radius <= 0:
      raise ValueError("радиус должен быть положительным")
    self.radius = radius
  def area(self) -> float:
return math.pi * (self.radius **2)
  
