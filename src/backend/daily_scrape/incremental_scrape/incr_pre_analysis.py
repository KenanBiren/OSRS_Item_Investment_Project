
import pandas as pd
import time
import timedelta
import datetime
import csv



## This script combines 14day data located in /Data/ with one-day data scraped
## and located in scrapy folder

# inputs: yesterdays 14day price / vol csvs, todays data csv
# output: todays price / vol csvs


price_df = pd.read_csv('/Users/kenanbiren/Documents/Data/yest_data/14day_price.csv')
vol_df = pd.read_csv('/Users/kenanbiren/Documents/Data/yest_data/14day_vol.csv')





todays_df = pd.read_csv('/Users/kenanbiren/Documents/Data/yest_data/test_data.csv')


price_list = todays_df['price'].tolist()
vol_list = todays_df['volume'].tolist()



current_date = datetime.date.today()
header = ['name']
for d in range(15):
    header.append((current_date - datetime.timedelta(days=d)).strftime('%Y/%m/%d'))

with open('/Users/kenanbiren/Documents/Data/14day_price.csv', mode='w') as price_file:
    writer = csv.writer(price_file)
    writer.writerow(header)

    price_file.close()


with open('/Users/kenanbiren/Documents/Data/14day_vol.csv', mode='w') as vol_file:
    writer = csv.writer(vol_file)
    writer.writerow(header)

    vol_file.close()

col_to_remove = (current_date - datetime.timedelta(days=15)).strftime('%Y/%m/%d')
price_df.drop(columns=col_to_remove)
vol_df.drop(columns=col_to_remove)
current_date_str = current_date.strftime('%Y/%m/%d')
price_df.insert(1, current_date_str, price_list)
vol_df.insert(1, current_date_str, vol_list)

price_df.to_csv('/Users/kenanbiren/Documents/Data/14day_price.csv', encoding='utf-8', index=False)
vol_df.to_csv('/Users/kenanbiren/Documents/Data/14day_vol.csv', encoding='utf-8', index=False)


