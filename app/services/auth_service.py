from app.models.user import User
from app import db
from flask_login import login_user, logout_user, current_user

class AuthService:
    @staticmethod
    def register_user(username, email, password):
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return False  # User already exists
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return True

    @staticmethod
    def login_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return True
        return False

    @staticmethod
    def logout_user():
        logout_user()

    @staticmethod
    def get_current_user():
        return current_user if current_user.is_authenticated else None
    