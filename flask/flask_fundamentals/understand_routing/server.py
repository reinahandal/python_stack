from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/dojo')
def dojo():
    return 'Dojo!'   
@app.route('/say/<name>')
def say(name):
    return "Hi " + name + "!"
@app.route('/repeat/<int:times>/<word>')
def repeat(times, word):
    str = ""
    for i in range(0, times):
        str += word + "<br>"
        # str += word + " "
    return str
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."
if __name__=="__main__":
    app.run(debug=True)