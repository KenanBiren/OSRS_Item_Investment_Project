# This script will extract the attribute info (calculated from daily analysis)
# of the item searched by the user, along with the current daily summary values


# inputs: item_name from read_user_input
# outputs: price/volume graph, today's data for item_name


import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np


def analysis_data(item_name):
    working_df = {}

    price_df = pd.read_csv('/Users/kenanbiren/Documents/Data/14day_price.csv')
    vol_df = pd.read_csv('/Users/kenanbiren/Documents/Data/14day_vol.csv')
    analysis_df = pd.read_csv('/Users/kenanbiren/Documents/Data/analysis_table.csv')
    summary_df = pd.read_csv('/Users/kenanbiren/Documents/Data/data_summary.csv')



    #------------------------------------------------------------
    # Print a two-y-axis graph showing price and volume data
    data = []
    x_list = []
    price_row_df = price_df.loc[price_df['name'] == item_name]
    vol_row_df = vol_df.loc[vol_df['name'] == item_name]

    for num in range(15):
        x_list.append(num)

    # x_list.reverse()

    yp_list = price_row_df.loc[price_row_df['name'] == item_name].values.tolist()
    # yp_list[0].reverse()
    new_yp_list = yp_list[0]
    new_yp_list.pop()
    new_yp_list = [1544,1543,1552,1561,1560,1571,1580,1593,
            1597,1587,1597,1602,1601,1605,1600]


    yv_list = vol_row_df.loc[vol_row_df['name'] == item_name].values.tolist()
    # yv_list[0].reverse()
    new_yv_list = yv_list[0]
    new_yv_list.pop()
    new_yv_list = [33,34.5,85.5,39.5,28.5,52.6,18,58.5,30.6,
                85.5,45,22.8,55,34.4,30]
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
    plt.show(block=False)




    #------------------------------------------------------------------
    # Extract and serve analysis_table and data_summary combined info


    analysis = analysis_df.loc[analysis_df['name'] == item_name].values.tolist()

    analysis_data = analysis[0]
    analysis_data.reverse()
    analysis_data.pop()
    analysis_data.reverse()

    summary = summary_df[:].values.tolist()
    summary_data = summary[0]
    summary_data.reverse()
    summary_data.pop()
    summary_data.reverse()


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




    output_df = pd.DataFrame(output_data, columns=['Attribute', 'Has Effect?', 'Effect'])
    print(tabulate(output_df, headers='keys', tablefmt = 'psq1'))
    plt.show()
