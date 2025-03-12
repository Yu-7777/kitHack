# create tableでtest.dbを事前に作成しておく
import sqlite3 # SQLITEのDBI
import random
from datetime import datetime, timedelta



def createTable():
    dbname="stock.db"
    con = sqlite3.connect( "stock.db" ) # DB接続
    c = con.cursor() # カーソル作成

    # zaikoテーブルが存在するか確認
    c.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND name='zaiko';
    """)

    if c.fetchone():
        return


    c.execute("PRAGMA foeig_keys=true;")

    c.execute("""
    CREATE TABLE IF NOT EXISTS category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        num INTEGER NOT NULL,
        cold INTEGER,
        place_stock TEXT,
        category TEXT
    );
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS item (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_id INTEGER NOT NULL,
        date DATE ,
        num INTEGER NOT NULL,
        foreign key (item_id) references category(id)
    );
    """)

    c.execute("SELECT name FROM sqlite_master WHERE type='table';")

    print(c.fetchall())

    con.commit() # 変更を反映（commitでファイル書き込み)
    con.close()
