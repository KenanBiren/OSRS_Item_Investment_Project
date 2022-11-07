import csv
import time
import datetime
import timedelta
import os

## This script takes a full 14-day scrape output from scrapy and converts it
## to separate 14-day price and volume tables indexed by correct dates

price_data = {}
vol_data = {}   # read scrapy output
with open('full_output.csv', mode='r') as f:
    header = next(f)
    
    reader = csv.reader(f)
    for row in reader:      # reformat scrape output columns from alphabetical
        master_list = []    # to chronological
        price_l = []
        vol_l = []
        sorted_price_list = []
        sorted_vol_list = []
        name = row[15]
        for entry in row:
            master_list.append(entry)
        for i in range(15):
            vol_l.append(row[i])
            price_l.append(row[(i+16)])
        sorted_price_list = [name, price_l[0], price_l[1], price_l[7], price_l[8], price_l[9],
                           price_l[10], price_l[11], price_l[12], price_l[13], price_l[14],
                           price_l[2], price_l[3], price_l[4], price_l[5], price_l[6]]
        sorted_vol_list = [name, vol_l[0], vol_l[1], vol_l[7], vol_l[8], vol_l[9],
                          vol_l[10], vol_l[11], vol_l[12], vol_l[13], vol_l[14],
                          vol_l[2], vol_l[3], vol_l[4], vol_l[5], vol_l[6]]
        price_data[name] = sorted_price_list
        vol_data[name] = sorted_vol_list
    f.close()

current_date = datetime.date.today()

# replace chronological, variable-named columns with chronological dates
# save to separate 14day_price.csv and 14day_vol.csv files
header = ['name']
for d in range(15):
    header.append((current_date - datetime.timedelta(days=d)).strftime('%Y/%m/%d'))
os.system("cd ~/OSRS_Item_Investment_Project/")
with open('data/14day_price.csv', mode='w') as price_file:
    writer = csv.writer(price_file)
    writer.writerow(header)
    for e in price_data:
        writer.writerow(price_data[e])
    price_file.close()


with open('data/14day_vol.csv', mode='w') as vol_file:
    writer = csv.writer(vol_file)
    writer.writerow(header)
    for e in vol_data:
        writer.writerow(vol_data[e])
    vol_file.close()