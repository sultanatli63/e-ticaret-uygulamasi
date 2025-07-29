import sqlite3
from models.user import User
from models.product import Product

class Database:
    def __init__(self, db_name='ecommerce.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT
        )''')
        self.conn.commit()

    def add_user(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        self.conn.commit()

    def get_user(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute('SELECT user_id, username, password FROM users WHERE username=? AND password=?', (username, password))
        row = cursor.fetchone()
        if row:
            return User(*row)
        return None

    def add_product(self, name, category, price, description):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO products (name, category, price, description) VALUES (?, ?, ?, ?)', (name, category, price, description))
        self.conn.commit()

    def get_categories(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT DISTINCT category FROM products')
        return [row[0] for row in cursor.fetchall()]

    def get_products_by_category(self, category):
        cursor = self.conn.cursor()
        cursor.execute('SELECT product_id, name, category, price, description FROM products WHERE category=?', (category,))
        return [Product(*row) for row in cursor.fetchall()]

    def get_product_by_id(self, product_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT product_id, name, category, price, description FROM products WHERE product_id=?', (product_id,))
        row = cursor.fetchone()
        if row:
            return Product(*row)
        return None
