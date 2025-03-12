import sqlite3
from datetime import datetime
from typing import Optional, Tuple

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

def select_category(
        name: Optional[str] = None,
        num: Optional[Tuple[str, int]] = None,
        cold: Optional[Tuple[str, int]] = None,
        place_stock: Optional[str] = None,
        category: Optional[str] = None
):
    con, cur = get_cursor()

    columns = []
    values = []

    if name is not None:
        columns.append("name = ?")
        values.append(name)
    if num is not None:
        operator, value = num
        columns.append(f"num { operator } ?")
        values.append(value)
    if cold is not None:
        operator, value = cold
        columns.append(f"cold { operator } ?")
        values.append(value)
    if place_stock is not None:
        columns.append("place_stock = ?")
        values.append(place_stock)
    if category is not None:
        columns.append("category = ?")
        values.append(category)

    query = f"SELECT * FROM { category_table }"
    if columns:
        query += " WHERE " + " AND ".join(columns)

    cur.execute(query, values)
    results = cur.fetchall()

    con.close()
    return results

def select_item(
        item_id: Optional[int] = None,
        date: Optional[Tuple[str, str]] = None,
        num: Optional[Tuple[str, int]] = None
):
    con, cur = get_cursor()

    columns = []
    values = []

    if item_id is not None:
        columns.append("item_id = ?")
        values.append(item_id)
    if date is not None:
        operator, value = date
        columns.append(f"date { operator } ?")
        values.append(value)
    if num is not None:
        operator, value = num
        columns.append(f"num { operator } ?")
        values.append(value)

    query = f"SELECT * FROM { item_table }"
    if columns:
        query += " WHERE " + " AND ".join(columns)

    cur.execute(query, values)
    results = cur.fetchall()

    con.close()
    return results