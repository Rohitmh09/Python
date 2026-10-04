import pandas as pd
from helpers import calculate_total, format_currency

#Read data
df = pd.read_csv('data/sales.csv')

totals =[] 

for index, row in df.iterrows():
    total = calculate_total(row['quantity'],row['price'])
    totals.append(total)

print(totals)

# Add totals to our data
df['total'] = totals

print(df)


formatted_t = []

for ind,row in df.iterrows():
    formatted_row = format_currency(row['total'])
    print(f"{row['product']}: {formatted_row}")
    formatted_t.append(formatted_row)

print(formatted_t)

#show grand total

grand_total = df['total'].sum()

grand_total = format_currency(grand_total)
print(f'Grand Total: {grand_total}')