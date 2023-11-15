from flask import Blueprint, render_template, g

bp = Blueprint('recipes', __name__)

from recipes.auth import login_requied

from recipes.db import get_db

@bp.route('/')
def index():
    return render_template("recipes/index.html")
