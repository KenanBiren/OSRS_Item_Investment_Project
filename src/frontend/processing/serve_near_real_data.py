from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


# This script will use selenium to search "item name" on the ge-tracker website
# to extract Current Price, Current Offer Price, Current Sell Price, Current Tax
# Buying Quantity (1 hour), Selling Quantity (1 hour), Buy/Sell Ratio, Buy Limit.



# inputs: item_name from read_user_input
# outputs: near-real time data from ge-tracker.com





def near_real_data(item):
    fields = ['Current Price', 'Current Offer Price', 'Current Sell Price', 'Current Tax',
                'Buying Quantity (1hr)', 'Selling Quantity (1hr)', 'Buy/Sell Ratio', 'Buy Limit']
    data = {}
    data_list = []
    options = Options()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    link = 'https://www.ge-tracker.com/names/rune'
    # open up website to search
    driver.get(link)
    time.sleep(2)
    # search item_name
    text_area = driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "form-control", " " ))]')
    text_area.send_keys(item)
    text_area.send_keys(Keys.ENTER)
    time.sleep(2)
    # click matching result
    search_results = driver.find_elements(By.CSS_SELECTOR, '.row-item-name')
    for r in search_results:
        if r.text == item:
            link = r.get_attribute('href')
            time.sleep(2)
    # extract data
    driver.get(link)
    fields = driver.find_elements(By.CSS_SELECTOR, '.has-tooltip')
    for d in fields:
        data_list.append(d.text)
    data_list = list(filter(None, data_list))

    ratio = driver.find_element(By.CSS_SELECTOR, 'span.text-profit').text


    limit = driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(4) td~ td').text


    data[fields[0]] = data_list[2]
    data[fields[1]] = data_list[4]
    data[fields[2]] = data_list[6]
    data[fields[3]] = data_list[7]
    data[fields[4]] = data_list[3]
    data[fields[5]] = data_list[5]
    data[fields[6]] = ratio
    data[fields[7]] = limit



    print(data)


    driver.close()
