import boto3
import time
import datetime
import os





def check_files():
    current_date = datetime.date.today()
    cd_str = current_date.strftime('%Y/%m/%d')
    yest_date = current_date - datetime.timedelta(days=2)
    yest_str = yest_date.strftime('%Y/%m/%d')
    tom_date = current_date + datetime.timedelta(days=2)
    tom_str = tom_date.strftime('%Y/%m/%d')

    next_scrape_date = ''

    filePath = "/Users/kenanbiren/Documents/Data"
    last_updated = os.path.getmtime(filePath)
    # Convert seconds since epoch to readable timestamp
    last_updated_str = time.strftime('%Y/%m/%d', time.localtime(last_updated))
    # print("Last Modified Time : ", last_updated_str )
    # print(cd_str)
    # print(yest_str)
    # print(tom_str)


    if last_updated_str != cd_str:
        s3 download status_file and get y/n and next scrape data
        if next_scrape_date ==  tom_str:
            s3 download data folder and replace
        else:
            print("Today's investment analysis has not yet been updated. Using yesterday's.\n")



