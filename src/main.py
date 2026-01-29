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

    # Generate source → destination pairs 
    for source, destination in permutations(station_codes, 2):

        # EXTRA SAFETY CHECK (even though permutations already avoids same)
        if source == destination:
            continue

        print(f"Fetching route: {source} → {destination}")

        response = fetch_route(source, destination)
        extracted = extract_data(response)

        if not extracted:
            print(f"No data found for {source} → {destination}")
            continue

        # Add station codes
        extracted["source_code"] = source
        extracted["destination_code"] = destination

        # Insert into SQLite immediately
        insert_route(extracted)

        # Store for CSV output
        results.append(extracted)

    # Save CSV only after all insertions are done
    if results:
        df = pd.DataFrame(results)
        df.to_csv("data/output.csv", index=False)
        print("CSV saved to data/output.csv")

    print("Data extraction and SQLite insertion completed successfully!")


if __name__ == "__main__":
    main()
