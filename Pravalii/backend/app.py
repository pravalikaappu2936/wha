from flask import Flask, request, jsonify
from predict_emotion import predict_emotion
from database import init_db, save_alert
from datetime import datetime
import os

app = Flask(__name__)
init_db()

DANGER = ["fear","stress"]

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["audio"]
    filepath = "temp.wav"
    file.save(filepath)

    emotion = predict_emotion(filepath)

    response = {"emotion": emotion, "danger": False}

    if emotion in DANGER:
        response["danger"] = True
        save_alert(emotion, str(datetime.now()))

    return jsonify(response)

app.run(debug=True)
