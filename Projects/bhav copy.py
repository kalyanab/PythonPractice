import requests
import os
from datetime import datetime, timedelta

def download_bse_bhavcopy(start_date, end_date, save_folder="bhavcopies"):
    """
    Downloads BSE Bhavcopy CSVs for a given date range.

    :param start_date: str, format "YYYY-MM-DD"
    :param end_date: str, format "YYYY-MM-DD"
    :param save_folder: folder to save files
    """
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Convert string dates to datetime
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    current = start
    while current <= end:
        date_str = current.strftime("%Y%m%d")
        url = f"https://www.bseindia.com/download/BhavCopy/Equity/BhavCopy_BSE_CM_0_0_0_{date_str}_F_0000.CSV"
        filename = os.path.join(save_folder, f"BhavCopy_{date_str}.csv")

        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200 and len(response.content) > 500:  # ensure valid file
                with open(filename, "wb") as f:
                    f.write(response.content)
                print(f"✅ Downloaded: {filename}")
            else:
                print(f"❌ Not available: {date_str}")
        except Exception as e:
            print(f"⚠️ Error for {date_str}: {e}")

        current += timedelta(days=1)

# Example usage:
download_bse_bhavcopy("2025-09-15", "2025-09-19")
