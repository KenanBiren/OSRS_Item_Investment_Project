import csv
import os

# run pre_scrape script to choose the correct scrape mode (full or incr) and 
# verify existence of required files if incremental scrape is chosen
os.system('python3 src/backend/extract/set_scrape_type.py')



trigger = '' # read scrape mode
with open("data/full_or_incr.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == 'full':
            trigger = 'full'
        elif: row[1] = 'incr':
            trigger = 'incr'
    f.close()

if trigger == 'full':    # trigger full scrape and corresponding post_scrape.py        
    os.system('python3 src/backend/extract/trigger_scrape.py')
    os.system('cd src/backend/extract/full_scrape/')
    os.system("scrapy crawl full_scrape -o full_output.csv")
    os.system("python3 post_scrape.py")
    os.system("python3 full_scrape_test.py")
    
elif trigger == 'incr':  # trigger full scrape and corresponding post_scrape.py
    os.system('python3 src/backend/extract/trigger_scrape.py')
    os.system('cd src/backend/extract/incr_scrape/')
    os.system("scrapy crawl incr_scrape -o incr_output.csv")
    os.system("python3 post_scrape.py")
    

        # trigger post_scrape verification test
os.system("cd ~/OSRS_Item_Investment_Project/;python3 src/backend/extract/post_scrape_test.py")

        # set next scrape mode as incremental
with open("data/full_or_incr.csv", 'w') as f:
    writer = csv.writer
    writer.writerow(["full (full) or incremental (incr)", "incr"])
    f.close()

