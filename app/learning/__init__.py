from flask import Blueprint

bp = Blueprint('learning', __name__, url_prefix='/learn')

from app.learning import routes