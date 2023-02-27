
from dataclasses import dataclass
import os
from flask import Blueprint, redirect, render_template, request, session, url_for
from .data import extract_answer, get_pending_surveys, get_survey_by_id, get_user_by_id, get_user_by_user_name, questions, save_survey_answer_by_id

vein_bp = Blueprint('vein', __name__)


def get_user():
    return session['CURRENT_USER']


@vein_bp.route('/vein')
def index():
    user_id, user_login = get_user()
    pending = get_pending_surveys(user_login)
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
    user_id, user_login = get_user()

    survey_id = request.form['survey_id']
    save_survey_answer_by_id(survey_id, user_id, extract_answer(request.form))

    return redirect(url_for('vein.index'))


@vein_bp.route('/vein/results')
def results():
    user_id, user_login = get_user()

    user = get_user_by_id(user_id)
    stats = get_survey_stats(user.projects[0].id)
    return render_template('vein/results.html', stats=stats, projects=user.projects)


@vein_bp.route('/vein/result_stats')
def result_stats():
    user_id, user_login = get_user()
    project_id = int(request.values.get("project_id"))
    user = get_user_by_id(user_id)

    stats = get_survey_stats(project_id)
    return render_template('vein/result-stats.html', stats=stats)


@dataclass
class SurveyStat:
    rating: int
    mood: int
    completed: int
    label: str


def get_survey_stats(project_id):

    if project_id == 1:
        return SurveyStat(4, 4, 30, "From January 1st to February 1st")
    else:
        return SurveyStat(1, 2, 70, "back from 2022")
