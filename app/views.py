from flask import render_template

from app import app
from app.database.connection import get_db


@app.route('/')
def index():
    title = "Live Flask"
    paragraph = "Este é o primeiro teste passando valores para templates com flask"
    return render_template('home.html', title=title, paragraph=paragraph)


@app.route('/users')
def list_users():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()
    return render_template('list.html', users=data)


@app.route('/users/<int:pk>')
def detail_user(pk):
    cur = get_db().cursor()
    cur.execute(f"SELECT * FROM users WHERE id={pk}")
    data = cur.fetchone()
    cur.close()
    return render_template('detail.html', user=data)
