from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(f"The email is {email} and the password is {password}")
        return "<b>Thanks for submitting your info</b>"
    return render_template("index.html")

app.run(debug=True)