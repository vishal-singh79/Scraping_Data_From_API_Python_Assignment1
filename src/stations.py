import json

def load_stations(filepath="data/stations.json"):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)
