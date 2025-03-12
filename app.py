from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import datetime
from setup.createtable import createTable

dt_now = datetime.datetime.now()
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
    if request.method == "POST":
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
            INSERT INTO zaiko (product_id, name, num, input, output, cold, category)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (product_id, name, num, input_date, output_date, cold, category))
        con.commit()
        con.close()

        # リダイレクトしてフォーム送信後にページを更新
        return redirect(url_for('test'))

    dblist = get_inventory()
    return render_template('test.html', dblen=len(dblist), dblist=dblist)

if __name__ == '__main__':
    createTable()
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
