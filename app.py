from flask import Flask, render_template, request, redirect
from src.classes.user import User

app = Flask(__name__)

is_login: bool = False

@app.route('/')
def index():
    return render_template('index.html', is_login=is_login, username="")

@app.route('/editor')
def editor():
    return render_template('editor.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/create_account')
def create_account():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    user = User(email, password, username)
    
    if user.is_in_db():
        return redirect('/login')

    user.signup()
    is_login = True
    return render_template('index.html', is_login=is_login,  username=user.get_username())

@app.route('/auth', methods=['POST'])
def auth():
    email = request.form['email']
    password = request.form['password']
    
    user = User(email, password)
    
    if not user.is_in_db():
        return redirect('/create_account')
    
    is_login = True
    return render_template('index.html', is_login=is_login,  username=user.get_username())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 