import pandas as pd
import csv
import datetime
import timedelta



## This script takes two 14day files (price and volume) and creates
## the analysis_table from them


# calculate data for run attributes
def get_run_data(price_list, vol_list):
    two_day_run_p = 0
    three_day_run_p = 0
    five_day_run_p = 0
    seven_day_run_p = 0
    two_day_run_v = 0
    three_day_run_v = 0
    five_day_run_v = 0
    seven_day_run_v = 0

    # PRICE

    # Calculate if item has been increasing or decreasing in price for 2 consecutive days
    if (price_list[0] > price_list[1] & price_list[1] > price_list[2]):
        two_day_run_p = 1
    elif (price_list[0] < price_list[1] & price_list[1] < price_list[2]):
        two_day_run_p = -1

    # Calculate if item has been inc/dec in price for 3 consecutive days
    if ((two_day_run_p == 1) & (price_list[2] > price_list[3])):
        three_day_run_p = 1
    elif ((two_day_run_p == -1) & (price_list[2] < price_list[3])):
        three_day_run_p = -1

    # Calculate if item has been inc/dec in price for 5 consecutive days
    if ((three_day_run_p == 1) & (price_list[3] > price_list[4]) & (price_list[4] > price_list[5])):
        five_day_run_p = 1
    elif ((three_day_run_p == -1) & (price_list[3] < price_list[4]) & (price_list[4] < price_list[5])):
        five_day_run_p = -1

    # Calculate if item has been inc/dec in price for 7 consecutive days
    if ((five_day_run_p == 1) & (price_list[5] > price_list[6]) & (price_list[6] > price_list[7])):
        seven_day_run_p = 1
    elif ((five_day_run_p == -1) & (price_list[5] < price_list[6]) & (price_list[6] < price_list[7])):
        seven_day_run_p = -1


    # VOLUME

    # Calculate if item has been increasing or decreasing in volume for 2 consecutive days
    if (vol_list[0] > vol_list[1] & vol_list[1] > vol_list[2]):
        two_day_run_v = 1
    elif (vol_list[0] < vol_list[1] & vol_list[1] < vol_list[2]):
        two_day_run_v = -1

    # Calculate if item has been inc/dec in vol for 3 consecutive days
    if ((two_day_run_v == 1) & (vol_list[2] > vol_list[3])):
        three_day_run_v = 1
    elif ((two_day_run_v == -1) & (vol_list[2] < vol_list[3])):
        three_day_run_v = -1

    # Calculate if item has been inc/dec in vol for 5 consecutive days
    if ((three_day_run_v == 1) & (vol_list[3] > vol_list[4]) & (vol_list[4] > vol_list[5])):
        five_day_run_v = 1
    elif ((three_day_run_v == -1) & (vol_list[3] < vol_list[4]) & (vol_list[4] < vol_list[5])):
        five_day_run_v = -1

    # Calculate if item has been inc/dec in vol for 7 consecutive days
    if ((five_day_run_v == 1) & (vol_list[5] > vol_list[6]) & (vol_list[6] > vol_list[7])):
        seven_day_run_v = 1
    elif ((five_day_run_v == -1) & (vol_list[5] < vol_list[6]) & (vol_list[6] < vol_list[7])):
        seven_day_run_v = -1

    return [two_day_run_p, three_day_run_p, five_day_run_p, seven_day_run_p,
            two_day_run_v, three_day_run_v, five_day_run_v, seven_day_run_v]


# calculate data for avg attributes
def get_avg_data(price_list, vol_list):
    one_day_avg_p = (price_list[0] - price_list[1]) / (price_list[1])
    three_day_avg_p = (price_list[0] - price_list[3]) / (price_list[3])
    seven_day_avg_p = (price_list[0] - price_list[7]) / (price_list[7])
    fourteen_day_avg_p = (price_list[0] - price_list[14]) / (price_list[14])

    one_day_avg_v = (vol_list[0] - vol_list[1]) / (vol_list[1] + 1)
    three_day_avg_v = (vol_list[0] - vol_list[3]) / (vol_list[3] + 1)
    seven_day_avg_v = (vol_list[0] - vol_list[7]) / (vol_list[7] + 1)
    fourteen_day_avg_v = (vol_list[0] - vol_list[14]) / (vol_list[14] + 1)

    data = [one_day_avg_p, three_day_avg_p, seven_day_avg_p, fourteen_day_avg_p,
            one_day_avg_v, three_day_avg_v, seven_day_avg_v, fourteen_day_avg_v]
    rounded_data = [round(item, 5) for item in data]

    return rounded_data




# code to run
working_df = {}

price_df = pd.read_csv('/home/ec2-user/OSRS_Item_Investment_App/data/14day_price.csv')
vol_df = pd.read_csv('/home/ec2-user/OSRS_Item_Investment_App/data/14day_vol.csv')



current_date = datetime.date.today()
# list of column names of scrapy_output.csv so the dataframe columns can be renamed
old_head = ['name']
new_head = ['name', '_0', '_1', '_2', '_3', '_4', '_5', '_6', '_7',
            '_8', '_9', '_10', '_11', '_12', '_13', '_14',]
for d in range(15):
    old_head.append((current_date - datetime.timedelta(days=d)).strftime('%Y/%m/%d'))
print(old_head)

# rename columns
for i in range(1,16):
    oh = old_head[i]
    nph = 'p' + new_head[i]
    nvh = 'v' + new_head[i]
    price_df.rename(columns={oh: nph}, inplace=True)
    vol_df.rename(columns={oh: nvh}, inplace=True)

# overwrite analysis_table.csv with column names, no data
analysis_header = ['name', 'two_day_run_p', 'three_day_run_p', 'five_day_run_p',
                   'seven_day_run_p', 'two_day_run_v', 'three_day_run_v',
                   'five_day_run_v', 'seven_day_run_v', 'one_day_avg_p',
                   'three_day_avg_p', 'seven_day_avg_p', 'fourteen_day_avg_p',
                   'one_day_avg_v', 'three_day_avg_v', 'seven_day_avg_v',
                   'fourteen_day_avg_v']
with open('/home/ec2-user/OSRS_Item_Investment_App/data/analysis_table.csv', mode='w') as f:
    writer = csv.writer(f)
    writer.writerow(analysis_header)
    f.close()

# combine name, run data, and avg data
for n in range(len(price_df.index)):
    name = price_df.loc[n, price_df.columns == 'name']
    namelist = name.tolist()
    prices = price_df.loc[n, price_df.columns != 'name']
    price_list = prices.tolist()
    vol = vol_df.loc[n, vol_df.columns != 'name']
    vol_list = vol.tolist()
    run_data = get_run_data(price_list, vol_list)
    avg_data = get_avg_data(price_list, vol_list)

    # add name, run data, and avg data to analysis_table.csv
    row = namelist + run_data + avg_data
    with open('/home/ec2-user/OSRS_Item_Investment_App/data/analysis_table.csv', mode='a') as f:
        writer = csv.writer(f)
        writer.writerow(row)
        f.close()






