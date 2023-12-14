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
    person_details = request.form['person_details']

    new_patient = Patient(first_name=first_name,
                          last_name=last_name,
                          middle_name=middle_name,
                          gender=gender,
                          birth_date=birth_date,
                          home_address=home_address,
                          person_details=person_details)

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


@bp.route('/patient<int:patient_id>/delete_patient', methods=['POST'])
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


@bp.route('/patient<int:patient_id>', methods=['GET'])
def appointments(patient_id):
    patient = Patient.query.get(patient_id)
    # Получаем информацию об осмотрах пациента из базы данных
    appointments = Appointment.query.filter_by(patient_id=patient_id).all()
    medications = Medication.query.all()
    return render_template('appointments.html', patient=patient, appointments=appointments, medications=medications)


@bp.route('/patient<int:patient_id>/add_appointment', methods=['POST'])
def add_appointment(patient_id):
    if request.method == 'POST':
        location = request.form.get('location')
        symptoms = request.form.get('symptoms')
        diagnosis = request.form.get('diagnosis')
        medications_ids = request.form.getlist('medications')
        prescription = request.form.get('prescription')
        
        new_appointment = Appointment(symptoms=symptoms, diagnosis=diagnosis, patient_id=patient_id)
        for medication_id in medications_ids:
            medication = Medication.query.get(medication_id)
            new_appointment.medications.append(medication)

        try:
            db.session.add(new_appointment)
            db.session.commit()
            flash('Запись о пациенте успешно добавлена.', 'success')
        except:
            db.session.rollback()
            flash('Ошибка отправления данных. Введены некорректные данные или не все поля заполнены!', 'danger')

        return redirect(url_for('patients.appointments', patient_id=patient_id))
    return redirect(url_for('patients.patient_list'))