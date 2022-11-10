import csv
import time
import datetime


# This file verifies the existence and last updated time of:
# -14day_price.csv
# -14day_vol.csv
# -full_output.csv or incr_output.csv depending on whether the last scrape 
# was full or incremental

current_date = datetime.date.today()
current_date_str = current_date.strftime('%Y/%m/%d')


price_row_check = False
price_col_check = False
price_val_check = False

vol_row_check = False
vol_col_check = False
vol_val_check = False

scrape_row_check = False
scrape_col_check = False
scrape_val_check = False

check_list = []
trigger = ''

    # check if recent scrape was full or incremental
with open("data/full_or_incr.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] == 'full':
            trigger = 'full'
        elif: row[1] = 'incr':
            trigger = 'incr'
    f.close()




if trigger == 'full':       # read full scrape output
    with open("src/backend/extract/full_scrape/full_output.csv", "r") as f:
        reader = csv.reader(f)
        num_rows = 0
        for row in reader:
            num_rows = num_rows + 1
        if num_rows > 1500:         # check number of rows
            scrape_row_check = True

        reader = csv.reader(f)
        head_row = next(reader)     # check name of header
            if head_row[1] == 'dv_1':
                scrape_col_check = True
        try:
            next_row = next(reader)
            value = next_row[1]     # check for non-null value in 2nd row
                if len(str(value)) > 0:
                    scrape_val_check = True
        except:
            continue
        f.close()
elif: trigger == 'incr':
    with open("src/backend/extract/incr_scrape/incr_output.csv", "r") as f:
        reader = csv.reader(f)
        num_rows = 0
        for row in reader:
            num_rows = num_rows + 1
        if num_rows > 1500:         # check number of rows
            scrape_row_check = True

        reader = csv.reader(f)
        head_row = next(reader)     # check name of header
            if head_row[1] == 'price':
                scrape_col_check = True
        try:
            next_row = next(reader)
            value = next_row[1]     # check for non-null value in 2nd row
                if len(str(value)) > 0:
                    scrape_val_check = True
        except:
            continue
        f.close()




with open("data/14day_price.csv", "r") as f:
    reader = csv.reader(f)
    num_rows = 0
    for row in reader:
        num_rows = num_rows + 1
    if num_rows > 1500:             # check number of rows
        price_row_check = True

    reader = csv.reader(f)
    head_row = next(reader)         # check for correct dates in header
        if head_row[1] == current_date_str:
            price_col_check = True
    try:
        next_row = next(reader)
        value = next_row[1]         # check for non-null value in 2nd row
            if len(str(value)) > 0:
                price_val_check = True
    except:
        continue
    f.close()



with open("data/14day_vol.csv", "r") as f:
    reader = csv.reader(f)
    num_rows = 0
    for row in reader:
        num_rows = num_rows + 1
    if num_rows > 1500:             # check number of rows
        vol_row_check = True

    reader = csv.reader(f)
    head_row = next(reader)         # check for correct dates in header
        if head_row[1] == current_date_str:
            vol_col_check = True
    try:
        next_row = next(reader)
        value = next_row[1]         # check for non-null value in 2nd row
            if len(str(value)) > 0:
                vol_val_check = True
    except:
        continue
    f.close()




check_list = [price_row_check, price_col_check, price_val_check,
                vol_row_check, vol_col_check, vol_val_check,
                scrape_row_check, scrape_col_check, scrape_val_check]

    # send exception if any checks failed
for check in check_list:
    if check == False:
        raise Exception("post_scrape_test.py FAILED")