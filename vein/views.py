
import os
from flask import Blueprint, render_template, session
from .data import get_pending_surveys, get_survey_from_id, questions

vein_bp = Blueprint('vein', __name__)


@vein_bp.route('/vein')
def index():
    pending = get_pending_surveys(session['user_name'])
    return render_template('vein/index.html', pending_surveys=pending)

@vein_bp.route('/vein/survey/<id>')
def survey(id):
    survey = get_survey_from_id(id)
    return render_template('vein/survey.html', questions=questions, current_project='CoE Cloud Google Cloud')

@vein_bp.route('/vein/results')
def results():
    return render_template('vein/results.html')

