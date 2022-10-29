# This script reads from the new_items.csv to see if we need to run a full scrape
# to gather data on the new items or just scrape today's data, then triggers it

# After the scrape is done, this script decides which steps to take to properly
# process and store the scraped data (whether to run process_analysis.py from
# full_scrape or incremental_scrape folder)







# updates status file -> prepares raw data for analysis -> performs analysis -> 
# saves in appropriate places -> updates status file -> 
# updates new_items.csv (saved locally) if needed


import csv
import boto3
import datetime
import os

# process_daily_scrape (runs on ec2)
#
#
# read new_items.csv and record new_items_trigger
# write lines to initially edit status file scrape stats
# trigger scrape
# update status_file analysis running: y/n to start analysis-
# decide pre-analysis process using new_items_trigger
# trigger analysis
# decide post analysis storage targets using new_week_trigger
# edit new_items.csv if needed
# update status_file analysis stats and current week/next week if needed




#-------------------------------------------
new_item_trigger = False
new_week_trigger = False
with open('*PATH TO new_items.csv ON EC2', mode='r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2] == 'y':
            new_item_trigger = True

#----------------------------------------------


## edit scrape started
if new_item_trigger:
    os.system('NAVIGATE TO FULL SPIDER FOLDER; scrapy crawl *SPIDER NAME* -o scrapy_output.csv')
    os.system('COMMAND TO RUN FULL PRE ANALYSIS')
else:
    os.system('NAVIGATE TO INCR SPIDER FOLDER; scrapy crawl *SPIDER NAME* -o scrapy_output.csv')
    os.system('COMMAND TO RUN INCREMENTAL PRE ANALYSIS')

## edit scrape ended and next scrape date in status_file here
#------------------------------------------------------
## function to update status_file analysis running and start time below

status_data = []

with open('*PATH TO status_file.csv ON EC2*', mode='r') as outfile:
    reader = csv.reader(outfile)
    for row in reader:
        status_data.append(row)
    outfile.close()

current_date = datetime.date.today()
cd_str = current_date.strftime('%Y/%m/%d, %H:%M')
tom_date = current_date + datetime.timedelta(days=1)
td_str = tom_date.strftime('%Y/%m/%d, %H:%M')

status_data[4][1] = 'y'
status_data[5][1] = cd_str

if status_data[8][1] == td_str:
    new_week_trigger = True

with open('*PATH TO status_file.csv ON EC2*', mode='w') as outfile:
    writer = csv.writer(outfile)
    for row in status_data:
        writer.writerow(row)
    outfile.close()


# upload to s3

#----------------------------------------
# trigger analysis and upload of files to s3

os.system('command to trigger analysis script')
os.system('command to trigger data_summary script')
os.system('command to save data titled current day to folder titled current week')
os.system('command to trigger send_to_s3 script')
#current_week = status_data[7][1]





#--------------------------------------------------------


current_date = datetime.date.today()
cd_str = current_date.strftime('%Y/%m/%d, %H:%M')
yest_date = current_date - datetime.timedelta(days=1)
yd_str = yest_date.strftime('%Y/%m/%d, %H:%M')
tom_date = current_date + datetime.timedelta(days=1)
td_str = tom_date.strftime('%Y/%m/%d, %H:%M')
new_current_week = tom_date.strftime('%Y/%m/%d')
new_next_week = (tom_date + datetime.timedelta(days=7)).strftime('%Y/%m/%d')


#------------------------------------------------------------
# updates status_file after files have been uploaded to s3
status_data = []
with open('*PATH TO status_file.csv ON EC2*', mode='r') as outfile:
    reader = csv.reader(outfile)
    for row in reader:
        status_data.append(row)
    outfile.close() ## is this block necessary? test

print(status_data)

if new_week_trigger:
    status_data[7][1] = new_current_week
    status_data[8][1] = new_next_week
    os.system('command to make new folder titled new_current_week')
    os.system('command to delete folder titled last current week')
    os.system('command to run weekly link scrape')

status_data[6][1] = datetime.date.today().strftime('%Y/%m/%d, %H:%M')


with open('/Users/kenanbiren/Documents/User Interface Script/status_file.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    for row in status_data:
        writer.writerow(row)
    outfile.close()

# upload status_file to s3

#------------------------------------------------------
# reset new_item_trigger
if new_item_trigger == True:
    with open('/Users/kenanbiren/Documents/User Interface Script/new_items.csv', mode='w') as f:
        writer = csv.writer(f)
        writer.writerow(['new items?', 'n'])
        f.close()






