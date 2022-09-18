from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def eight():
    return render_template("index.html", rows=8, cols=8, color1="black", color2="red")
@app.route('/4')
def four():
    return render_template("index.html", rows=4, cols=8, color1="black", color2="red")
@app.route('/<x>/<y>')
def custom(x,y):
    return render_template("index.html", rows=int(x), cols=int(y), color1="black", color2="red")
@app.route('/<x>/<y>/<color1>/<color2>')
def customcolors(x,y,color1,color2):
    return render_template("index.html", rows=int(x), cols=int(y), color1=color1, color2=color2)
if __name__ == "__main__":
    app.run(debug=True)