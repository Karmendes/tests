from flask import Flask, request, jsonify
from flask import Blueprint

from src.unitarios.calculator import ICalculator,CalculatorAreaCircle,CalculatorAreaSquare,CalculatorAreaTriangle

routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET"])
def liveness():
    return jsonify('I am a live!!')

@routes.route("/triangle", methods=["POST"])
def calc_triangle():
    dados = request.get_json()
    base = dados['base']
    height = dados['height']
    calc = ICalculator(CalculatorAreaTriangle(base,height))
    result = calc.calculate()
    return jsonify(f'The Area of Triangle is {result}')
@routes.route("/square", methods=["POST"])
def calc_square():
    dados = request.get_json()
    side = dados['side']
    calc = ICalculator(CalculatorAreaSquare(side))
    result = calc.calculate()
    return jsonify(f'The Area of Square is {result}')
@routes.route("/circle", methods=["POST"])
def calc_circle():
    dados = request.get_json()
    radius = dados['radius']
    calc = ICalculator(CalculatorAreaCircle(radius))
    result = calc.calculate()
    return jsonify(f'The Area of Circle is {result}')

