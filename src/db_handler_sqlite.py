import sqlite3
import os

DB_PATH = "data/mumbai_metro.db"

def get_connection():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS journey_routes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            source_code TEXT,
            source_name TEXT,

            destination_code TEXT,
            destination_name TEXT,

            fare INTEGER,
            total_distance TEXT,

            intermediate_station_count INTEGER,
            stations_between TEXT,

            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

            UNIQUE (source_code, destination_code)
        )
    """)

    conn.commit()
    conn.close()

def insert_route(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO journey_routes (
            source_code, source_name,
            destination_code, destination_name,
            fare, total_distance,
            intermediate_station_count, stations_between
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["source_code"],
        data["source"],
        data["destination_code"],
        data["destination"],
        data["fare"],
        data["total_distance"],
        data["intermediate_station_count"],
        data["stations_between"]
    ))

    conn.commit()
    conn.close()
