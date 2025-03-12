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

if __name__ == '__main__':
    createTable()
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
