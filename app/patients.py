from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import db
from models import *

bp = Blueprint('patients', __name__, url_prefix='/patients')

@bp.route('/')
def patient_list():
    patients = Patient.query.all()  # Получаем все записи из таблицы пациентов
    return render_template('patients.html', patients=patients)
