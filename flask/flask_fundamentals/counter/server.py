from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def counter():
    session['counter'] = 
@app.route('/users')
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

if __name__ == "__main__":
    app.run(debug=True)