from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import db
from models import *

bp = Blueprint('medications', __name__, url_prefix='/medications')


@bp.route('/')
def medication_list():
    medications = Medication.query.all()
    return render_template('medications.html', medications=medications)


@bp.route('/add', methods=['POST'])
def add_medication():
    if request.method == 'POST':
        
        name = request.form['name']
        method_of_use = request.form['method_of_use']
        description = request.form['description']
        effects = request.form['effects']
        side_effects = request.form['side_effects']
        new_medication = Medication(name=name, method_of_use=method_of_use, description=description, effects=effects, side_effects=side_effects)
       
        try:
            db.session.add(new_medication)
            db.session.commit()
            flash('Успешно добавлено новое лекарство.', 'success')
        except:
            db.session.rollback()
            flash('Ошибка при добавлении нового лекарства. Пожалуйста, проверьте введенные данные.', 'danger')
    
    return redirect(url_for('medications.medication_list'))


@bp.route('medication<int:medication_id>/delete_medication', methods=['POST'])
def delete_medication(medication_id):
    if request.method == 'POST':
        
        medication = Medication.query.get(medication_id)

        if medication:
            try:
                db.session.delete(medication)
                db.session.commit()
                flash('Запись о препарате успешно удалена.', 'success')
            except:
                db.session.rollback()
                flash('Ошибка отправления данных. Не удалось удалить данные!', 'danger')
            
        return redirect(url_for('medications.medication_list'))
    return render_template('medications.html')