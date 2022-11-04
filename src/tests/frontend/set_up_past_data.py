import csv
import datetime
import timedelta
import pandas as pd


# this script renames files in /data folder to mimic as if today's analysis
# has not been uploaded


current_date = datetime.date.today()
cd_str = current_date.strftime('%Y/%m/%d')

price_df = pd.read_csv("data/14day_price.csv")
vol_df = pd.read_csv("data/14day_vol.csv")

header = ['name']
for d in range(5,20):
    header.append((current_date - datetime.timedelta(days=d)).strftime('%Y/%m/%d'))

price_df.columns = header
vol_df.columns = header

price_df.to_csv('data/14day_price.csv', encoding='utf-8', index=False)
vol_df.to_csv('data/14day_vol.csv', encoding='utf-8', index=False)



data = []
with open("data/data_summary.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
    f.close()

data[1][0] = cd_str

with open("data/data_summary.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(data)
    f.close()

