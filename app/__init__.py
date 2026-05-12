from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager

login_manager = LoginManager()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        from app.models.user import User
        return User.query.get(int(user_id))

    # Register Blueprints
    from app.routes.main_routes import main_bp
    from app.routes.auth_routes import auth_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()  # Creates the database file

    return app