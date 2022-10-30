import csv


# used to trigger full scrape (run this before very first run)

with open('/home/ec2-user/OSRS_Item_Investment_App/new_items.csv', mode='w') as f:
    writer = csv.writer(f)
    writer.writerow(['new items?', 'y'])
    f.close()



