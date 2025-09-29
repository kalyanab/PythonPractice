import os
import urllib.request
import zipfile
from datetime import datetime, timedelta

def download_bse_bhavcopy(start_date, end_date, save_folder="bhavcopies"):
    """
    Downloads and unzips BSE Bhavcopy ZIPs for a given date range using only built-in libraries.
    Skips Saturdays and Sundays automatically and uses headers to avoid 403 errors.
    Extracts ZIP contents directly into the save_folder (no sub-folders).
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

        # Date format for file
        date_str = current.strftime("%d%m%y")
        url = f"https://www.bseindia.com/download/BhavCopy/Equity/EQ_ISINCODE_{date_str}.zip"
        zip_path = os.path.join(save_folder, f"BhavCopy_{date_str}.zip")

        try:
            # Add browser-like headers
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/120.0 Safari/537.36"
            }
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response, open(zip_path, "wb") as out_file:
                out_file.write(response.read())

            # Check file size (skip invalid/empty files)
            if os.path.getsize(zip_path) < 500:
                print(f"❌ Not available (holiday?): {date_str}")
                os.remove(zip_path)
            else:
                print(f"✅ Downloaded: {zip_path}")

                # Unzip directly into save_folder
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(save_folder)
                    print(f"📂 Extracted into: {save_folder}")

                # Optional: delete zip after extracting
                os.remove(zip_path)

        except Exception as e:
            print(f"⚠️ Error for {date_str}: {e}")

        current += timedelta(days=1)

# Example usage
download_bse_bhavcopy("2022-01-01", "2022-12-31")
