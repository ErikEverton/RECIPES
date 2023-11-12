DROP TABLE IF EXISTS user;
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
    Ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL,
    preparation_time INTEGER NOT NULL,
    difficulty TEXT NOT NULL,
    Category TEXT NOT NULL,
    FOREIGN KEY (chef_id) REFERENCES user (id)
);
