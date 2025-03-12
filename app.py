from flask import Flask, render_template, request
import sqlite3
import datetime
from setup.createtable  import createTable




dt_now = datetime.datetime.now()
app = Flask(__name__)

def get_inventory():
    con = sqlite3.connect("stock.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM zaiko")
    rows = cur.fetchall()
    con.close()
    return rows


@app.route('/')
def hello_wosrld():
    return "Hello world"

@app.route('/test', methods=['GET','POST'])
def test(): 
    if request.methods="POST":
        
        name = request.form.get('name', '')
        num = request.form.get('num', '')
        input_date = request.form.get('input', '')
        output_date = request.form.get('output', '')
        cold = request.form.get('cold', '')
        price = request.form.get('price', '')
        category = request.form.get('category', '')

        con = sqlite3.connect("stock.db")
        cur = con.cursor()
        cur.execute("""
            INSERT INTO zaiko (name, input, output, cold, price, category)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, input_date, output_date, cold, price, category))
        con.commit()
        con.close()

    dblist = get_inventory()

    return render_template('test.html', dblen=len(dblist), dblist = dblist)

if __name__ == '__main__':
    createTable()
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
