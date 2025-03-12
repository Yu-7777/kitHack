from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/test')
def test():
    return render_template('test.html')

@app.route("/cal2", methods=['GET', 'POST'])
def cal2():
    item = {
        "id": "0",
        "name": "0",
        "category": "0",
        "price": "0",
        "stock": "0"
    }
    return render_template('cal2.html', item=item)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)