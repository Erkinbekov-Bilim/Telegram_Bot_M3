# queries.py

CREATE_TABLE_registered = """
    CREATE TABLE IF NOT EXISTS registered (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL,
    city TEXT NOT NULL,
    photo TEXT
    )
"""


INSERT_registered_query = """
    INSERT INTO registered  
    (fullname, age, email, city, photo)
    VALUES
    (?, ?, ?, ?, ?)
"""

SELECT_registered_query = """
    SELECT * FROM registered
"""

