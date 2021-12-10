from flask import Flask , redirect, url_for
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def home():
    return "Hello, world'!"  
    
@app.route("/about")
def about_page():
    return redirect("/")  

@app.route("/home-page")
@app.route("/home")
def home_page():
    return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True)