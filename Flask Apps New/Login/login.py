from flask import Flask, render_template, redirect, url_for, request, make_response
  
app = Flask(__name__)  
 
@app.route('/error')  
def error():  
    return "<p><strong>Enter correct password</strong></p>"  
 
@app.route('/login')  
def login():  
    return render_template("login.html")  
 
@app.route('/success', methods=["POST"])  
def success():  
    if request.method == "POST":  
        email = request.form['email']  
        password = request.form['password']  
      
    if password == "root":  
        resp = make_response(render_template('success.html'))  
        resp.set_cookie('email', email)  
        return resp  
    else:  
        return redirect(url_for('error'))  
 
@app.route('/viewprofile')  
def profile():  
    email = request.cookies.get('email')  
    resp = make_response(render_template('profile.html', name = email))  
    return resp  
  
if __name__ == "__main__":  
    app.run(debug = True)  