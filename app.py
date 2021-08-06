# coding : utf-8

from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin
from utils.data import get_data

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": "*" # Allow requests from exterior
    }
})

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/api/ecowas")
@cross_origin()
def get_ecowas():
    ecowas, update_date = get_data()
    data = {"last_update": update_date, "data": ecowas}
    return jsonify(data)

@app.route("/api/world")
@cross_origin()
def get_world():
    ecowas, update_date = get_data(filter=False)
    data = {"last_update": update_date, "data": ecowas}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
