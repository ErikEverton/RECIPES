from flask import Blueprint, request, render_template, url_for, flash, get_flashed_messages, redirect
from werkzeug.security import check_password_hash, generate_password_hash

from recipes.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirmation = request.form["confirmation"]
        db = get_db
        error = None

        if not username:
            error = 'Username is required.'
        if not password:
            error = 'Password is required.'
        if not confirmation:
            error = 'Confirmation is required.'
        if confirmation != password:
            error = 'Confirmation and password must be equal'

        if error is None:
            try:
                db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", (username, generate_password_hash(password)))
                db.commit()
            except db.IntegrityError:
                error = f"User username is already registered."
            else:
                return redirect(url_for("auth.login"))
        flash(error)

    return render_template("auth/register.html")
        
