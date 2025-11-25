import requests
import pandas as pd
from datetime import datetime, timedelta
import os
import calendar

# ---------------------------------------------------------
# CONFIG: SET YOUR DATE RANGE HERE (DD-MM-YYYY)
# ---------------------------------------------------------
START_DATE = "01-04-2005"     # DD-MM-YYYY
END_DATE   = "31-12-2018"     # DD-MM-YYYY
SAVE_FOLDER = r"D:\NSE_YEARLY_DATA"
INDEX_NAME = "NIFTY SMALLCAP 250"
# ---------------------------------------------------------

# Ensure folder exists
os.makedirs(SAVE_FOLDER, exist_ok=True)

# NSE session & headers
session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*",
    "Referer": "https://www.nseindia.com/"
}
session.get("https://www.nseindia.com", headers=headers)

def fetch_data(from_date, to_date):
    """Fetch NSE monthly data."""
    url = (
        "https://www.nseindia.com/api/historicalOR/indicesHistory?"
        f"indexType={INDEX_NAME.replace(' ', '%20')}"
        f"&from={from_date}&to={to_date}"
    )
    print(f"\n📥 Downloading {from_date} → {to_date}")

    try:
        r = session.get(url, headers=headers)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        print("❌ Error:", e)
        return None

    if "data" not in data or not data["data"]:
        print("⚠ No data returned.")
        return None

    return pd.DataFrame(data["data"])

def month_ranges(start_dt, end_dt):
    """Generate month-wise date splits between two dates."""
    current = start_dt.replace(day=1)

    while current <= end_dt:
        year, month = current.year, current.month
        last_day = calendar.monthrange(year, month)[1]

        first_date = current
        last_date = datetime(year, month, last_day)

        # Trim inside range
        if first_date < start_dt:
            first_date = start_dt
        if last_date > end_dt:
            last_date = end_dt

        yield first_date.strftime("%d-%m-%Y"), last_date.strftime("%d-%m-%Y")

        # Move to next month
        if month == 12:
            current = datetime(year + 1, 1, 1)
        else:
            current = datetime(year, month + 1, 1)


# ---------------------------------------------------------
# MAIN EXECUTION
# ---------------------------------------------------------

start_dt = datetime.strptime(START_DATE, "%d-%m-%Y")
end_dt   = datetime.strptime(END_DATE, "%d-%m-%Y")

print(f"➡ Fetching data from {START_DATE} to {END_DATE}")

# Loop monthly
for from_d, to_d in month_ranges(start_dt, end_dt):
    df = fetch_data(from_d, to_d)
    if df is None:
        continue

    file_name = f"{INDEX_NAME.replace(' ', '_')}_{from_d}_to_{to_d}.csv"
    file_path = os.path.join(SAVE_FOLDER, file_name)

    df.to_csv(file_path, index=False)
    print(f"✅ Saved: {file_path}")

print("\n🎉 Completed downloading all data!")
