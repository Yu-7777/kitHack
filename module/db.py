import sqlite3
from datetime import datetime

category_table = "category"
item_table = "item"

def get_connection():
    return sqlite3.connect("stock.db")

def get_cursor():
    con = get_connection()
    cur = con.cursor()
    return con, cur

def add_category(name: str, num: int, cold: int, place_stock: str, category: str) -> None:
    con, cur = get_cursor()
    cur.execute(f'INSERT INTO { category_table } (name, num, cold, place_stock, category) VALUES (?, ?, ?, ?, ?)', (name, num, cold, place_stock, category))
    con.commit()
    con.close()

def add_item(item_id: int, date: str, num: int) -> None:
    con, cur = get_cursor()
    cur.execute(f'INSERT INTO { item_table } (item_id, date, num) VALUES (?, ?, ?)', (item_id, date, num))
    con.commit()
    con.close()