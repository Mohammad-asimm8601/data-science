from flask import Flask,render_template, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    #some machine learning model
    data = {"Output":45, "Accuracy":98.55}
    return jsonify(data),200

app.run(debug=True)