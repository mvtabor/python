from flask import (
    Blueprint, render_template
)

bp = Blueprint('portafolio', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('portafolio/index.html')

@bp.route('/mail', methods=['POST'])
def mail():
    return 'Chancho'
