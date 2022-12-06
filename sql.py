import sqlite3


conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS categories(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(32) NOT NULL UNIQUE,
#         is_published BOOLEAN DEFAULT(false)
#     );
# ''')
# conn.commit()
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS products(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(32) NOT NULL,
#         descr VARCHAR(1024),
#         price DECIMAL(7, 2) NOT NULL DEFAULT(0.0),
#         category_id INTEGER NOT NULL,
#         FOREIGN KEY (category_id) REFERENCES categories(id)
#         ON DELETE CASCADE
#     );
# ''')
# conn.commit()
# cur.executemany('''
#     INSERT INTO categories(name, is_published)
#     VALUES(?, ?);
# ''', (('Food', True), ('Drinks', True)))
# conn.commit()
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS users(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(64) NOT NULL,
#         email VARCHAR(64) NOT NULL UNIQUE,
#         referrer_id INTEGER,
#         FOREIGN KEY (referrer_id) REFERENCES users(id) ON DELETE NO ACTION
#     );
# ''')
# conn.commit()
