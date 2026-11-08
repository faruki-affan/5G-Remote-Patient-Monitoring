import random
import time
import requests
from datetime import datetime

API_URL = "http://127.0.0.1:5000/api/vitals"

def generate_vitals():
    return {
        "patient_id": "P001",
        "timestamp": datetime.now().isoformat(),
        "heart_rate": random.randint(65, 100),
        "spo2": random.randint(94, 100),
        "temperature": round(random.uniform(36.0, 37.5), 1)
    }

while True:
    vitals = generate_vitals()

    try:
        response = requests.post(API_URL, json=vitals, timeout=5)
        response.raise_for_status()
        print("Sent:", vitals)
    except requests.RequestException as e:
        print("Connection error:", e)

    time.sleep(2)
