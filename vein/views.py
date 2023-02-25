
import os
from flask import Blueprint, render_template

vein_bp = Blueprint('vein', __name__)

questions = [
    "My enthusiasm regarding the work I do...",
    "The Teamwork atmosphere and communication during the last sprints were...",
    "To what extent the tasks were challenging enough for me...",
    "I would rate my value contributed to the team as follows...",
    "The workload of this/the last sprint was...",
    "I feel supported by the client and stakeholders...",
    "I feel recognized and praised by the team...",
    "I feel inspired and excited to work in this team for the coming sprints..."
]


@vein_bp.route('/vein')
def index():
    return render_template('vein/index.html', questions=questions)