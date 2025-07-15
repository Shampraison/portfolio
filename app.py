from flask import Flask,redirect,render_template,url_for
app = Flask(__name__)
@app.route("/")
def index():
    return redirect(url_for('home'))
@app.route("/home")
def home():
    return render_template("Main.html")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():  
    return render_template("contact.html")
@app.route("/project")
def project():
    return render_template("project.html")

if __name__ == '__main__':
    app.run()