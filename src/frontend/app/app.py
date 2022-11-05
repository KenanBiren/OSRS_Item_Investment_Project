import matplotlib
matplotlib.use("AGG")
import matplotlib.pyplot as plt
import csv
import time
import datetime
import timedelta
import os
import pandas as pd
from tabulate import tabulate





def read_input():
    item_list = []
    print(os.getcwd())
    print(os.listdir())
                        # get current item masterlist
    with open('data/14day_price.csv', mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            item_list.append(row[0])

                # prompt input
    while(True):
        item = input('What item would you like to search?\n')
        item = item.lower()
        item = item.capitalize()
        print('item: ' + item)
        t = 0
        if item in item_list:
            print('item found! item: ')
            return item
            break
        else:                       # invalid input -> suggestion
            print('Invalid input, please try again. Did you mean:')
            item_split = item.split()
            longest_word = max(item_split, key=len)
            for i in range(len(item_list)):
                if longest_word in item_list[i]:
                    print(item_list[i])
                    t = t + 1
                if t == 5:
                    break


item_name = read_input()


def check_files():
    current_date = datetime.date.today()
    cd_str = current_date.strftime('%Y/%m/%d')
    yest_date = current_date - datetime.timedelta(days=2)
    yest_str = yest_date.strftime('%Y/%m/%d')
    tom_date = current_date + datetime.timedelta(days=2)
    tom_str = tom_date.strftime('%Y/%m/%d')

    

    filePath = "data/"
    last_updated = os.path.getmtime(filePath)
    # convert seconds since epoch to readable timestamp
    last_updated_str = time.strftime('%Y/%m/%d', time.localtime(last_updated))
   


    if last_updated_str != cd_str:
        print("Today's daily investment analysis has not yet been updated. Using yesterday's.\n")








def analysis_data(item_name):
    working_df = {}

    price_df = pd.read_csv('data/14day_price.csv')
    vol_df = pd.read_csv('data/14day_vol.csv')
    analysis_df = pd.read_csv('data/analysis_table.csv')
    summary_df = pd.read_csv('data/data_summary.csv')

    print(summary_df)

    #------------------------------------------------------------
    # print a two-y-axis graph showing price and volume data
    data = []
    x_list = []
    price_row_df = price_df.loc[price_df['name'] == item_name]
    vol_row_df = vol_df.loc[vol_df['name'] == item_name]

    for num in range(15):
        x_list.append(num)

   
    
    yp_list = price_row_df.loc[price_row_df['name'] == item_name].values.tolist()
    new_yp_list = yp_list[0]
    new_yp_list.reverse()
    new_yp_list.pop()
    new_yp_list.reverse()
   

    yv_list = vol_row_df.loc[vol_row_df['name'] == item_name].values.tolist()
    new_yv_list = yv_list[0]
    new_yv_list.reverse()
    new_yv_list.pop()
    new_yv_list.reverse()
   

    for n in range(len(x_list)):
        data.append([x_list[n], new_yp_list[n], new_yv_list[n]])


    graph_df = pd.DataFrame(data, columns=['days_ago', 'price', 'volume'])



    fig,ax = plt.subplots()
    # make a plot
    ax.plot(graph_df.days_ago,
            graph_df.price,
            color="red",
            marker="o")
    # set x-axis label
    ax.set_xlabel("days ago", fontsize = 14)
    # set y-axis label
    ax.set_ylabel("price",
                color="red",
                fontsize=14)

    ax2=ax.twinx()
    # make a plot with different y-axis using second axis object
    ax2.plot(graph_df.days_ago, graph_df["volume"],color="blue",marker="o")
    ax2.set_ylabel("volume",color="blue",fontsize=14)
    plt.gca().invert_xaxis()
    plt.title(item_name)
    plt.savefig('foo.png')
    #plt.show(block=False)




    #------------------------------------------------------------------
    # extract and serve analysis_table and data_summary combined info

    # find analysis data on item_name
    analysis = analysis_df.loc[analysis_df['name'] == item_name].values.tolist()

    # extract analysis data on item_name as list
    analysis_data = analysis[0]
    analysis_data.reverse()
    analysis_data.pop()
    analysis_data.reverse()

    # extract today's summary data as a list
    summary = summary_df[:].values.tolist()
    summary_data = summary[0]
    summary_data.reverse()
    summary_data.pop()
    summary_data.reverse()

    # apply summary data to item_name's analysis data to get expected % increase today
    sum = 0
    calculated_data = []
    changes = []
    change = 0
    for n in range(8):
        change = analysis_data[n] * summary_data[n]
        changes.append(change)
        sum = sum + change
    for n in range(8, 16):
        if analysis_data[n] > 0:
            change = summary_data[n]
        elif analysis_data[n] < 0:
            change = 0 - summary_data[n]
        changes.append(change)
        sum = sum + change

    sum = round(sum, 5)

    # create output dictionary
    output_data = []
    has_effect = []
    fields = ['two_day_run_p', 'three_day_run_p', 'five_day_run_p',
        'seven_day_run_p', 'two_day_run_v', 'three_day_run_v', 'five_day_run_v',
        'seven_day_run_v', 'one_day_avg_p', 'three_day_avg_p', 'seven_day_avg_p', 'fourteen_day_avg_p',
                'one_day_avg_v', 'three_day_avg_v', 'seven_day_avg_v', 'fourteen_day_avg_v']
    for n in range(len(analysis_data)):
        if analysis_data[n] != 0:
            has_effect.append('Yes')
        else:
            has_effect.append('No')
        output_data.append([fields[n], has_effect[n], changes[n]])



    # print all outputs together
    output_df = pd.DataFrame(output_data, columns=['Attribute', 'Has Effect?', 'Effect'])
    print(tabulate(output_df, headers='keys', tablefmt = 'psq1'))
    #plt.show()
    #plt.savefig('graph.png')








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
    # open up ge-tracker.com to begin search
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







check_files()
analysis_data(item_name)
near_real_data(item_name)
