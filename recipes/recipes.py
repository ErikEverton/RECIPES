from flask import Blueprint

bp = Blueprint('recipes', __name__)

from recipes.auth import login_requied

from recipes.db import get_db

@bp.route('/')
def index():
    return "index"
