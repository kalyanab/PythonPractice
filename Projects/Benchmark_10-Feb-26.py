import requests
import pandas as pd
import os
from datetime import datetime, timedelta
import time

# ===============================
# USER INPUT
# ===============================
INDEX_NAME = "NIFTY 50"
START_DATE = "01-01-2003"
END_DATE = "31-12-2003"

# ===============================
# OUTPUT PATH
# ===============================
OUTPUT_DIR = r"C:\Users\LENOVO\Downloads\Benchmark data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(
    OUTPUT_DIR,
    f"{INDEX_NAME.replace(' ', '_')}_{START_DATE}_to_{END_DATE}.csv"
)

# ===============================
# DATE HANDLING
# ===============================
start = datetime.strptime(START_DATE, "%d-%m-%Y")
end = datetime.strptime(END_DATE, "%d-%m-%Y")

# ===============================
# SESSION + HEADERS
# ===============================
session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com/",
    "Connection": "keep-alive"
}

# Warm-up request (VERY IMPORTANT)
session.get("https://www.nseindia.com", headers=headers, timeout=10)
time.sleep(2)

all_data = []

# ===============================
# LOOP IN 30-DAY CHUNKS
# ===============================
current = start
while current <= end:
    chunk_end = min(current + timedelta(days=30), end)

    from_date = current.strftime("%d-%m-%Y")
    to_date = chunk_end.strftime("%d-%m-%Y")

    url = (
        "https://www.nseindia.com/api/historical/indices"
        f"?indexType={INDEX_NAME.replace(' ', '%20')}"
        f"&from={from_date}&to={to_date}"
    )

    print(f"Fetching: {from_date} → {to_date}")

    try:
        r = session.get(url, headers=headers, timeout=10)
        r.raise_for_status()

        data = r.json().get("data", [])
        all_data.extend(data)

        time.sleep(1.5)  # Anti-block delay

    except Exception as e:
        print("⚠️ Skipped:", e)

    current = chunk_end + timedelta(days=1)

# ===============================
# SAVE DATA
# ===============================
df = pd.DataFrame(all_data)

if df.empty:
    print("❌ No data downloaded.")
else:
    df.drop_duplicates(inplace=True)
    df.to_csv(OUTPUT_FILE, index=False)
    print("\n✅ SUCCESS")
    print("Saved at:", OUTPUT_FILE)
