from flask import Flask, render_template, request
import sqlite3
import random
from datetime import datetime, timedelta
from setup.createtable  import createTable



dt_now = datetime.now()
app = Flask(__name__)

@app.route('/')
def hello_wosrld():

    return "Hello world"

@app.route('/test')
def test():
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    dblen, dblist = 0, []
    
    if request.methods=="GET":
        var1 = None
    else:
        name = request.form.get('name','')
        num = request.form.get('num','')
        input = request.form.get('input','')
        output = request.form.get('output','')
        category = request.form.get('category','')

        con.commit()
        cur.execute("SELECT * FROM log ORDER BY id DESC")
        dblist = cur.fetchall()
        con.close()

    return render_template('test.html', dblen=len(dblist), dblist = dblist)

if __name__ == '__main__':
    createTable()
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
