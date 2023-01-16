import ast

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from PIL import Image

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<user>')
def hello_world(user=None):  # put application's code here
    return render_template('hello.html', user=user)

@app.route('/end')
def end_world():
    return render_template('end.html')

@app.route('/ai', methods=['GET', 'POST'])
def ai():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            img = Image.open(request.files['file'].stream)
            parcel = {
                "width": img.width,
                "height": img.height
            }
            return redirect(url_for('diagram', parcel=parcel))
    return render_template('ai.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagram/')
@app.route('/diagram/<parcel>')
def diagram(parcel=None):
    dict = ast.literal_eval(parcel)
    return render_template('diagram.html', parcel=dict)

if __name__ == '__main__':
    app.run()
