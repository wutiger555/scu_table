from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, session, redirect, url_for
from scu_request import getTable
import os

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom( 24 )
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    if(session.get('id') is None):
        return redirect(url_for('login'))
    df = getTable(session.get('id'), session.get('passwd'))
    return render_template('table.html', df=df)

@app.route('/login')
def login():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        id = request.values['id']
        passwd = request.values['passwd']
        session['id'] = id
        session['passwd'] = passwd
        
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)