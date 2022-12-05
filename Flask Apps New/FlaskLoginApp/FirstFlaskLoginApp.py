from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    uname = request.form['uname']
    password = request.form['password']

    if uname == 'vishal' and password == 'root':
        return f"Welcome {uname}"
    else:
        return "Login Failed"


if __name__ == '__main__':
    app.run(debug = True)