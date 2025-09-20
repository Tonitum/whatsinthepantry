import sqlite3


def init_db():
    with sqlite3.connect('recipes.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            meal TEXT
        )''')
        conn.execute('''CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY,
            recipe_id INTEGER,
            name TEXT,
            FOREIGN KEY (recipe_id) REFERENCES recipes(id)
        )''')
        conn.commit()
