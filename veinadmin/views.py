
import os
from flask import Blueprint, render_template

veinadmin_bp = Blueprint('veinadmin', __name__)


@veinadmin_bp.route('/veinadmin')
def index():
    return render_template('veinadmin/index.html')

