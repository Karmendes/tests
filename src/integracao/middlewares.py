from werkzeug.wrappers import Request,Response
from abc import ABC,abstractmethod

class ValidateRoute(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def validate(self):
        pass


class ValidateRouteCircle(ValidateRoute):
    def __init__(self,data):
        self.data = data
    def validate(self):
        if 'radius' not in self.data:
            return Response(u"Key 'radius' not found", mimetype= 'text/plain', status=401)
        if isinstance(self.data['radius'],int):
            return self.data
        else:
            return Response(u"Value 'radius' must be a number", mimetype= 'text/plain', status=401)

class ValidateRouteSquare(ValidateRoute):
    def __init__(self,data):
        self.data = data
    def validate(self):
        if 'side' not in self.data:
            return Response(u"Key 'side' not found", mimetype= 'text/plain', status=401)
        if isinstance(self.data['side'],int):
            return self.data
        else: 
            return Response(u"Value 'side' must be a number", mimetype= 'text/plain', status=401)

class ValidateRouteTriangle(ValidateRoute):
    def __init__(self,data):
        self.data = data
    def validate(self):
        if any(key not in self.data for key in ['base','height']):
            return Response(u"Key 'base' or 'height' not found", mimetype= 'text/plain', status=401)
        if isinstance(self.data['base'],int) and isinstance(self.data['height'],int):
            return self.data
        else: 
            return Response(u"Value 'base' and 'height' must be a number", mimetype= 'text/plain', status=401)

factory = {
    '/triangle':ValidateRouteTriangle,
    '/square':ValidateRouteSquare,
    '/circle':ValidateRouteCircle
}

class Middleware:
    def __init__(self, app):
        self.app = app
    def __call__(self,environ,start_response):
        # get data 
        request = Request(environ)
        data = request.get_json()
        route = request.path
        # Choose the class accordingly with route
        class_validation = factory[route]
        # Instance the valid class
        class_midleware = class_validation(data)
        res = class_midleware.validate()
        # If not pass for the validation
        if isinstance(res,Response):
            return res(environ, start_response)
        # if pass
        environ['data'] = res 
        return self.app(environ, start_response)
