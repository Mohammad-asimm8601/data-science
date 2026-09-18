from flask import Flask, render_template,flash

app = Flask(__name__)
app.secret_key = 'Queen@123'

@app.route("/")
def hello_world():
    flash("Thank you")
    return render_template("index.html")

@app.route("/about")
def about_page():
    flash("Thanks for visiting")
    return render_template("about.html")

app.run(debug=True)