This script turns a one day scrape of data and combines it with
past data located locally on EC2 into proper format for
the first steps of analysis



triggered by: process_backend.py

next task: daily_analysis.py

inputs: today's price and volume data from by scrapy spider 
(incremental scrape -> scrapy_output.csv -> incr_pre_analysis)

outputs: 14day_price.csv, 14day_vol.csv indexed by correct dates

data storage used: EC2 local (Docker /data volume)

test scripts needed: