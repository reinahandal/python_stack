from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def level1():
    return render_template("index.html", times=3, color="skyblue")
@app.route('/play/<times>')
def level2(times):
    return render_template("index.html", times=int(times), color="skyblue")
@app.route('/play/<times>/<color>')
def level3(times,color):
    return render_template("index.html", times=int(times), color=color)
if __name__=="__main__":
    app.run(debug=True)