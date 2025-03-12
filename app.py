from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello world"

@app.route("/cal2", methods=['GET', 'POST'])
def cal2():
    item.id, item.name, item.category, item.price, item.stock = 
    "0","0","0","0",


    return render_template('', item.id, item.name, item.category, item.price, item.stock)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=8000)