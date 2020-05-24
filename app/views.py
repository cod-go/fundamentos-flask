from flask import render_template

from app import app


@app.route('/')
def index():
    title = "Live Flask"
    paragraph = "Este é o primeiro teste passando valores para templates com flask"
    return render_template('home.html', title=title, paragraph=paragraph)
