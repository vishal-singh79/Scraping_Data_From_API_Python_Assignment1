import pandas as pd
from itertools import permutations

from stations import load_stations
from api_client import fetch_route
from extractor import extract_data
from db_handler_sqlite import create_table, insert_route

def main():
    # Create DB & table
    create_table()

    stations = load_stations()
    station_codes = list(stations.keys())

    results = []

    for source, destination in permutations(station_codes, 2):
        print(f"Fetching: {source} → {destination}")

        response = fetch_route(source, destination)
        extracted = extract_data(response)

        if extracted:
            extracted["source_code"] = source
            extracted["destination_code"] = destination

            # Insert into SQLite
            insert_route(extracted)

            results.append(extracted)

  
    df = pd.DataFrame(results)
    df.to_csv("data/output.csv", index=False)

    print("Data extraction + SQLite insertion completed!")

if __name__ == "__main__":
    main()
