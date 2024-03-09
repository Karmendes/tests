from werkzeug.wrappers import Request,Response
import pytest
from middlewares import ValidateRouteCircle,ValidateRouteSquare,ValidateRouteTriangle,Middleware


def test_validate_route_circle():
    data = {'radius':4}
    valid = ValidateRouteCircle(data)
    result = valid.validate()
    assert result == data

def test_validate_route_circle_key_wrong():
    data = {'radiu':4}
    valid = ValidateRouteCircle(data)
    result = valid.validate()
    assert isinstance(result, Response)  # Assert that the return value is a Response object
    assert result.status_code == 401  # Assert the status code

def test_validate_route_circle_value_type():
    data = {'radius':'43'}
    valid = ValidateRouteCircle(data)
    result = valid.validate()
    assert isinstance(result, Response)  # Assert that the return value is a Response object
    assert result.status_code == 401  # Assert the status code

def test_validate_route_square():
    data = {'side':4}
    valid = ValidateRouteSquare(data)
    result = valid.validate()
    assert result == data

def test_validate_route_square_key_wrong():
    data = {'sidee':4}
    valid = ValidateRouteSquare(data)
    result = valid.validate()
    assert isinstance(result, Response)  # Assert that the return value is a Response object
    assert result.status_code == 401  # Assert the status code

def test_validate_route_square_value_type():
    data = {'side':'43'}
    valid = ValidateRouteSquare(data)
    result = valid.validate()
    assert isinstance(result, Response)  # Assert that the return value is a Response object
    assert result.status_code == 401  # Assert the status code

def test_validate_route_triangle():
    data = {'base':4,'height':4}
    valid = ValidateRouteTriangle(data)
    result = valid.validate()
    assert result == data

def test_validate_route_triangle_key_wrong():
    data = {'bas':4,'height':4}
    valid = ValidateRouteTriangle(data)
    result = valid.validate()
    assert isinstance(result, Response)  # Assert that the return value is a Response object
    assert result.status_code == 401  # Assert the status code

def test_validate_route_triangle_value_type():
    data = {'base':'43','height':32}
    valid = ValidateRouteTriangle(data)
    result = valid.validate()
    assert isinstance(result, Response)  # Assert that the return value is a Response object
    assert result.status_code == 401  # Assert the status code