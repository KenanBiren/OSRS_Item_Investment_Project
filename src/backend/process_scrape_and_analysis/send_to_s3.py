import boto3
import csv
from s3_upload_dir import uploadDirectory

s3 = boto3('s3')
s3.uploadDirectory('*PATH TO /data/ FOLDER ON EC2', 'BUCKET_NAME')

yest_date = current_date - datetime.timedelta(days=1)
yd_str = yest_date.strftime('%Y/%m/%d, %H:%M')
new_current_week = tom_date.strftime('%Y/%m/%d')
new_next_week = (tom_date + datetime.timedelta(days=7)).strftime('%Y/%m/%d')


#------------------------------------------------------------
# updates status_file 
status_data = []
with open('*PATH TO status_file.csv ON EC2*', mode='r') as outfile:
    reader = csv.reader(outfile)
    for row in reader:
        status_data.append(row)
    outfile.close() 

print(status_data)

if new_week_trigger:
    s3.uploadDirectory('*PATH TO /Week of xxxx/xx/xx/ FOLDER ON EC2', 'BUCKET_NAME')
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
    s3.upload_fileobj(f, "BUCKET_NAME", "status_file.csv")
    outfile.close()
# uploads status_file to S3