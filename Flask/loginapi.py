from flask import Blueprint, app, redirect, render_template, request

login_api = Blueprint('login_api', __name__)



@login_api.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')


@login_api.route('/login', methods=['POST'])
def post_login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    print(f"Username: {username}")
    print(f"Password: {password}")
    return f'Login submitted successfully from {username}.'


@login_api.route('/admin')
def admin():
    return redirect('/login')