from flask import Flask
from src.integracao.routes import routes
from src.integracao.middlewares import Middleware

app = Flask(__name__)

app.wsgi_app = Middleware(app.wsgi_app)
app.register_blueprint(routes, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)