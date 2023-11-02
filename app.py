from flask import Flask, request, render_template, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your-secret-key'

users = []

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('secured'))
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return 'Please fill in all the fields.'

    password_hash = generate_password_hash(password, method='sha256')
    users.append({'username': username, 'password': password_hash})
    return render_template('index.html')
    

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = next((user for user in users if user['username'] == username), None)
    if user and check_password_hash(user['password'], password):
        session['username'] = username
        return redirect(url_for('secured'))
    return 'Login failed. <a href="/">Try again</a>'

@app.route('/secured')
def secured():
    if 'username' in session:
       return render_template("secured.html")
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))
@app.route('/log')
def log():
   
    return render_template("index.html")
@app.route('/reg')
def reg():
   
    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)
