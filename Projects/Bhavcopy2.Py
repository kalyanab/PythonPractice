import os
import urllib.request
from datetime import datetime, timedelta

def download_bse_bhavcopy(start_date, end_date, save_folder="bhavcopies"):
    """
    Downloads BSE Bhavcopy CSVs for a given date range using only built-in libraries.
    Skips Saturdays and Sundays automatically and uses headers to avoid 403 errors.
    """
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    current = start
    while current <= end:
        # Skip weekends
        if current.weekday() in (5, 6):
            print(f"⏩ Skipping weekend: {current.strftime('%Y-%m-%d')}")
            current += timedelta(days=1)
            continue

        date_str = current.strftime("%Y%m%d")
        url = f"https://www.bseindia.com/download/BhavCopy/Equity/BhavCopy_BSE_CM_0_0_0_{date_str}_F_0000.CSV"
        filename = os.path.join(save_folder, f"BhavCopy_{date_str}.csv")

        try:
            # Add browser-like headers
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/120.0 Safari/537.36"
            }
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response, open(filename, "wb") as out_file:
                out_file.write(response.read())

            # Check file size (skip invalid/empty files)
            if os.path.getsize(filename) < 500:
                print(f"❌ Not available (holiday?): {date_str}")
                os.remove(filename)
            else:
                print(f"✅ Downloaded: {filename}")
        except Exception as e:
            print(f"⚠️ Error for {date_str}: {e}")

        current += timedelta(days=1)

# Example usage
download_bse_bhavcopy("2024-01-01", "2024-12-31")
