DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS recipe;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    hash TEXT NOT NULL 
);

CREATE TABLE recipe(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chef_id INTEGER NOT NULL, 
    title  TEXT UNIQUE NOT NULL,
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL,
    preparation_time INTEGER NOT NULL,
    difficulty TEXT NOT NULL,
    category TEXT NOT NULL,
    FOREIGN KEY (chef_id) REFERENCES users (id)
);

CREATE TABLE comments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    recipe_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    body TEXT NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES recipe (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);
