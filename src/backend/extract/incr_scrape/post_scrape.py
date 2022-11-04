import pandas as pd
import time
import datetime
import timedelta
import csv



## This script combines 14day data located in /Data/ with one-day data scraped
## and located in scrapy folder

# inputs: yesterdays 14day price / vol csvs, todays data csv
# output: todays price / vol csvs

os.system("cd ~/OSRS_Item_Investment_Project/")
price_df = pd.read_csv('data/14day_price.csv')
vol_df = pd.read_csv('data/14day_vol.csv')

todays_df = pd.read_csv('code/src/incr_scrape/incr_output.csv')

# extract price and volumes from todays data
price_list = todays_df['price'].tolist()
vol_list = todays_df['volume'].tolist()


# write replace column headers and replace today's column data
current_date = datetime.date.today()
current_date_str = current_date.strftime('%Y/%m/%d')


col_to_remove = (current_date - datetime.timedelta(days=15)).strftime('%Y/%m/%d')
price_df.drop(columns=col_to_remove)
vol_df.drop(columns=col_to_remove)
price_df.insert(1, current_date_str, price_list)
vol_df.insert(1, current_date_str, vol_list)



# upload to csvs (overwrite)
price_df.to_csv('data/14day_price.csv', encoding='utf-8', index=False)
vol_df.to_csv('data/14day_vol.csv', encoding='utf-8', index=False)


