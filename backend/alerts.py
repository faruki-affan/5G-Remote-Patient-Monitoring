def check_vitals(data):
    alerts = []

    heart_rate = data.get("heart_rate")
    spo2 = data.get("spo2")
    temperature = data.get("temperature")

    if heart_rate is not None:
        if heart_rate < 60:
            alerts.append("LOW HEART RATE")
        elif heart_rate > 100:
            alerts.append("HIGH HEART RATE")

    if spo2 is not None and spo2 < 94:
        alerts.append("LOW OXYGEN LEVEL")

    if temperature is not None and temperature > 38:
        alerts.append("HIGH BODY TEMPERATURE")

    return alerts
