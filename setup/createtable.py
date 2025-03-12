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
    '''
    # ダミーデータ生成用のカテゴリ
    categories = ["食品", "飲料", "雑貨", "家電", "衣類"]
    names = ["商品A", "商品B", "商品C", "商品D", "商品E"]

    # ダミーデータの挿入
    for _ in range(100):
        name = random.choice(names) + str(random.randint(1, 100))
        num = random.randint(1, 100)
        input_date = datetime.now() - timedelta(days=random.randint(1, 365))
        output_date = input_date + timedelta(days=random.randint(1, 30))
        cold = random.choice([0, 1])  # 冷蔵（0: なし, 1: あり）
        price = random.randint(100, 10000)
        category = random.choice(categories)
        
        # データ挿入クエリ
        c.execute("""
        INSERT INTO zaiko (name, num, input, output, cold, price, category)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """, (name, num, input_date.strftime("%Y-%m-%d"), output_date.strftime("%Y-%m-%d"), cold, price, category))




        
    print( "ダミーデータ１００個追加" )
    c.execute("SELECT * FROM zaiko") # 行数取得
    print (c.fetchall())
    '''

    c.execute("SELECT name FROM sqlite_master WHERE type='table';")

    print(c.fetchall())

    con.commit() # 変更を反映（commitでファイル書き込み)
    con.close() 