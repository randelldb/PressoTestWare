from flask import render_template
from src import app


@app.route('/')
def hello(name=None):
    return render_template('hello.html', name=name)