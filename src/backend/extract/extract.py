import csv
import os

trigger = ''
with open("data/full_or_incr.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == 'full':
            trigger = 'full'
        elif: row[1] = 'incr':
            trigger = 'incr'
        #     ......error
    f.close()

if trigger == 'full':            
    os.system('cd src/extract/full_scrape/')
    os.system("scrapy crawl full_scrape -o full_output.csv")
    # add unit test here
    os.system("python3 post_scrape.py")
    # add unit test here
else:
    os.system('cd src/extract/incr_scrape/')
    os.system("scrapy crawl incr_scrape -o incr_output.csv")
    # add unit test here
    os.system("python3 post_scrape.py")
    # add unit test here


with open("data/full_or_incr.csv", 'w') as f:
    writer = csv.writer
    writer.writerow(["full (full) or incremental (incr)", "incr"])
    f.close()

