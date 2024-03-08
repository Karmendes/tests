from calculator import CalculatorAreaCircle,CalculatorAreaSquare,CalculatorAreaTriangle,ICalculator
from faker import Faker

faker = Faker()

class MockAreaCalc():
    def __init__(self):
        pass
    def calculate(self):
        return faker.random_number()

def test_area_circle():
    radius = faker.random_number()
    calc = CalculatorAreaCircle(radius)
    result = calc.calculate()
    assert result == (radius^2) * 3.14

def test_area_square():
    side = faker.random_number()
    calc = CalculatorAreaSquare(side)
    result = calc.calculate()
    assert result == (side * side)

def test_area_triangle():
    base = faker.random_number()
    height = faker.random_number()
    calc = CalculatorAreaTriangle(base,height)
    result = calc.calculate()
    assert result == (base * height)/2

def test_interface_calc_response():
    mock = MockAreaCalc()
    calc = ICalculator(mock)
    result = calc.calculate() 
    assert result is not None
def test_interface_calc_type():
    mock = MockAreaCalc()
    calc = ICalculator(mock)
    result = calc.calculate() 
    assert isinstance(result, (float, int))