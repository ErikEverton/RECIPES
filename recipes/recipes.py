from flask import Blueprint, render_template, g, request, redirect, url_for, flash

bp = Blueprint('recipes', __name__)

from recipes.auth import login_requied

from recipes.db import get_db

@bp.route('/')
def index():
    db = get_db()
    recipes = db.execute(
        "SELECT r.id, title, ingredients, difficulty, username"
        "   FROM recipe r JOIN users u ON r.chef_id = u.id",
    ).fetchall()
    return render_template("recipes/index.html", recipes=recipes)


@bp.route('/create/', methods=['GET', 'POST'])
@login_requied
def create():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        preparation_time = request.form['preparation_time']
        difficulty = request.form['difficulty']
        category = request.form['category']
        error = None

        if not title:
            error = 'Title is required.'
        elif not ingredients:
            error = 'ingredients is required.'
        elif not instructions:
            error = 'instructions is required.'
        elif not preparation_time:
            error = 'preparation_time is requied.'
        elif not difficulty:
            error = 'difficulty is requied.'
        elif not category:
            error
        
        if error is None:
            db = get_db()
            db.execute(
                'INSERT INTO recipe (title, ingredients, instructions, preparation_time, difficulty, category, chef_id)'
                'VALUES (?, ?, ?, ?, ?, ?, ?)', (title, ingredients, instructions, preparation_time, difficulty, category, g.user['id']), 
            )
            db.commit()
            return redirect(url_for('recipes.index'))
        else:
            flash(error)


    return render_template('recipes/create.html')



