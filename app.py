from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random
from datetime import datetime, timedelta
from setup.createtable  import createTable



dt_now = datetime.now()
app = Flask(__name__)

def get_inventory():
    con = sqlite3.connect("stock.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM zaiko")
    rows = cur.fetchall()
    con.close()
    return rows

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == "GET":
        product_id = request.form.get('product_id', '')
        name = request.form.get('product_name', '')
        num = request.form.get('product_num', '')
        input_date = request.form.get('arrival_date', '')
        output_date = request.form.get('shipment_date', '')
        cold = request.form.get('temperature', '')
        category = request.form.get('category', '')

        con = sqlite3.connect("stock.db")
        cur = con.cursor()
        cur.execute("""
            INSERT INTO zaiko (id, name, num, input, output, cold, category)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (product_id, name, num, input_date, output_date, cold, category))
        con.commit()
        con.close()

        # ページをリロードしてフォームの再送信を防ぐ
        return redirect(url_for('test'))

    dblist = get_inventory()
    return render_template('test.html', dblist=dblist)

if __name__ == '__main__':
    createTable()
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
