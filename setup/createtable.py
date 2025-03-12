# create tableでtest.dbを事前に作成しておく
import sqlite3 # SQLITEのDBI
def createTable():
    dbname="stock.db"
    con = sqlite3.connect( "stock.db" ) # DB接続
    c = con.cursor() # カーソル作成



    c.execute("""
    CREATE TABLE zaiko (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        input DATE,
        output DATE,
        cold INTEGER,
        price INTEGER,
        category TEXT
    );
    """)
    # 2行挿入
    #c.execute("SELECT count(*) FROM zaiko") # 行数取得
    print( "データ件数" )
    
    con.commit() # 変更を反映（commitでファイル書き込み)
    con.close() 