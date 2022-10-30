import csv
import boto3
import datetime
import os
from s3_upload_dir import uploadDirectory


# This script reads from the new_items.csv to see if we need to run a full scrape
# to gather data on the new items or just scrape today's data, then triggers it

# After the scrape is done, this script decides which steps to take to properly
# process and store the scraped data (whether to run process_analysis.py from
# full_scrape or incremental_scrape folder)



# read new_items.csv to get new_items_trigger
# trigger scrape
# update status_file analysis running: y/n, scrape stats, and analysis start time
# decide / run pre-analysis process from new_items_trigger
# trigger analysis
# trigger send_to_s3, which handles data transfer
# edit new_items.csv to 'n' if needed





#-------------------------------------------
new_item_trigger = False
new_week_trigger = False
with open('/home/ec2-user/OSRS_Item_Investment_App/new_items.csv', mode='r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2] == 'y':
            new_item_trigger = True

#----------------------------------------------
# record "scrape time started" here
if new_item_trigger:
    os.system('cd /home/ec2-user/OSRS_Item_Investment_App/scripts/full_scrape/full_scrape/; scrapy crawl full_scrape -o scrapy_output.csv')
    os.system('cd /home/ec2-user/OSRS_Item_Investment_App/scripts/;python3 full_pre_analysis.py')
else:
    os.system('/home/ec2-user/OSRS_Item_Investment_App/scripts/incr_scrape/incr_scrape/ ; scrapy crawl incr_scrape -o scrapy_output.csv')
    os.system('cd /home/ec2-user/OSRS_Item_Investment_App/scripts/;python3 incr_pre_analysis.py')


#------------------------------------------------------
# update status_file analysis running y/n and start time

status_data = []

with open('/home/ec2-user/OSRS_Item_Investment_App/status_file.csv', mode='r') as outfile:
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


# edit and upload status file to s3
with open('/home/ec2-user/OSRS_Item_Investment_App/status_file.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    for row in status_data:
        writer.writerow(row)
    s3.upload_fileobj(outfile, "osrs-item-investment-app", "status_file.csv")
    outfile.close()




#----------------------------------------
# trigger analysis and upload of files to s3
curr_wk = str(status_data[7][1])
command = 'cp /home/ec2-user/OSRS_Item_Investment_App/data/ /home/ec2-user/OSRS_Item_Investment_App/Week of ' 
+ curr_wk
os.system('python3 daily_analysis.py')
os.system('python3 create_data_summary.py')
os.system(command)
os.system('python3 send_to_s3.py')




# reset new_items.csv
if (new_item_trigger):
    with open("/home/ec2-user/OSRS_Item_Investment_App/new_items.csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['new items?', 'n'])
        f.close()








