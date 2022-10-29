import csv
import datetime
import timedelta

# purpose: edit dates on status file as if today's analysis is complete 
# and uploaded

# edit dates on 14day_price.csv, 14day_vol.csv as if they were
# created today

# edit fields in status_file.csv
current_date = datetime.datetime.today()
current_date_str = current_date.strftime('%Y/%m/%d')
tom_date = (current_date + datetime.timedelta(days=1)).strftime('%Y/%m/%d')
cd_w_time = current_date.strftime('%Y/%m/%d, %H:%M')
cd_5_hr_ago = (current_date - datetime.timedelta(hours=5)).strftime('%Y/%m/%d, %H:%M')


data = []
with open("/Users/kenanbiren/Documents/Projects/OSRS_Item_Investment_App/samples/data/status_file.csv", mode='r') as f:
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


with open("/Users/kenanbiren/Documents/Projects/OSRS_Item_Investment_App/samples/data/status_file.csv", mode='w') as f:
    writer = csv.writer(f)
    writer.writerows(data)
    f.close()

