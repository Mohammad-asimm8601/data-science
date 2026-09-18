from flask import Flask, render_template

app = Flask(__name__, static_folder='assets')

@app.route("/")
def hello_word():
    return "<p>Hello, World!</p>"

@app.route("/about")
def template():
    return render_template("index.html")

app.run(debug=True)