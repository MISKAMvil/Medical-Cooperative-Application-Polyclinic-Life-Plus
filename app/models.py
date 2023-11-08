import os

from datetime import datetime

import sqlalchemy as sa
# импортируется библиотека SQLAlchemy под псевдонимом sa

from users_policy import UsersPolicy

from werkzeug.security import check_password_hash, generate_password_hash

from flask_login import UserMixin

from flask import url_for, current_app

from app import db
# импортируется объект db из модуля app


class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100))
    gender = db.Column(db.String(10), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    home_address = db.Column(db.String(100), nullable=False)

    @property
    def full_name(self):
        return ' '.join([self.last_name, self.first_name, self.middle_name or ''])

    def __repr__(self):
        return '<Patient %r %r %r>' % (self.first_name, self.last_name, self.middle_name)


class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    symptoms = db.Column(db.String(255), nullable=False)
    diagnosis = db.Column(db.String(255), nullable=False)

    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    patient = db.relationship('Patient', backref=db.backref('appointments', lazy=True))
    # medications = db.relationship('Medication', backref='medications_relation', lazy=True)
    medications = db.relationship("Medication", back_populates="appointment", overlaps="medications_relation")

    def __repr__(self):
        return f"Appointment(id={self.id}, date={self.date}, patient_id={self.patient_id})"


class Medication(db.Model):
    __tablename__ = 'medications'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    method_of_use = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    effects = db.Column(db.Text, nullable=False)
    side_effects = db.Column(db.Text, nullable=False)

    # appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'), nullable=False)
    # appointment = db.relationship('Appointment', backref='medications_relation', lazy=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'))
    appointment = db.relationship("Appointment", back_populates="medications", overlaps="medications_relation")

    def __repr__(self):
        return f"Medication(id={self.id}, name='{self.name}', appointment_id={self.appointment_id})"


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    # role = db.relationship('Roles')
    # reviews = db.relationship('Review', backref='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# -----
    def __init__(self, user_id, user_login, role_id):
        self.id = user_id
        self.login = user_login
        self.role_id = role_id
        
	# Возвращает тру, если пользователь админ, и фолс, если нет
    def is_admin(self):
        # Сравнивается Id роли с админским
        return self.role_id == current_app.config['ADMINISTRATOR_ROLE_ID']
    
	# Метод, отвечающий за проверку прав
	# Метод `can` создает экземпляр класса `UsersPolicy` с переданной записью и подгружает
	#  метод `action` этого класса, который отвечает за проверку полномочий пользователя на
	#  выполнение данного действия. Если метод найден, то он вызывается и возвращается его
	#  результат. Если метод не найден, то возвращается `False`.
    def can(self, action, record = None):
        users_policy = UsersPolicy(record)
        method = getattr(users_policy, action, None)
        if method:
            return method()
        return False
# -----

    @property
    def full_name(self):
        return ' '.join([self.last_name, self.first_name, self.middle_name or ''])

    def __repr__(self):
        return '<User %r>' % self.login


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    desc = db.Column(db.Text, nullable=False)

    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name