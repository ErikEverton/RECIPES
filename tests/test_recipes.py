import pytest
from recipes.db import get_db

def test_index(client, auth):
    response = client.get('/')
    assert b'Log In' in response.data
    assert b'Register' in response.data

    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'test title' in response.data
    assert b'href="/update/1"' in response.data


@pytest.mark.parametrize('path', (
    '/create/',
    '/update/1',
    '/delete_recipe/1',
    '/delete_comment/1',
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers["Location"] == "/auth/login/"


def test_author_required(app, client, auth):
    with app.app_context():
        db = get_db()
        db.execute('UPDATE recipe SET chef_id = 2 WHERE id = 1')
        db.commit()

    auth.login()
    assert client.post('/update/1').status_code == 403
    assert client.post('/delete_recipe/1').status_code == 403
    assert b"href=/update/1" not in client.get('/').data


@pytest.mark.parametrize('path', (
    '/update/2',
    '/delete/2',
))
def test_exists_required(client, auth, path):
    auth.login()
    assert client.post(path).status_code == 404


def test_create(client, auth, app):
    auth.login()
    assert client.get('/create/').status_code == 200
    client.post('/create/', data={'title': 'created', 'ingredients': 'test', 'instructions': 'test', 'preparation_time': 1, 'difficulty': 'test', 'category': 'test'})

    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM recipe').fetchone()[0]
        assert count == 2

    
def test_update(client, auth, app):
    auth.login()
    assert client.get('/update/1').status_code == 200
    client.post('/update/1', data={'title': 'updated', 'ingredients': 'test', 'instructions': 'test', 'preparation_time': 1, 'difficulty': 'test', 'category': 'test'})

    with app.app_context():
        db = get_db()
        recipe = db.execute('SELECT * FROM recipe WHERE id = 1').fetchone()
        assert recipe['title'] == 'updated'


@pytest.mark.parametrize('path', (
    '/create',
    'update/1',
))
def test_create_update_validate(client, auth, path):
    auth.login()
    response = client.post(path, data={'title': '', 'ingredients': '', 'instructions': '', 'preparation_time': 1, 'difficulty': '', 'category': ''})
    b"title is required" in response.data


def test_delete(client, auth, app):
    auth.login()
    response = client.post('delete_recipe/1')
    assert response.headers['Location'] == '/'
    
    with app.app_context():
        db = get_db()
        recipe = db.execute('SELECT * FROM recipe WHERE id = 1').fetchone()
        assert recipe is None


def test_delete_comment(client, auth, app):
    auth.login()
    
    with app.app_context():
        db = get_db()
        comment = db.execute('SELECT * FROM comments WHERE id = 1').fetchone()
        assert comment is None

