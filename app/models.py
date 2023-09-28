import os

import sqlalchemy as sa
# импортируется библиотека SQLAlchemy под псевдонимом sa

# from users_policy import UsersPolicy

# from werkzeug.security import check_password_hash, generate_password_hash

# from flask_login import UserMixin

# from flask import url_for, current_app

from app import db
# импортируется объект db из модуля app

class Patient(db.Model):
    tablename = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    home_address = db.Column(db.String(100), nullable=False)

    def repr(self):
        return '<Patient %r>' % self.name
