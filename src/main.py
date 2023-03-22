from flask import Flask

from routes import routes


def create_app():
    new_app = Flask(__name__)
    new_app.static_folder = 'static'
    new_app.register_blueprint(routes)
    return new_app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
