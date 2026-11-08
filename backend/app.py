from datetime import datetime
from alerts import check_vitals
from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime

app = Flask(__name__)

readings = []

@app.route("/")
def dashboard():
    return send_from_directory("../dashboard", "index.html")

@app.route("/api/vitals", methods=["POST"])
def receive_vitals():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    required = ["patient_id", "heart_rate", "spo2", "temperature"]
    if any(field not in data for field in required):
        return jsonify({"error": "Missing fields"}), 400

    data["received_at"] = datetime.now().isoformat()
    data["alerts"] = check_vitals(data)
    readings.append(data)
    return jsonify({"message": "Vitals received"}), 201


@app.route("/api/vitals", methods=["GET"])
def get_vitals():
    return jsonify(readings[-100:])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
