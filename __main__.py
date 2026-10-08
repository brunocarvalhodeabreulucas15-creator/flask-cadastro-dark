import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def criar_banco():
    con = sqlite3.connect('dados.db')
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE)
    ''')
    con.commit()
    con.close()

criar_banco()

@app.route('/')
def homepag():
    return render_template('homepag.html')

@app.route('/cadastrar', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome'].strip()
        idade = request.form['idade']
        email = request.form['email'].strip()

        con = sqlite3.connect('dados.db')
        cur = con.cursor()
        cur.execute('INSERT INTO usuarios (nome, idade, email) VALUES (?,?,?)', (nome, idade, email))
        con.commit()
        con.close()
        return redirect(url_for('homepag'))
    return render_template('cadastrar.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)