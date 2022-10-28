This script turns a full 14-day scrape of data into proper format
for the first steps of analysis



triggered by: process_backend.py

next task: daily_analysis.py

inputs: 14-day price and volume data from by scrapy spider 
(full scrape -> scrapy_output.csv -> full_pre_analysis)

outputs: 14day_price.csv, 14day_vol.csv indexed by correct dates

data storage used: EC2 local (Docker /data volume)

test scripts needed: