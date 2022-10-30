from selenium import webdriver
import selenium.webdriver.common.by
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

options = Options()
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--user-agent=Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=chrome_options)

with open('/home/ec2-user/OSRS_Item_Investment_App/item_links.csv', mode='r') as f:
    reader = csv.reader(f)
    row_count = sum(1 for row in reader)
    f.close()

def get_all_items():
    cur_pg = 1
    no_pg = 74
    item_list = []
    buylimit_list = []
    dailyvol_list = []

    driver.get('https://prices.runescape.wiki/osrs/all-items/')

    while cur_pg <= no_pg:  ## Extract full item list
        try:  
            cur_pg = cur_pg + 1
            time.sleep(2)
            names = driver.find_elements(by="css selector", value='td:nth-child(2) a')
            for n in names:
                text = n.text
                if '(tablet)' in text:
                    text = text.replace(' (tablet)', '', 1)
                item_list.append(text)

            next_url = driver.find_element(by="xpath",
                                           value='//*[contains(concat( " ", @class, " " ), concat( " ", "btn-secondary", " " )) and (((count(preceding-sibling::*) + 1) = 3) and parent::*)]')
            next_url.click()  ## Click next page
        except:
            break
    return item_list



def get_link(name, position):  # use item name to get link to price data on osrs website. Returns link as string
    time.sleep(2)
    driver.get('https://secure.runescape.com/m=itemdb_oldschool/')
    time.sleep(2)
    text_area = driver.find_element(by="xpath", value='//*[(@id = "item-search")]')
    text_area.send_keys(name)
    text_area.send_keys(selenium.webdriver.Keys.ENTER)
    time.sleep(2)
    results = driver.find_elements(by="css selector", value='.table-item-link')
    link = ''
    for r in results:
        if r.get_attribute('title') == name:
            link = r.get_attribute('href')
    new_row = [name, link]
    with open('/home/ec2-user/OSRS_Item_Investment_App/item_links.csv', 'a+', newline='') as f:
        writer = csv.writer(f)
        f.seek(position)
        writer.writerow(new_row)  ## write row to csv file, record position of cursor
        pos = f.tell()            ## (use cursor position as start for next row)
        f.close()
    return pos


# if scraped item list is longer than current one, save the new one
# and edit new_item.csv to trigger full scrape tomorrow
all_items = get_all_items()
pos = 0
if len(all_items) > row_count:
    with open('/home/ec2-user/OSRS_Item_Investment_App/item_links.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Item', 'Link'])
        position = f.tell()
        f.close()

    for i in range(len(all_items)):
        pos = get_link(all_items[i], position)
        position = pos

    with open('/home/ec2-user/OSRS_Item_Investment_App/new_items.csv', mode='w') as f:
        writer = csv.writer(f)
        writer.writerow(['new items?', 'y'])
        f.close()
else: 
    with open('/home/ec2-user/OSRS_Item_Investment_App/new_items.csv', mode='w') as f:
        writer = csv.writer(f)
        writer.writerow(['new items?', 'n'])
        f.close()

driver.close()
