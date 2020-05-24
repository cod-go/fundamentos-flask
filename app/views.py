from flask import render_template, request, url_for, redirect

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


@app.route('/users/new', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        cur = get_db().cursor()
        cur.execute(f"INSERT INTO users(name) VALUES('{request.form['name']}')")
        get_db().commit()
        cur.close()
        return redirect(url_for('list_users'))
    return render_template('form.html')


@app.route('/users/<int:pk>/edit', methods=['GET', 'POST'])
def update_user(pk):
    cur = get_db().cursor()
    if request.method == "POST":
        cur.execute(f"UPDATE users SET name='{request.form['name']}' WHERE id={pk}")
        get_db().commit()
        cur.close()
        return redirect(url_for('list_users'))
    cur.execute(f"SELECT name FROM users WHERE id = {pk}")
    name = cur.fetchone()['name']
    return render_template('form.html', name=name, pk=pk)
