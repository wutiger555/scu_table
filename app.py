from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/login')
def login():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        id = request.values['id']
        passwd = request.values['passwd']
        print(id, passwd)
        
    return render_template('table.html')

if __name__ == '__main__':
    app.run(debug=True)