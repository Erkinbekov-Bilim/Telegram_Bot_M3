# main_db.py

import sqlite3
from db import queries


db = sqlite3.connect('db/registered.sqlite3')
db_store = sqlite3.connect('db/store.sqlite3')

cursor = db.cursor()
cursor_store = db_store.cursor()


async def create_db():
    if db:
        print("Database created")

    cursor.execute(queries.CREATE_TABLE_registered)
    cursor_store.execute(queries.CREATE_TABLE_store)
    cursor_store.execute(queries.CREATE_TABLE_product_details)
    cursor_store.execute(queries.CREATE_TABLE_collection_products)

async def sql_insert_registered(fullname, age, email, city, photo):
    cursor.execute(queries.INSERT_registered_query, (fullname, age, email, city, photo))
    db.commit()

async def sql_insert_store(product_name, product_size, product_price, product_photo, product_id):
    cursor_store.execute(queries.INSERT_store_QUERY, (
        product_name, product_size, product_price, product_photo, product_id
    ))
    db_store.commit()

async def sql_insert_product_details(product_id, product_category, product_info):
    cursor_store.execute(queries.INSERT_product_details_QUERY, (
        product_id, product_category, product_info
    ))
    db_store.commit()

async def sql_insert_collection_product(product_id, collection):
    cursor_store.execute(queries.INSERT_collection_products_QUERY, (
        product_id, collection
    ))
    db_store.commit()


# CRUD - Create, Read, Update, Delete
# ==============================================================

def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT * FROM store s
    INNER JOIN product_details sd 
    INNER JOIN collection_products cp
    ON s.product_id = sd.product_id 
    AND s.product_id = cp.product_id
    """).fetchall()
    conn.close()

    return products

def delete_product(product_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM store WHERE product_id = ?", (product_id,))
    conn.execute('DELETE FROM product_details WHERE product_id = ?', (product_id,))
    conn.execute('DELETE FROM collection_products WHERE product_id = ?', (product_id,))
    conn.commit()
    conn.close()

