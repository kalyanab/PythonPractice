import pandas as pd

# ----------- File Path -----------
# Use r"" raw string to avoid escape-character problems
file_path = r"C:\Users\LENOVO\Downloads\RG Sample.xlsx"

# ----------- Read Excel File -----------
df = pd.read_excel(file_path)

# Convert quantities into Buy & Sell columns for clarity
df.loc[df['Type'] == 'Purchase', 'BuyQty'] = df['Quantity']
df.loc[df['Type'] == 'Redemption', 'SellQty'] = df['Quantity'].abs()

# FIFO realized gain/loss calculation
buy_stack = []  # store tuples (qty, price)
realized_gain_list = []

for _, row in df.iterrows():
    if row['Type'] == 'Purchase':
        buy_stack.append([row['BuyQty'], row['Price']])
        realized_gain_list.append(0)
    elif row['Type'] == 'Redemption':
        sell_qty = row['SellQty']
        sell_price = row['Price']
        realized_pl = 0

        # FIFO matching logic
        while sell_qty > 0 and buy_stack:
            buy_qty, buy_price = buy_stack[0]
            if sell_qty >= buy_qty:
                realized_pl += (sell_price - buy_price) * buy_qty
                sell_qty -= buy_qty
                buy_stack.pop(0)
            else:
                realized_pl += (sell_price - buy_price) * sell_qty
                buy_stack[0][0] -= sell_qty
                sell_qty = 0

        realized_gain_list.append(realized_pl)

# Add Realized P/L column
df["Realised G/L"] = realized_gain_list

# ----------- Unrealized Gain/Loss -----------
remaining_qty = sum(qty for qty, _ in buy_stack)

if remaining_qty > 0:
    total_cost = sum(qty * price for qty, price in buy_stack)
    avg_buy_price = total_cost / remaining_qty
    current_price = df.iloc[-1]["Price"]
    unrealized_pl = (current_price - avg_buy_price) * remaining_qty
else:
    unrealized_pl = 0

df["Unrealised G/L"] = unrealized_pl

# ----------- Export Updated Output File -----------
output_path = r"D:\PythonPractice\Projects\RG_Sample_Output.xlsx"
df.to_excel(output_path, index=False)

print("✔ P&L Calculation Completed Successfully!")
print("Output saved to:", output_path)
