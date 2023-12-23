from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from models import *
from users_policy import UsersPolicy
from functools import wraps

# Создается объект "bp" типа Blueprint для модуля "auth" в приложении Flask с именем "name".
#  При обращении к маршрутам модуля "auth", они будут иметь префикс "/auth".
bp = Blueprint('auth', __name__, url_prefix='/auth')

# Функция "init_login_manager" создает и настраивает объект "login_manager" класса "LoginManager"
# для управления аутентификацией пользователей в приложении Flask
def init_login_manager(app):
	login_manager = LoginManager()
	# Создан экземпляр класса
	login_manager.init_app(app)
	# Даем приложению знать о существования логин менеджера
	login_manager.login_view = 'auth.login'
	login_manager.login_message = 'Для выполнения данного действия необходимо пройти процедуру аутентификации.'
	login_manager.login_message_category = 'warning'
	# функция "load_user" будет вызвана при каждой следующей авторизации пользователя,
	#  чтобы получить информацию о пользователе из базы данных или источника данных
	login_manager.user_loader(load_user)


def load_user(user_id):
    user = User.query.get(user_id)
    return user

# Декоратор для проверки прав доступа к страничке, для исбежания повторения кода
def permission_check(action):
    def decor(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            user_id = kwargs.get('user_id')
            user = None
            if user_id:
                user = load_user(user_id)
            if not current_user.can(action, user):
                flash('Недостаточно прав для выполнения данного действия.', 'warning')
                return redirect(url_for('books.main_page'))
            return function(*args, **kwargs)
        return wrapper
    return decor


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login and password:
            user = User.query.filter_by(login=login).first()
            if user and user.check_password(password):
                login_user(user)
                flash('Вы успешно аутентифицированы.', 'success')
                next = request.args.get('next')
                return redirect(next or url_for('index'))
        flash('Невозможно аутентифицироваться с указанными логином и паролем!', 'danger')
    return render_template('login.html')


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))