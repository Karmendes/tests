
from abc import ABC,abstractmethod

class CalculatorMaster(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def calculate(self):
        pass
    

class CalculatorAreaTriangle(CalculatorMaster):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def calculate(self):
        return int((self.base * self.height) / 2)

class CalculatorAreaSquare(CalculatorMaster):
    def __init__(self,side):
        self.side = side
    def calculate(self):
        return self.side * self.side

class CalculatorAreaCircle(CalculatorMaster):
    def __init__(self,radius):
        self.radius = radius
        self.pi = 3.14
    def calculate(self):
        return self.pi * (self.radius * self.radius)

class ICalculator:
    def __init__(self,algorith):
        self.calculator = algorith
    def calculate(self):
        return self.calculator.calculate()