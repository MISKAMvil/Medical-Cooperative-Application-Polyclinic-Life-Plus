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
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    middle_name = request.form['middle_name']
    gender = request.form['gender']
    birth_date = request.form['birth_date']
    home_address = request.form['home_address']

    new_patient = Patient(first_name=first_name, last_name=last_name, middle_name=middle_name, gender=gender, birth_date=birth_date, home_address=home_address)

    try:
        db.session.add(new_patient)
        db.session.commit()
        flash('Запись о пациенте успешно добавлена.', 'success')
    except:
        db.session.rollback()
        flash('Ошибка отправления данных. Введены некорректные данные или не все поля заполнены!', 'danger')
        # return redirect(url_for('patients.patient_list'))

    # flash('Запись о пациенте успешно добавлена.', 'success')
    return redirect(url_for('patients.patient_list'))

@bp.route('/delete_patient/<int:patient_id>', methods=['POST'])
def delete_patient(patient_id):
    if request.method == 'POST':
        
        patient = Patient.query.get(patient_id)

        if patient:
            try:
                db.session.delete(patient)
                db.session.commit()
                flash('Запись о пациенте успешно удалена.', 'success')
            except:
                db.session.rollback()
                flash('Ошибка отправления данных. Не удалось удалить данные!', 'danger')
            
        return redirect(url_for('patients.patient_list'))
    return render_template('patients.html')

@bp.route('/appointments/<int:patient_id>')
def appointments(patient_id):
    patient = Patient.query.get(patient_id)
    # Получаем информацию об осмотрах пациента из базы данных
    appointments = Appointment.query.filter_by(patient_id=patient_id).all()
    return render_template('appointments.html', patient=patient, appointments=appointments)