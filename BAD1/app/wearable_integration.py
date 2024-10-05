def wearable_integration(data):
    # Assuming we integrate some wearable device to monitor user vitals
    vitals_data = {
        "heart_rate": data.get("heart_rate"),
        "temperature": data.get("temperature"),
    }
    return vitals_data
