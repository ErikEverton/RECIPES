from flask import Blueprint, render_template, g, request, redirect, url_for, flash, abort

bp = Blueprint('recipes', __name__)

from recipes.auth import login_required

from recipes.db import get_db

@bp.route('/')
def index():
    db = get_db()
    recipes = db.execute(
        "SELECT r.id, chef_id, title, ingredients, difficulty, username"
        "   FROM recipe r JOIN users u ON r.chef_id = u.id"
    ).fetchall()
    return render_template("recipes/index.html", recipes=recipes)


@bp.route('/create/', methods=['GET', 'POST'])
@login_required
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


@bp.route('/recipe/<int:recipe_id>', methods=['GET', 'POST'])
def recipe(recipe_id):
    db = get_db()
    if request.method == 'POST':
        if not g.user:
            return redirect(url_for('auth.login'))
        body = request.form['body']
        error = None

        if not body:
            error = 'comment is required'
        
        if error is None:
            user_id = g.user['id']
            db.execute(
                'INSERT INTO comments (recipe_id, user_id, body)'
                'VALUES (?, ?, ?)', (recipe_id, user_id, body),
            )
            db.commit()
        
        return redirect(url_for('recipes.recipe', recipe_id=recipe_id))
            
    
    recipe = db.execute(
        "SELECT * FROM recipe r"
        "   JOIN users u ON u.id = r.chef_id"
        "   WHERE r.id = ? ", (recipe_id,)
    ).fetchone()
    comments = db.execute(
        "SELECT * FROM comments c"
        "   JOIN users u ON u.id = user_id"
        "   WHERE recipe_id = ? ", (recipe_id,)
    )
    return render_template('recipes/recipe.html', data=recipe, comments=comments)


def get_recipe(id, check_autor=True):
    post = get_db().execute(
        'SELECT * FROM recipe WHERE id = ?', (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")
    
    if check_autor and post['chef_id'] != g.user['id']:
        abort(403)
    
    return post


def get_comment(id):
    comment = get_db().execute(
        'SELECT * FROM comments WHERE id = ?', (id, )
    ).fetchone()

    return comment


@bp.route('/update/<int:recipe_id>', methods=('GET', 'POST'))
@login_required
def update(recipe_id):
    recipe = get_recipe(recipe_id)
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
            error = 'Ingredients is required.'
        elif not instructions:
            error = 'Instructions is required.'
        elif not preparation_time:
            error = 'Preparation_time is requied.'
        elif not difficulty:
            error = 'Difficulty is requied.'
        elif not category:
            error = 'Category is required.'

        if error is None:
            db = get_db()
            db.execute(
                'UPDATE recipe SET title = ?, ingredients = ?, instructions=?, preparation_time=?, difficulty=?, category=?'
                'WHERE id = ?',
                (title, ingredients, instructions, preparation_time, difficulty, category, recipe_id)
            )
            db.commit()
            return redirect(url_for('index'))


    return render_template('recipes/update.html', recipe=recipe)


@bp.route('/delete_recipe/<int:recipe_id>', methods=('POST',))
@login_required
def delete_recipe(recipe_id):
    get_recipe(recipe_id)
    db = get_db()
    db.execute('DELETE FROM recipe WHERE id = ?', (recipe_id, ))
    db.commit()
    return redirect(url_for('index'))


@bp.route('/delete_comment/<int:comment_id>', methods=('POST',))
@login_required
def delete_comment(comment_id):
    comment = get_comment(comment_id)
    db = get_db()
    db.execute('DELETE FROM comments WHERE id = ?', (comment_id, ))
    db.commit()
    return redirect(url_for('recipes.recipe', recipe_id=comment['recipe_id']))
