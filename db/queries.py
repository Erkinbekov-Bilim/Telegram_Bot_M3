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

CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    product_size TEXT,
    product_price TEXT,
    product_photo TEXT,
    product_id TEXT
    )
"""

CREATE_TABLE_product_details = """
    CREATE TABLE IF NOT EXISTS product_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT,
    product_category TEXT,
    product_info TEXT
    )
"""

CREATE_TABLE_collection_products = """
    CREATE TABLE IF NOT EXISTS collection_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT,
    collection TEXT
    )
"""

INSERT_store_QUERY = """
    INSERT INTO store (product_name, product_size, product_price, product_photo, product_id)
    VALUES (?, ?, ?, ?, ?)
"""

INSERT_product_details_QUERY = """
    INSERT INTO product_details (product_id, product_category, product_info)
    VALUES (?, ?, ?)
"""

INSERT_collection_products_QUERY = """
    INSERT INTO collection_products (product_id, collection)
    VALUES (?, ?)
"""
