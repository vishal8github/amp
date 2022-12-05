from flask import Flask, redirect, url_for, render_template

#creating the flask class object
app = Flask(__name__)


@app.route('/admin')  
def admin():  
    return render_template("admin.html")  
  
@app.route('/librarion')  
def librarion():  
    return 'librarion'  
  
@app.route('/student')  
def student():  
    return 'student'  
  
@app.route('/user/<name>')  
def user(name):  
    if name == 'admin':  
        return redirect(url_for('admin'))  
    if name == 'librarion':  
        return redirect(url_for('librarion'))  
    if name == 'student':  
        return redirect(url_for('student'))  

if __name__ == '__main__':  
    app.run(debug = True)  