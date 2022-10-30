import csv
import datetime
import timedelta
import os
# This script edits dates on status file and last update time of /data/ to test 
# app as if today's analysis is complete and uploaded


# make an edit in /data/ so that last updated date is today
os.system("cd /Users/kenanbiren/OSRS_Item_Investment_App/data/")
os.sysem("mkdir dummy")
os.system("rmdir dummy")


current_date = datetime.datetime.today()
current_date_str = current_date.strftime('%Y/%m/%d')
tom_date = (current_date + datetime.timedelta(days=1)).strftime('%Y/%m/%d')
cd_w_time = current_date.strftime('%Y/%m/%d, %H:%M')
cd_5_hr_ago = (current_date - datetime.timedelta(hours=5)).strftime('%Y/%m/%d, %H:%M')
data = []

# edit fields in status_file.csv
with open("/Users/kenanbiren/OSRS_Item_Investment_App/status_file.csv", mode='r') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
    f.close()



data[0][1] = cd_5_hr_ago
data[1][1] = cd_5_hr_ago
data[2][1] = cd_5_hr_ago
data[3][1] = tom_date
data[4][1] = 'n'
data[5][1] = cd_w_time
data[6][1] = cd_w_time
data[8][1] = current_date_str


with open("/Users/kenanbiren/OSRS_Item_Investment_App/data/status_file.csv", mode='w') as f:
    writer = csv.writer(f)
    writer.writerows(data)
    f.close()

