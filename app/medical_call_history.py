from flask import Blueprint, render_template, request
from app import db
from models import Medication, Appointment
from flask_login import login_required
from sqlalchemy.orm import joinedload

bp = Blueprint('medical_call_history', __name__, url_prefix='/medical_call_history')


@bp.route('/')
@login_required
def medical_call_history():
    # Получение параметров фильтрации из запроса
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    disease_name = request.args.get('disease_name')

    # Запрос на получение медицинской истории вызовов с учетом фильтрации по дате и болезни
    if start_date and end_date:
        medical_call_history = (
            Appointment.query
            .options(joinedload('patient'))
            .filter(
                (Appointment.date.between(start_date, end_date)) | (Appointment.date == None),
                (Appointment.diagnosis.ilike(f'%{disease_name}%'))
            )
            .all()
        )
    elif disease_name:
        # Если дата не выбрана, но указано имя болезни, ищем по названию болезни за все время
        medical_call_history = (
            Appointment.query
            .options(joinedload('patient'))
            .filter(Appointment.diagnosis.ilike(f'%{disease_name}%'))
            .all()
        )
    else:
        medical_call_history = Appointment.query.all()

    print(medical_call_history)

    return render_template('medical_call_history.html', medical_call_history=medical_call_history)
