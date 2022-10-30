import boto3
import csv
from s3_upload_dir import uploadDirectory



# upload today's /data/ folder to S3
s3 = boto3('s3')
s3.uploadDirectory('/home/ec2-user/OSRS_Item_Investment_App/data/', 'osrs-item-investment-app')

yest_date = current_date - datetime.timedelta(days=1)
yd_str = yest_date.strftime('%Y/%m/%d, %H:%M')
new_current_week = tom_date.strftime('%Y/%m/%d')
new_next_week = (tom_date + datetime.timedelta(days=7)).strftime('%Y/%m/%d')


#------------------------------------------------------------
# read status_file 
status_data = []
with open('/home/ec2-user/OSRS_Item_Investment_App/status_file.csv', mode='r') as outfile:
    reader = csv.reader(outfile)
    for row in reader:
        status_data.append(row)
    outfile.close() 



# update status file weekly fields, reformat week folders, run weekly scrape
if new_week_trigger:
    week = str(status_data[7][1])
    path = '/home/ec2-user/OSRS_Item_Investment_App/Week of ' + week
    s3.uploadDirectory(path, 'osrs-item-investment-app')
    status_data[7][1] = new_current_week
    status_data[8][1] = new_next_week
    curr_wk = 'Week of ' + new_current_week
    nxt_wk = 'Week of ' + new_next_week
    command = 'mkdir ' + curr_wk
    os.system(command)
    command = 'mkdir ' + nxt_wk
    os.system(command)
    os.system('python3 weekly_scrape.py')

# edit analysis end time in status file
status_data[6][1] = datetime.date.today().strftime('%Y/%m/%d, %H:%M')

# upload status_file to S3
with open('/home/ec2-user/OSRS_Item_Investment_App/status_file.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    for row in status_data:
        writer.writerow(row)
    s3.upload_fileobj(f, "osrs-item-investment-app", "status_file.csv")
    outfile.close()



