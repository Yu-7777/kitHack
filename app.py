from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random
from datetime import datetime, timedelta
from setup.createtable  import createTable
from module import db


dt_now = datetime.now()
app = Flask(__name__)

@app.route('/test', methods=['GET', 'POST'])
def test():
    dblist = db.select_category()
    if request.method == "GET":
        return render_template('test.html', dblist=dblist)
    if request.method == "POST":
        product_id = request.form.get('product_id', '')
        name = request.form.get('product_name', '')
        num = request.form.get('product_num', '')
        input_date = request.form.get('arrival_date', '')
        output_date = request.form.get('shipment_date', '')
        cold = request.form.get('temperature', '')
        category = request.form.get('category', '')

        print(product_id)

        # ページをリロードしてフォームの再送信を防ぐ
        return redirect(url_for('test'))

    dblist = db.select_category()
    return render_template('test.html', dblist=dblist)

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        name = request.form.get('name', '')
        num = request.form.get('num', '')
        cold = request.form.get('cold', '')
        place_stock = request.form.get('place_stock', '')
        category_val = request.form.get('category', '')

        num = int(num)
        cold = int(cold)

        db.add_category(name=name, num=num, cold=cold, place_stock=place_stock, category=category_val)
        return redirect(url_for('index'))

    dblist = db.select_category()
    dblist = [dict(row) for row in dblist]
    return render_template('index.html', dblist=dblist)

@app.route('/delete_category/<int:id>', methods=['POST'])
def delete_category(id):
    db.delete_category(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    createTable()
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
