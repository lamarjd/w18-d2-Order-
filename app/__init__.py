# bootstrap (that means "declare and configure") your Flask app with the Blueprint from app.routes.order and the configuration object. This time, give relative imports a try. (See them, there?)

from flask import Flask
from .config import Configuration
#  import the db variable from the models module. Then, pass the app variable into the db.init_app method.
from .models import db, Employee   # New import
from .routes import orders
from .routes import session
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(orders.bp)
app.register_blueprint(session.bp)
db.init_app(app)  # Configure the application with SQLAlchemy


login = LoginManager(app)
login.login_view = "session.login"


@login.user_loader
def load_user(id):
    return Employee.query.get(int(id))