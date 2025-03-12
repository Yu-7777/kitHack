import sqlite3
from datetime import datetime

def get_connection():
    return sqlite3.connect("stock.db")

def get_cursor():
    con = get_connection()
    cur = con.cursor()
    return con, cur

def add_product(name: str, num: int, cold: int, place_stock: str, category: str) -> None:
    con, cur = get_cursor()
    cur.execute(""")