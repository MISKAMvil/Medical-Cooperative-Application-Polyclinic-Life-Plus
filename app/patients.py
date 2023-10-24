from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import db
from models import *

bp = Blueprint('patients', __name__, url_prefix='/patients')

@bp.route('/')
def patient_list():
    patients = Patient.query.all()  # Получаем все записи из таблицы пациентов
    return render_template('patients.html', patients=patients)

@bp.route('/add_patient', methods=['POST'])
def add_patient():
    name = request.form['name']
    gender = request.form['gender']
    birth_date = request.form['birth_date']
    home_address = request.form['home_address']

    new_patient = Patient(name=name, gender=gender, birth_date=birth_date, home_address=home_address)

    try:
        db.session.add(new_patient)
        db.session.commit()
        flash('Рецензия успешно отправлена на проверку.', 'success')
    except:
        db.session.rollback()
        flash('Ошибка отправления данных. Введены некорректные данные или не все поля заполнены!', 'danger')
        # return redirect(url_for('patients.patient_list'))

    # flash('Рецензия успешно отправлена на проверку.', 'success')
    return redirect(url_for('patients.patient_list'))