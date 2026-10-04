import os

import pandas as pd

#Read the CSV file
df = pd.read_csv('data/sales.csv')
print('CSV Data:')
print(df)
print(f'\n Shape: {df.shape}, Rows: {df.shape[0]}, Columns: {df.shape[1]}')


# Quick operation: calculate total for each row

df['total'] = df['quantity'] * df['price']

print(df)

#exists_ok = True use for not show error if already exists
os.makedirs('output',exist_ok=True)

#Save in Different Formats
df.to_json('output/sales_data.json',orient='records',indent=2  )

df.to_csv('output/sales_data.csv',index=False)
df.to_excel('output/sales_data.xlsx',index=False)

print('file save successfully')