from flask import Blueprint, request, render_template
from werkzeug.security import check_password_hash, generate_password_hash

from recipes.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        pass

    return render_template("auth/register.html")
        
