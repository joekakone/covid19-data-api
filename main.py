from flask import Flask, jsonify
from utils.data import get_data

app = Flask(__name__)

@app.route("/")
def home():
    ecowas, update_date = get_data()
    data = {"last_update": update_date, "data": ecowas}
    return jsonify(data)
