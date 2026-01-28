# Mumbai Metro Route Scraper – API Data Pipeline

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

---

## Overview

This project is a **production-grade data pipeline** that automatically scrapes Mumbai Metro route information from the MMRCL (Mumbai Metropolitan Region Development Authority) API. It retrieves journey details between all station pairs, cleans the data, validates it, and stores it in both **SQLite database** and **CSV format** for easy analysis.

### What Does It Do?

1. **Fetches Route Data**: Queries the MMRCL API for journey routes between all pairs of metro stations
2. **Extracts Information**: Parses API responses to extract:
   - Source and destination station names & codes
   - Fare amounts
   - Total distance
   - Intermediate stations along the route
   - Station count between source and destination
3. **Stores Data Securely**: Saves all extracted data in two formats:
   - **SQLite Database** (`mumbai_metro.db`) - for structured querying
   - **CSV File** (`output.csv`) - for spreadsheet analysis
4. **Handles Errors Gracefully**: Manages API failures and invalid responses without crashing

### Project Flow

```
┌─────────────────────┐
│  Load Station Data  │  (from stations.json)
│  (27 metro stations)│
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────┐
│ Generate All Routes     │  (permutations: A→B, B→A, etc.)
│ (source → destination)  │
└──────────┬──────────────┘
           │
           ▼
┌──────────────────────┐
│  Fetch from MMRCL    │  (HTTP requests with retry logic)
│  API for Each Route  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Extract & Clean     │  (Parse stations, fare, distance)
│  Route Information   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Store in SQLite DB  │  (Duplicate prevention with UNIQUE constraint)
│  + Export to CSV     │
└──────────────────────┘
```

---

## How It Works - Step by Step

### 1. **Station Configuration**
Loads a predefined list of 27 Mumbai Metro stations from [`data/stations.json`](data/stations.json) with their codes (e.g., `CSTM` → Chhatrapati Shivaji Maharaj Terminus).

### 2. **API Requests**
Using [`src/api_client.py`](src/api_client.py), the script makes HTTP requests to:
```
https://portal.mmrcl.com/en/api/v2/journey-route/{SOURCE}/{DESTINATION}/station/station/least-distance/{DATE}/one_way/
```

### 3. **Data Extraction**
[`src/extractor.py`](src/extractor.py) processes the API response and extracts:
- Journey fare
- Total distance
- All intermediate stations
- Station count between source and destination

### 4. **Data Storage**

**SQLite Database** ([`src/db_handler_sqlite.py`](src/db_handler_sqlite.py)):
- Creates a `journey_routes` table with proper schema
- Stores routes with UNIQUE constraint (prevents duplicate entries)
- Includes timestamp for tracking when data was inserted

**CSV Export** ([`src/main.py`](src/main.py)):
- Exports all routes to `data/output.csv`
- Easy to open in Excel, Google Sheets, or data analysis tools

---

##  Key Features

- **Automated API Scraping**: Fetches data for all station-pair combinations
- **Robust Error Handling**: Gracefully handles API failures and malformed responses
- **Data Validation**: Extracts only valid, complete route information
- **Dual Storage**: Saves to both SQLite (relational) and CSV (spreadsheet-friendly)
- **Duplicate Prevention**: UNIQUE constraints prevent data duplication
- **Modular Design**: Clean separation of concerns (API, extraction, storage)
- **Scalable Structure**: Easy to extend or modify for other APIs

---

## 🛠 Tech Stack
- **Python 3**
- **Requests**
- **Pandas**
- **SQLite**
- **Logging**


---

## Prerequisites

- **Python 3.8 or higher**
- **pip** (Python package manager)
- **Internet connection** (to fetch from MMRCL API)

### Check Versions
```bash
python --version
pip --version
```

---

## Quick Start Guide

### Step 1: Clone or Download the Project
```bash
cd /path/to/Pythonassignment1API
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it (Linux/Mac)
source venv/bin/activate

# Or activate it (Windows)
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**Dependencies installed:**
- `requests` - For API calls
- `pandas` - For CSV handling
- `sqlite3` - Already included with Python

### Step 4: Configure API Settings (Optional)

Edit [`src/config.py`](src/config.py) to change:
- `BASE_URL` - API endpoint
- `DATE` - Journey date for the query
- `TRAVEL_TYPE` - Trip type (one_way, return, etc.)
- `HEADERS` - Custom headers for the API request

Current config:
```python
BASE_URL = "https://portal.mmrcl.com/en/api/v2/journey-route"
DATE = "2026-01-26"
TRAVEL_TYPE = "one_way"
```

### Step 5: Run the Project
```bash
cd src
python main.py
```

### What Gets Generated:
```
data/
├── mumbai_metro.db          # SQLite database with all routes
├── output.csv               # Spreadsheet-friendly CSV file
└── stations.json            # Station reference data
```

---


### CSV File (`output.csv`)
```
source | destination | fare | total_distance | intermediate_station_count | stations_between
CSTM,CHGM,40,2.2 km,3,Girgaon -> Kalbadevi -> Hutatma Chowk
CHGM,CSTM,40,2.2 km,3,Girgaon -> Kalbadevi -> Hutatma Chowk
...
```

---

## Project Structure

```
Pythonassignment1API/
├── README.md                      # This file
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore rules
├── data/
│   ├── stations.json              # Station reference data
│   ├── mumbai_metro.db            # Generated SQLite database
│   └── output.csv                 # Generated CSV export
└── src/
    ├── main.py                    # Main entry point
    ├── api_client.py              # API request handler
    ├── extractor.py               # Data extraction logic
    ├── db_handler_sqlite.py        # Database operations
    ├── stations.py                # Station loader
    ├── config.py                  # Configuration settings
    └── __pycache__/               # Python cache (auto-generated)
```

---




**Happy Scraping!**

