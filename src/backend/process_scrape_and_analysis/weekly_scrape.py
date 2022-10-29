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

with open('/Users/kenanbiren/Documents/raw_links_csv/item_links.csv', mode='r') as f:
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

    while cur_pg <= no_pg:  ## Extract full item list with associated buy
        try:  ## limits and most recent daily volume
            cur_pg = cur_pg + 1
            time.sleep(2)
            names = driver.find_elements(by="css selector", value='td:nth-child(2) a')
            for n in names:
                text = n.text
                if '(tablet)' in text:
                    text = text.replace(' (tablet)', '', 1)
                item_list.append(text)

            # buylimit = driver.find_elements(by="css selector", value='td:nth-child(3)')
            # for b in buylimit:
            #     b1 = b.text.replace(',', '')
            #     if b1 != '':
            #         if b1 == 'Unknown':
            #             buylimit_list.append(int(1))
            #         else:
            #             buylimit_list.append(int(b1))
            #
            # dailyvol = driver.find_elements(by="css selector", value='td:nth-child(10)')
            # for d in dailyvol:
            #     d1 = d.text.replace(',', '')
            #     if d1 != 'Unknown':
            #         dailyvol_list.append(int(d1))
            #     else:
            #         dailyvol_list.append(int(0))
            #
            next_url = driver.find_element(by="xpath",
                                           value='//*[contains(concat( " ", @class, " " ), concat( " ", "btn-secondary", " " )) and (((count(preceding-sibling::*) + 1) = 3) and parent::*)]')
            next_url.click()  ## Click next page
        except:
            break
    return item_list
    # Code to only inlcude items where daily volume is not greater than 10x buy limit

    # for i in range(len(item_list)):
    #     if daily_vol_list[i] > 10 * buylimit_list[i]:
    #         final_item_list.append(item_list[i])
    #         final_dailyvol_list.append(dailyvol_list[i])
    #         final_buylimit_list.append(buylimit_list[i])

    #return [item_list, dailyvol_list, buylimit_list]


def get_link(name, position):  ##Use item name to get link to price data on osrs website. Returns link as string
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
    with open('/Users/kenanbiren/Documents/Link_List/item_links.csv', 'a+', newline='') as f:
        writer = csv.writer(f)
        f.seek(position)
        writer.writerow(new_row)  ## Write row to csv file, record position of cursor
        pos = f.tell()  ## (use cursor position as start for next row)
        f.close()
    return pos



all_items = get_all_items()
pos = 0
if len(all_items) > row_count:
    with open('/Users/kenanbiren/Documents/raw_links_csv/item_links.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Item', 'Link'])
        position = f.tell()
        f.close()

    for i in range(len(all_items)):
        pos = get_link(all_items[i], position)
        position = pos

    with open('/Users/kenanbiren/Documents/raw_links_csv/new_items.csv', mode='w') as f:
        writer = csv.writer(f)
        writer.writerow(['new items?', 'y'])
        f.close()
else: 
    with open('/Users/kenanbiren/Documents/raw_links_csv/new_items.csv', mode='w') as f:
        writer = csv.writer(f)
        writer.writerow(['new items?', 'n'])
        f.close()

driver.close()
