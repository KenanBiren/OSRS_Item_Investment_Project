import csv
import pandas as pd
import datetime



fields = ['two_day_run_p', 'three_day_run_p', 'five_day_run_p',
       'seven_day_run_p', 'two_day_run_v', 'three_day_run_v', 'five_day_run_v',
       'seven_day_run_v', 'one_day_avg_p', 'three_day_avg_p', 'seven_day_avg_p', 'fourteen_day_avg_p',
              'one_day_avg_v', 'three_day_avg_v', 'seven_day_avg_v', 'fourteen_day_avg_v']
data = []
current_date = datetime.date.today().strftime('%Y/%m/%d')
data.append(current_date)
## this script reads the analysis_table and build's today's data summary
df = pd.read_csv('/Users/kenanbiren/Documents/Data/analysis_table.csv')




result_list = df['one_day_avg_p']

for n in range(len(fields)):
    # data = df.loc[:, df.columns == field]
    # data_list = data.tolist()
    result = df[fields[n]].multiply(df["one_day_avg_p"], axis="index")
    number = result.mean()
    data.append(round(number, 5))


with open('/Users/kenanbiren/Documents/Data/data_summary.csv', mode='w') as f:
    writer = csv.writer(f)

    writer.writerow(['date'] + fields)
    writer.writerow((data))
