from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/editor')
def editor():
    return render_template('editor.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/create_account')
def create_account():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 