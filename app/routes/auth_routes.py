from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        auth_service = AuthService()
        if auth_service.login_user(username, password):
            flash('Login successful!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')