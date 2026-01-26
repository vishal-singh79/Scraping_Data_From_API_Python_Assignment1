import requests
from config import BASE_URL, DATE, TRAVEL_TYPE, HEADERS

def fetch_route(source_code, destination_code):
    url = f"{BASE_URL}/{source_code}/{destination_code}/station/station/least-distance/{DATE}/{TRAVEL_TYPE}/"
    
    response = requests.get(url, headers=HEADERS, timeout=10)
    
    if response.status_code != 200:
        return None
    
    return response.json()
