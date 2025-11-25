import os
import pandas as pd

# Input folder path
input_folder = r"C:\Users\LENOVO\Downloads\NSE_YEARLY_DATA"

# Output file
output_file = r"C:\Users\LENOVO\Downloads\Merged_Output.xlsx"

# Empty list to store all extracted data
merged_data = []

# Loop through all files in folder
for file in os.listdir(input_folder):
    if file.endswith(".xlsx") or file.endswith(".xls"):
        file_path = os.path.join(input_folder, file)

        print(f"Reading: {file}")

        # Read Excel
        df = pd.read_excel(file_path)

        # Extract column D and H by column name or index
        try:
            col_D = df.iloc[:, 3]    # 4th column (D)
            col_H = df.iloc[:, 7]    # 8th column (H)
        except Exception as e:
            print(f"Skipping {file} because of missing columns: {e}")
            continue

        # Create a new temporary DataFrame
        temp_df = pd.DataFrame({
            "F": col_D,   # Save column D data into column F
            "H": col_H    # Save column H data into column H
        })

        merged_data.append(temp_df)

# Combine all extracted data
if merged_data:
    final_df = pd.concat(merged_data, ignore_index=True)
    final_df.to_excel(output_file, index=False)
    print("Data merged successfully!")
    print(f"Output saved to: {output_file}")
else:
    print("No valid Excel files found!")
