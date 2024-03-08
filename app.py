from flask import Flask
from src.integracao.routes import routes
from src.integracao.routes import calc_square,calc_circle,calc_triangle

app = Flask(__name__)

app.register_blueprint(routes, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)