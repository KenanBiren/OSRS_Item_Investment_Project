import boto3
import time
import datetime
import os
from s3_download_dir import download_s3_folder

# This script checks the /data/ folder to see when it was last updated. If it
# was updated today, do nothing. If it needs an update, attempt to download
# new /data/ from S3


def check_files():
    current_date = datetime.date.today()
    cd_str = current_date.strftime('%Y/%m/%d')
    yest_date = current_date - datetime.timedelta(days=2)
    yest_str = yest_date.strftime('%Y/%m/%d')
    tom_date = current_date + datetime.timedelta(days=2)
    tom_str = tom_date.strftime('%Y/%m/%d')

    next_scrape_date = ''

    filePath = "/Users/kenanbiren/OSRS_Item_Investment_App/data/"
    last_updated = os.path.getmtime(filePath)
    # convert seconds since epoch to readable timestamp
    last_updated_str = time.strftime('%Y/%m/%d', time.localtime(last_updated))
    # print("Last Modified Time : ", last_updated_str )
    # print(cd_str)
    # print(yest_str)
    # print(tom_str)


    if last_updated_str != cd_str:
        s3 download status_file and get y/n and next scrape date
        if next_scrape_date ==  tom_str:
            download_s3_folder('osrs-item-investment-app', 'data', '/Users/kenanbiren/OSRS_Item_Investment_App/data/stage/')
            # sanity check for file content size here
            os.system('rm -r /data/;mv /Users/kenanbiren/OSRS_Item_Investment_App/data/stage/ /Users/kenanbiren/OSRS_Item_Investment_App/data/')
            # sanity check for dates in data here
        else:
            print("Today's investment analysis has not yet been updated. Using yesterday's.\n")



