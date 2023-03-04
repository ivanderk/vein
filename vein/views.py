
import os
from flask import Blueprint, redirect, render_template, request, session, url_for

from vein.models import SurveyStat
from .data import extract_answer, get_pending_surveys, get_survey_by_id, get_survey_stats, get_user_by_login, questions, save_survey_answer_by_id, update_survey_stats

vein_bp = Blueprint('vein', __name__)


def get_user():
    return session['CURRENT_USER']


@vein_bp.route('/vein')
def index():
    user_id, user_login = get_user()
    pending = [surv for surv in get_pending_surveys(user_login)]
    return render_template('vein/index.html', pending_surveys=pending)


@vein_bp.route('/vein/survey', methods=['POST'])
def survey():

    if not 'survey_id' in request.form:
        return redirect(url_for('vein.index'))

    survey_id = request.form['survey_id']
    survey = get_survey_by_id(survey_id)

    return render_template('vein/survey.html', questions=questions, survey=survey)


@vein_bp.route('/vein/process_answer', methods=['POST'])
def process_answer():
    user_id, _ = get_user()

    survey_id = request.form['survey_id']
    save_survey_answer_by_id(survey_id, user_id, extract_answer(request.form))
    update_survey_stats(survey_id)
    return redirect(url_for('vein.results', survey_id = survey_id))


@vein_bp.route('/vein/results')
def results():
    user_id, user_login = get_user()
    
    project_id = request.args.get('project_id', type=int)   
    survey_id = request.args.get('survey_id', type=int) 
    stats = get_survey_stats(user_login, project_id = project_id, survey_id=survey_id)

    return render_template('vein/results.html', stats=stats)


@vein_bp.route('/vein/result_stats')
def result_stats():
    user_id, user_login = get_user()
    
    project_id = request.args.get('project_id', type=int)   
    survey_id = request.args.get('survey_id', type=int) 
    stats = get_survey_stats(user_login, project_id = project_id, survey_id=survey_id)
    
    return render_template('vein/result-stats.html', stats=stats)
