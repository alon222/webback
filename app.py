from flask import Flask , redirect, url_for,render_template
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def home():
    return render_template('cv.html')

@app.route("/contact-me")
def contact():
    return render_template('cv1.html')

@app.route("/assignment8")
def assignment8():
    ishobbies=True
    hobbies=['swimming','running','tennies','sleeping']
    music=['pop','ישראלי','Country']
    return render_template('assignment8.html',user_name='David',ishobbies=ishobbies,hobbies=hobbies,music=music)

@app.route("/home-page")
@app.route("/home")
def home_page():
    return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True)