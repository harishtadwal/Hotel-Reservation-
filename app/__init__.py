from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)

    login_manager.init_app(app)

    migrate.init_app(app,db)

    login_manager.login_view = "auth.login"

    from app.models import User, Room, Booking, Payment, Hotel

    from app.routes.user import user
    app.register_blueprint(user)

    from app.routes.staff import staff 
    app.register_blueprint(staff)


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.routes.auth import auth
    app.register_blueprint(auth)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return render_template("base.html")

    return app