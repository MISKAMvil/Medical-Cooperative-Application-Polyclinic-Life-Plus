from flask import Flask, render_template
# импортирует класс `Flask` из модуля `flask`

from sqlalchemy import MetaData
# импортируется класс MetaData из библиотеки SQLAlchemy - это объект, который содержит информацию о базе данных SQL

from flask_sqlalchemy import SQLAlchemy
# импортируется класс SQLAlchemy из Flask SQLAlchemy  - это расширение Flask, которое предоставляет доступ к объекту базы данных SQLAlchemy в приложении Flask

from flask_migrate import Migrate
# Библиотека Flask-Migrate позволяет мигрировать базы данных в приложении Flask, используя SQLAlchemy

from prometheus_client import Summary, generate_latest
# from prometheus_client import Counter, start_http_server
from prometheus_flask_exporter import PrometheusMetrics

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
# создание метрики для отслеживания затраченного времени и выполненных запросов.

app = Flask(__name__)
# создает экземпляр приложения Flask, с именем текущего модуля (__name__ - это встроенная переменная, которая содержит имя текущего модуля)

application = app
# копирует объект приложения Flask в новую переменную `application`. Обычно используется, когда запускается сервер приложений, который ожидает переменную `application` в качестве имени приложения

metrics = PrometheusMetrics(app, group_by='endpoint')

app.config.from_pyfile('config.py')
# подклюячаем 'config.py', он содержит переменные с параметрами конфигурации, которые могут быть использованы в приложении (настройки базы данных, настройки безопасности, параметры сессии)

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
# Создание словаря "convention", содержащего соглашение об именовании для различных ограничений таблицы

metadata = MetaData(naming_convention=convention)
# Создание объекта "metadata" класса MetaData, принимающего словарь "convention" в качестве параметра

db = SQLAlchemy(app, metadata=metadata)
#  Создание объекта SQLAlchemy для взаимодействия с базой данных, принимающего объект "app" (Flask-приложение) и объект "metadata" в качестве параметров

migrate = Migrate(app, db)
# Создание объекта "migrate" класса Migrate для выполнения миграций в базе данных, принимающего объект "app" и объект SQLAlchemy "db" в качестве параметров

from models import *
# Чтобы flask_migrate увидел нашу модель, ее надо импортировать

from auth import bp as auth_bp, init_login_manager
from patients import bp as patients_bp
from medications import bp as medications_bp
from medical_call_history import bp as medical_call_history_bp

app.register_blueprint(auth_bp)
app.register_blueprint(patients_bp)
app.register_blueprint(medications_bp)
app.register_blueprint(medical_call_history_bp)

init_login_manager(app)

# @app.before_request
# def before_request():
#     if not request.is_secure:
#         url = request.url.replace('http://', 'https://', 1)
#         code = 301
#         return redirect(url, code=code)


@app.route('/')
@REQUEST_TIME.time()
def index():
    return render_template('index.html')


@app.route('/metrics')
def metrics():
    return generate_latest()

# if __name__ == '__main__':
#     app.run(debug=True, threaded=True)