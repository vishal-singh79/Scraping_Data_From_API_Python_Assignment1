def extract_data(api_response):
    if not api_response:
        return None

    all_stations = []

    for route in api_response.get("route", []):
        for station in route.get("path", []):
            all_stations.append(station["name"])

    intermediate_stations = all_stations[1:-1]

    return {
        "source": api_response.get("from"),
        "destination": api_response.get("to"),
        "fare": api_response.get("fare"),
        "total_distance": api_response.get("distance"),
        "intermediate_station_count": len(intermediate_stations),
        "stations_between": " -> ".join(intermediate_stations)
    }
