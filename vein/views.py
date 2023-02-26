
import os
from flask import Blueprint, render_template
from .data import questions

vein_bp = Blueprint('vein', __name__)


@vein_bp.route('/vein')
def index():
    return render_template('vein/index.html')

@vein_bp.route('/vein/survey')
def survey():
    return render_template('vein/survey.html', questions=questions, current_project='CoE Cloud Google Cloud')

@vein_bp.route('/vein/results')
def results():
    return render_template('vein/results.html')

