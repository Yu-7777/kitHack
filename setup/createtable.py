# create tableでtest.dbを事前に作成しておく
import sqlite3 # SQLITEのDBI
import random
from datetime import datetime, timedelta
from module import db



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


    c.execute("PRAGMA foreign_keys=true;")

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
    

    # ダミーデータ生成と挿入
    def insert_dummy_data():
        # categoryテーブル用データ生成
        for i in range(1, 11):  # 1〜100のデータを生成
            name = f"商品{i}"
            num = random.randint(1, 500)
            cold = random.choice([0, 1])
            place_stock = f"場所{random.randint(1, 10)}"
            category = random.choice(["食品", "機材", "調理器具"])
            db.add_category(name, num, cold, place_stock, category)

        # itemテーブル用データ生成
        for _ in range(10):  # 100件のデータを生成
            item_id = random.randint(1, 100)  # categoryテーブルのidを参照
            date = (datetime.today() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d')
            num = random.randint(1, 50)
            db.add_item(item_id, date, num)
    
    




    insert_dummy_data()
    print ("ダミーデータ挿入")
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    c.execute("SELECT * FROM item") 
    print(c.fetchall())

    c.execute("SELECT * FROM category") 
    print(c.fetchall())

    con.commit() # 変更を反映（commitでファイル書き込み)
    con.close()
