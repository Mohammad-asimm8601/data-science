from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = "Asim"
    luckynos = [1, 23, 4, 5, 6, 7, 8]
    footer = "<p> Copyright 2025 </p> | All rights reserved"
    return render_template("index.html", name=name, lucky = luckynos, footer = footer)


app.run(debug=True)
