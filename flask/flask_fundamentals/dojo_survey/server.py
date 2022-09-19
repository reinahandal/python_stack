from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result', methods=['POST'])
def submit_survey():
    form_name = request.form['name']
    form_location = request.form['location']
    form_language = request.form['language']
    form_comment = request.form['comment']
    form_background = request.form['background']
    form_career_service = request.form['career-service']
    form_newsletter = request.form['newsletter']
    form_challenges = request.form['challenges']
    return render_template("show.html", name=form_name, location=form_location, language=form_language, comment=form_comment, background=form_background, career_service=form_career_service, newsletter=form_newsletter, challenges=form_challenges)
if __name__ == "__main__":
    app.run(debug=True)