import pandas as pd
import datetime
import timedelta
import csv
import os


# this script uses today's 14day_price.csv and 14day_vol.csv to create today's
# analysis_table.csv and data_summary.csv



# calculate if item has increased in (price, volume) for the past (2, 3, 5, 7)
# days consecutively
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


# calculate percent change in an item's daily average (price, volume) from 
# (1, 3, 7, 14) days ago
def get_avg_data(price_list, vol_list):
    # PRICE

    one_day_avg_p = (price_list[0] - price_list[1]) / (price_list[1])
    three_day_avg_p = (price_list[0] - price_list[3]) / (price_list[3])
    seven_day_avg_p = (price_list[0] - price_list[7]) / (price_list[7])
    fourteen_day_avg_p = (price_list[0] - price_list[14]) / (price_list[14])

    # VOLUME
    one_day_avg_v = (vol_list[0] - vol_list[1]) / (vol_list[1] + 1)
    three_day_avg_v = (vol_list[0] - vol_list[3]) / (vol_list[3] + 1)
    seven_day_avg_v = (vol_list[0] - vol_list[7]) / (vol_list[7] + 1)
    fourteen_day_avg_v = (vol_list[0] - vol_list[14]) / (vol_list[14] + 1)

    data = [one_day_avg_p, three_day_avg_p, seven_day_avg_p, fourteen_day_avg_p,
            one_day_avg_v, three_day_avg_v, seven_day_avg_v, fourteen_day_avg_v]
    rounded_data = [round(item, 5) for item in data]

    return rounded_data







# convert 14day csvs to pandas dataframes
price_df = pd.read_csv('data/14day_price.csv')
vol_df = pd.read_csv('data/14day_vol.csv')



# overwrite analysis_table.csv with header row (column names)
analysis_header = ['name', 'two_day_run_p', 'three_day_run_p', 'five_day_run_p',
                   'seven_day_run_p', 'two_day_run_v', 'three_day_run_v',
                   'five_day_run_v', 'seven_day_run_v', 'one_day_avg_p',
                   'three_day_avg_p', 'seven_day_avg_p', 'fourteen_day_avg_p',
                   'one_day_avg_v', 'three_day_avg_v', 'seven_day_avg_v',
                   'fourteen_day_avg_v']
with open('data/analysis_table.csv', mode='w') as f:
    writer = csv.writer(f)
    writer.writerow(analysis_header)
    f.close()

# combine each item's name, run data, and avg data into a row
for n in range(len(price_df.index)):
    name = price_df.loc[n, price_df.columns == 'name']
    namelist = name.tolist()
    prices = price_df.loc[n, price_df.columns != 'name']
    price_list = prices.tolist()
    vol = vol_df.loc[n, vol_df.columns != 'name']
    vol_list = vol.tolist()
    run_data = get_run_data(price_list, vol_list)
    avg_data = get_avg_data(price_list, vol_list)

    # add row of data produced above to analysis_table.csv
    row = namelist + run_data + avg_data
    with open('data/analysis_table.csv', mode='a') as f:
        writer = csv.writer(f)
        writer.writerow(row)
        f.close()



#-----------------------create data summary


fields = ['two_day_run_p', 'three_day_run_p', 'five_day_run_p',
       'seven_day_run_p', 'two_day_run_v', 'three_day_run_v', 'five_day_run_v',
       'seven_day_run_v', 'one_day_avg_p', 'three_day_avg_p', 'seven_day_avg_p', 'fourteen_day_avg_p',
              'one_day_avg_v', 'three_day_avg_v', 'seven_day_avg_v', 'fourteen_day_avg_v']
data = []
current_date = datetime.date.today().strftime('%Y/%m/%d')
data.append(current_date)

df = pd.read_csv('data/analysis_table.csv')
result_list = df['one_day_avg_p']

for n in range(len(fields)):
    # data = df.loc[:, df.columns == field]
    # data_list = data.tolist()
    result = df[fields[n]].multiply(df["one_day_avg_p"], axis="index")
    number = result.mean()
    data.append(round(number, 5))


with open('data/data_summary.csv', mode='w') as f:
    writer = csv.writer(f)
    writer.writerow(['date'] + fields)
    writer.writerow((data))

# once analysis is done, run script to test analysis output
os.system('python3 src/backend/transform/analysis/analysis_test.py')
           
