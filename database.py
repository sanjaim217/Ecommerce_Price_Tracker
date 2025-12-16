
import sqlite3

def init_db():
    conn = sqlite3.connect("price_tracker.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS products (url TEXT, price REAL, target REAL)")
    conn.commit()
    conn.close()

def add_product(url, price, target):
    conn = sqlite3.connect("price_tracker.db")
    c = conn.cursor()
    c.execute("INSERT INTO products VALUES (?,?,?)", (url, price, target))
    conn.commit()
    conn.close()

def get_products():
    conn = sqlite3.connect("price_tracker.db")
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    data = c.fetchall()
    conn.close()
    return data
