from flask import Flask, render_template, request, redirect
from src.classes.user import User

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', is_login=False, username="")

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
    
    user = User(username, email, password)
    
    if not user.is_in_db():
        user.signup()
        return render_template('index.html', is_login=True,  username=user.get_username())
    return "No"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 