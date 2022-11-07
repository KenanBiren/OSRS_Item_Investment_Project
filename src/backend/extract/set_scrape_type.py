import csv
import time
import datetime

# script start is project folder
# this script queries data folder 14day csvs to see if they are complete and dates match up to yesterday's
# if so, set incr scrape
# else set full
current_date = datetime.date.today()
current_date_str = current_date.strftime('%Y/%m/%d')

updated = False
double_check = False


    # check if a scrape was run yesterday by checking price data
with open("data/14day_price.csv", "r") as f:
    reader = csv.reader(f)
    row = next(reader)
        if row[1] == current_date_str:
            updated = True
    f.close()

if (updated):       # if a scrap was run yesterday, run incremental today

    with open("data/full_or_incr.csv", 'w') as f:
        writer = csv.writer
        writer.writerow(["full (full) or incremental (incr)", "incr"])
        f.close()
        
                    # double check that volume data is also from yesterday
    with open("data/14day_vol.csv", "r") as f:
        reader = csv.reader(f)
        row = next(reader)
            if row[1] == current_date_str:
                double_check = True
        f.close()
else:
    double_check = True     # set today's scrape as incremental
    with open("data/full_or_incr.csv", 'w') as f:
        writer = csv.writer
        writer.writerow(["full (full) or incremental (incr)", "full"])
        f.close()

# if price data is updated but volume data is not, something has gone wrong
if double_check == False:   
    print("Something wrong with set_scrape_type.py or configuration of Docker bind mount")
