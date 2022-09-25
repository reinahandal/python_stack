from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def counter():
    counter = session.get('counter', 0)
    session['counter'] = counter + 1
    return render_template('index.html', counter = session['counter'])


@app.route('/destroy_session', methods=['POST'])
def destroy():
    session.clear()
    return redirect ("/")


@app.route('/plustwo', methods=['POST'])
def plustwo():
    counter2 = session.get('counter', 0)
    session['counter'] = counter2 + 1
    return redirect ("/")


if __name__ == "__main__":
    app.run(debug=True)