import csv


# used to trigger full scrape

with open('/Users/kenanbiren/Documents/raw_links_csv/new_items.csv', mode='w') as f:
    writer = csv.writer(f)
    writer.writerow(['new items?', 'y'])
    f.close()



